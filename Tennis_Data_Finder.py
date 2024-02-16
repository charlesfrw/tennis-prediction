import os
import pandas as pd
import re
from termcolor import colored


# Welcome message and instructions for the user
print(colored("--------------------------------------------------", 'green'))
print(colored("Welcome to the ATP Tennis Data Finder Tool", 'green'))
print(colored("--------------------------------------------------", 'green'))
print("")
print(colored("This tool is designed to allow you to find specific match data for ATP players.", 'green'))
print("")
print(colored("To use this tool, please follow these steps:", 'green'))
print(colored("1. Enter the name of the player you wish to search for.", 'green'))
print(colored("2. Optionally, enter the name of the opponent you wish to filter by.", 'green'))
print(colored("3. Optionally, enter the name of the tournament you wish to filter by.", 'green'))
print(colored("4. Optionally, enter the surface you wish to filter by.", 'green'))
print(colored("5. Optionally, enter the year you wish to filter by.", 'green'))
print(colored("6. Optionally, enter the round you wish to filter by.", 'green'))
print("")
print(colored("After entering your search criteria, please choose whether you wish to download the matches data as a CSV file or preview it on the console.", 'green'))
print("")
print(colored("Please note that this tool only includes data for matches played since 2014.", 'green'))
print("")
print(colored("Thank you for using the ATP Tennis Data Finder Tool.", 'green'))
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

# ... (le reste de votre code avant la boucle while)

# ... (le reste de votre code avant la boucle while)

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

        # Ask the user if they want to download the file or just preview it
        download_choice = input("Do you want to download the file or just preview it? (d/p): ")

        # Save the matches played by the player to a CSV file on the desktop
        if download_choice == 'd':
            # Get the path to the desktop
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

            # Create the file name using the player and opponent names
            file_name = f'Result_{player_name}_{opponent_name}_{filter_info}.csv'

            # Save the matches played by the player to a CSV file on the desktop
            player_matches.to_csv(os.path.join(desktop_path, file_name), index=False)

            # Print a message to indicate that the file has been saved
            print(f"The file '{file_name}' has been saved to your desktop.")

        # Preview the matches played by the player
        elif download_choice == 'p':
            # Print the first 5 rows of the matches played by the player
            print(player_matches.head())

        # Invalid choice
        else:
            print("Invalid choice. Please choose 'd' to download the file or 'p' to preview it.")

    else:
        print("No matches found.")

    # Ask the user if they want to perform another search
    another_search = input("Do you want to perform another search? (yes/no): ").lower()

    # Check if the user wants to perform another search
    if another_search != 'yes':
        perform_another_search = False  # Set the variable to False to exit the loop



