import os
import re
import pandas as pd
from termcolor import colored

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

# Function to calculate global average for a player and his opponent
def calculate_global_average(player_name, player_matches):
    columns_to_average = {
        'Minutes': 'minutes', 'Winner Ace': 'w_ace', 'Winner Double Fault': 'w_df',
        'Winner Service Points': 'w_svpt', 'Winner First Serve In': 'w_1stIn',
        'Winner First Serve Won': 'w_1stWon', 'Winner Second Serve Won': 'w_2ndWon',
        'Winner Service Games': 'w_SvGms', 'Winner Break Points Saved': 'w_bpSaved',
        'Winner Break Points Faced': 'w_bpFaced', 'Loser Ace': 'l_ace', 'Loser Double Fault': 'l_df',
        'Loser Service Points': 'l_svpt', 'Loser First Serve In': 'l_1stIn',
        'Loser First Serve Won': 'l_1stWon', 'Loser Second Serve Won': 'l_2ndWon',
        'Loser Service Games': 'l_SvGms', 'Loser Break Points Saved': 'l_bpSaved',
        'Loser Break Points Faced': 'l_bpFaced'
    }

    player_and_opponent_stats = player_matches[list(columns_to_average.values())]
    global_average = player_and_opponent_stats.mean()

    print(f"\n[{player_name}] Global Average Statistics:")
    for column, value in global_average.items():
        colored_column = colored(column, 'cyan', attrs=['bold'])
        colored_value = colored(f'{value:.2f}', 'yellow', attrs=['bold'])
        print(f"{colored_column}: {colored_value}")

    winner_matches = player_matches[player_matches['winner_id'] == player_id]
    loser_matches = player_matches[player_matches['loser_id'] == player_id]

    if not winner_matches.empty:
        print(colored(f"\nStats when {player_name} won:", 'green', attrs=['bold']))
        print_stats(winner_matches[columns_to_average.values()], columns_to_average)

    if not loser_matches.empty:
        print(colored(f"\nStats when {player_name} lost:", 'red', attrs=['bold']))
        print_stats(loser_matches[columns_to_average.values()], columns_to_average)




# Welcome message and instructions for the user
print(colored("----------------------------------", 'green'))
print(colored("ATP Tennis Player Statistics", 'green'))
print(colored("----------------------------------", 'green'))
print("")
print(colored("This tool is designed  to search specifics tennis player statistics for ATP players.", 'green'))
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
print(colored("Thank you for using the ATP Tennis Player Statistics.", 'green'))
print("")

# Define the directory containing the matches CSV files
matches_dir = '/Users/charles/Desktop/TENNIS/tennis_atp-master'

# Define the file name of the players CSV file
players_file = 'atp_players.csv'

# Load all the matches CSV files into a single DataFrame
matches_files = [f for f in os.listdir(matches_dir) if f.startswith('atp_matches_') and re.search(r'\d{4}', f).group(0) >= '2014']
matches_files.sort(key=lambda x: int(re.search(r'\d{4}', x).group(0)), reverse=True)

matches_data = [pd.read_csv(os.path.join(matches_dir, filename)) for filename in matches_files]
matches_df = pd.concat(matches_data)

# Load the players CSV file into a DataFrame
players_df = pd.read_csv(os.path.join(matches_dir, players_file))

# Function to calculate global average for a player and his opponent
def calculate_global_average(player_matches):
    columns_to_average = {
        'Minutes': 'minutes', 'Winner Ace': 'w_ace', 'Winner Double Fault': 'w_df',
        'Winner Service Points': 'w_svpt', 'Winner First Serve In': 'w_1stIn',
        'Winner First Serve Won': 'w_1stWon', 'Winner Second Serve Won': 'w_2ndWon',
        'Winner Service Games': 'w_SvGms', 'Winner Break Points Saved': 'w_bpSaved',
        'Winner Break Points Faced': 'w_bpFaced', 'Loser Ace': 'l_ace', 'Loser Double Fault': 'l_df',
        'Loser Service Points': 'l_svpt', 'Loser First Serve In': 'l_1stIn',
        'Loser First Serve Won': 'l_1stWon', 'Loser Second Serve Won': 'l_2ndWon',
        'Loser Service Games': 'l_SvGms', 'Loser Break Points Saved': 'l_bpSaved',
        'Loser Break Points Faced': 'l_bpFaced'
    }

    player_and_opponent_stats = player_matches[list(columns_to_average.values())]
    global_average = player_and_opponent_stats.mean()

    return global_average

# Flag to control the search loop
perform_another_search = True

while perform_another_search:
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
    player_matches = get_player_matches(player_name, opponent_name=opponent_name if opponent_name else None,
                                        tournament_name=tournament_name if tournament_name else None,
                                        surface=surface if surface else None,
                                        year=year if year else None, round_=round_ if round_ else None)

    # Check if any matches were found
    if player_matches is not None and len(player_matches) > 0:
        # Calculate global average for the player and his opponent
        player_global_average = calculate_global_average(player_matches)

        print("\nGlobal Average Statistics:")
        for column, value in player_global_average.items():
            colored_column = colored(column, 'cyan', attrs=['bold'])
            colored_value = colored(f'{value:.2f}', 'yellow', attrs=['bold'])
            print(f"{colored_column}: {colored_value}")

    else:
        print("No matches found. Check filters and retry.")

    another_search = input("Do you want to perform another search? (yes/no): ").lower()

    if another_search != 'yes':
        perform_another_search = False  # Set the variable to False to exit the loop

