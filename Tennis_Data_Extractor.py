import os
import pandas as pd
import re
from termcolor import colored

# Welcome message and instructions for the user
print(colored("--------------------------------------------------", 'green'))
print(colored("Welcome to the ATP Tennis Match Data Extractor Tool", 'green'))
print(colored("--------------------------------------------------", 'green'))
print("")
print(colored("This tool is designed to allow you to extract tennis data needed for Machine Learning.", 'green'))
print("")
print(colored("To use this tool, please follow these steps:", 'green'))
print(colored("1. Enter the name of the player you wish to search for.", 'green'))
print(colored("2. Optionally, enter the name of the opponent you wish to filter by.", 'green'))
print(colored("3. Optionally, enter the name of the tournament you wish to filter by.", 'green'))
print(colored("4. Optionally, enter the surface you wish to filter by.", 'green'))
print(colored("5. Optionally, enter the year you wish to filter by.", 'green'))
print(colored("6. Optionally, enter the round you wish to filter by.", 'green'))
print("")
print(colored("Please note that this tool only includes data for matches played since 2014.", 'green'))
print("")
print(colored("Thank you for using the ATP Tennis Match Data Extractor Tool.", 'green'))
print("")

# Define the directory containing the matches CSV files
matches_dir = '/Users/charles/Desktop/TENNIS/tennis_atp-master'

# Define the file name of the players CSV file
players_file = 'atp_players.csv'

# Find all the matches CSV files in the directory
matches_files = [f for f in os.listdir(matches_dir) if f.startswith('atp_matches_') and re.search(r'\d{4}', f).group(0) >= '2014']

# Sort the matches CSV files by year (descending order)
matches_files.sort(key=lambda x: int(re.search(r'\d{4}', x).group(0)), reverse=True)

# Load all the matches CSV files into a single DataFrame
matches_data = []
for filename in matches_files:
    matches_df = pd.read_csv(os.path.join(matches_dir, filename))
    matches_data.append(matches_df)
matches_df = pd.concat(matches_data)

# Load the players CSV file into a DataFrame
players_df = pd.read_csv(os.path.join(matches_dir, players_file))

# Define a function to find the matches played by a given player
def get_player_matches(player_name, opponent_name=None, tournament_name=None, surface=None, year=None, round_=None):
    # Find the player ID based on the player name
    query = (players_df['name_first'].str.lower() == player_name.lower().split()[0]) & \
            (players_df['name_last'].str.lower() == player_name.lower().split()[1])
    player_id = players_df.loc[query, 'player_id'].values[0]

    # Filter the matches DataFrame by player
    player_matches = matches_df[(matches_df['winner_id'] == player_id) | (matches_df['loser_id'] == player_id)]

    # Filter the matches DataFrame by opponent (if specified)
    if opponent_name is not None:
        query = (players_df['name_first'].str.lower() == opponent_name.lower().split()[0]) & \
                (players_df['name_last'].str.lower() == opponent_name.lower().split()[1])
        opponent_id = players_df.loc[query, 'player_id'].values[0]
        player_matches = player_matches[(player_matches['winner_id'] == opponent_id) | (player_matches['loser_id'] == opponent_id)]

    # Filter the matches DataFrame by tournament (if specified)
    if tournament_name is not None:
        player_matches = player_matches[player_matches['tourney_name'].str.contains(tournament_name, case=False)]

    # Filter the matches DataFrame by surface (if specified)
    if surface is not None:
        player_matches = player_matches[player_matches['surface'] == surface]

    # Convert tourney_date column to string type
    player_matches.loc[:, 'tourney_date'] = player_matches['tourney_date'].astype(str)

    # Filter the matches DataFrame by year (if specified)
    if year is not None:
        player_matches = player_matches[player_matches['tourney_date'].str.contains(str(year), na=False)]

    # Convert round column to lowercase
    player_matches.loc[:, 'round'] = player_matches['round'].str.lower()

    # Filter the matches DataFrame by round (if specified)
    if round_ is not None:
        player_matches = player_matches[player_matches['round'].str.contains(round_.lower(), case=False)]

    # Return the matches played by the player
    return player_matches

# Adapted code for filtering and saving data separately

perform_another_search = True

while perform_another_search:
    # Print a new line and the search number between dashed lines
    print("")
    print(colored("--------------------------------------------------", 'green'))
    print(colored(f"New Search", 'green'))
    print(colored("--------------------------------------------------", 'green'))
    print("")
    
    # Ask the user for the name of the player
    player_name = input("Enter the name of the player (e.g. Roger Federer): ")

    # Ask the user for the name of the opponent (if any)
    opponent_name = input("Enter the name of the opponent (leave blank if you want all): ")

    # Ask the user for the name of the tournament (if any)
    tournament_name = input("Enter the name of the tournament (leave blank if all): ")

    # Ask the user for the surface (if any)
    surface = input("Enter the surface (e.g. Hard, Clay, Grass) (leave blank if all): ")

    # Ask the user for the year (if any)
    year = input("Enter the year (YYYY) (leave blank if all year since 2014): ")

    # Ask the user for the round (if any)
    round_ = input("Enter the round (e.g. F, SF, QF, RR, R16, R32, R64, R128) (leave blank if not applicable): ")

    # Call the function to get the matches played by the player
    player_matches = get_player_matches(player_name, opponent_name=opponent_name if opponent_name else None, tournament_name=tournament_name if tournament_name else None, surface=surface if surface else None, year=year if year else None, round_=round_ if round_ else None)

    # Check if any matches were found
    if player_matches is not None and len(player_matches) > 0:
        # Define filter_info using the user's search criteria
        filter_info = f'{tournament_name}_{surface}_{year}_{round_}'.replace(" ", "_").replace(",", "")

        # Define a dictionary to store different sets of filtered data
        filtered_data = {}

        # Extract and store data for each combination of filters
        filtered_data['Players_Opponent'] = player_matches
        filtered_data['Player_Year'] = get_player_matches(player_name, year=year if year else None)
        filtered_data['Player_Surface'] = get_player_matches(player_name, surface=surface if surface else None)
        filtered_data['Player_Tourney'] = get_player_matches(player_name, tournament_name=tournament_name if tournament_name else None)
        filtered_data['Player_Round'] = get_player_matches(player_name, round_=round_ if round_ else None)
        filtered_data['Opponent_Year'] = get_player_matches(opponent_name, year=year if year else None)
        filtered_data['Opponent_Surface'] = get_player_matches(opponent_name, surface=surface if surface else None)
        filtered_data['Opponent_Tourney'] = get_player_matches(opponent_name, tournament_name=tournament_name if tournament_name else None)
        filtered_data['Opponent_Round'] = get_player_matches(opponent_name, round_=round_ if round_ else None)

        # Concatenate all filtered data into one DataFrame
        all_data = pd.concat(filtered_data.values(), keys=filtered_data.keys())

        # Save the concatenated data to a single CSV file on the desktop
        all_file_name = f'AllResults.csv'
        desktop_path = '/Users/charles/Desktop/TENNIS/Data'
        all_data.to_csv(os.path.join(desktop_path, all_file_name), index=False)
        print(f"The file '{all_file_name}' containing all results has been saved to data file.")

    # Ask the user if they want to perform another search
    another_search = input("Do you want to perform another search? (yes/no): ").lower()

    # Check if the user wants to perform another search
    if another_search != 'yes':
        perform_another_search = False  # Set the variable to False to exit the loop
