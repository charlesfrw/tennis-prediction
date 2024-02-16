import requests
from bs4 import BeautifulSoup

ATP_RANKINGS_URL = "https://www.atptour.com/en/rankings/singles"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
SELECTOR_RANKING_TABLE = 'table.mega-table'

def make_request(url):
    headers = {'User-Agent': USER_AGENT}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.content
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def parse_ranking_table(content, num_players):
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        ranking_table = soup.find('table', class_='mega-table')
        if ranking_table:
            return extract_rankings(ranking_table, num_players)
        else:
            print("ATP singles rankings table not found on the page.")
    return None

def extract_rankings(ranking_table, num_players):
    atp_rankings = []
    for row in ranking_table.find_all('tr')[1:num_players + 1]:
        columns = row.find_all('td')
        if len(columns) >= 3:
            rank = columns[0].text.strip()
            player = columns[1].text.replace('\n', '').strip()
            points = columns[2].text.strip()
            atp_rankings.append({'Rank': rank, 'Player': player, 'Points': points})
        else:
            print("Insufficient data in a row. Skipping.")
    return atp_rankings

def display_rankings(atp_rankings):
    if atp_rankings:
        print("\033[93m" + "-"*40)  # ANSI escape code for yellow color
        print("\033[93mTENNIS ATP RANKINGS")
        print("\033[93m" + "-"*40)
        
        for player_info in atp_rankings:
            print(f"{player_info['Rank']}. {player_info['Player']} - {player_info['Points']} points")

def get_user_input():
    while True:
        user_input = input("\033[93mDo you want to see more rankings? (yes/no): ").lower()
        if user_input in ('yes', 'no'):
            return user_input
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    num_players_to_display = 15

    while True:
        content = make_request(ATP_RANKINGS_URL)
        atp_rankings = parse_ranking_table(content, num_players_to_display)

        if atp_rankings:
            display_rankings(atp_rankings)
            user_input = get_user_input()

            if user_input == 'yes':
                num_players_to_display += 15
            else:
                print("Exiting.")
                break
        else:
            print("No ATP singles rankings available.")
            break

if __name__ == "__main__":
    main()
