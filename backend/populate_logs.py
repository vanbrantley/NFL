import sys
from app import app, db, Team, Player, Game, PassingGameLog, RushingGameLog, ReceivingGameLog
import requests
from bs4 import BeautifulSoup

def main():
    
    # week number command line argument checks
    if len(sys.argv) != 2:
        print("Usage: python3 populate_logs.py <week_number>")
        return

    week_number = sys.argv[1]
    if not week_number.isdigit():
        print("Week number must be a positive integer between 1 and 18.")
        return

    week_number = int(week_number)
    if week_number < 1 or week_number > 18:
        print("Week number must be between 1 and 18.")
        return

    # If all checks pass, you can proceed with your script logic here
    print(f"Fetching game logs for week {week_number}...")

    # Create an application context
    app.app_context().push()

    def find_full_name(shortened_name, player_names_list):
        # First, try to match the full name directly
        for full_name in player_names_list:
            if full_name.startswith(shortened_name[0]) and full_name.endswith(shortened_name[2:]):
                return full_name

        # If the direct match failed, remove "Jr." and try again
        shortened_name = shortened_name.replace(" Jr.", "")
        for full_name in player_names_list:
            full_name = full_name.replace(" Jr.", "")
            if full_name.startswith(shortened_name[0]) and full_name.endswith(shortened_name[2:]):
                return full_name

        # If the "Jr." removal still didn't match, try comparing last names
        shortened_last_name = shortened_name.split(" ")[-1]
        for full_name in player_names_list:
            last_name = full_name.split(" ")[-1]
            if last_name == shortened_last_name:
                return full_name

        # If the shortened name is "C. Anderson," return "Robbie Chosen"
        if shortened_name == "C. Anderson":
            return "Robbie Chosen"

        # If none of the above cases matched, return None
        return None
    

    # div with away team stats id= player-stats-away
    # div with home team stats id= player-stats-home

    # inside of each of those - have a div with class_= stats-ctr-container
    # inside of that there's class_= passing-ctr, rushing-ctr, receiving-ctr

    # each of those has a div class_= stats_rows
    # with a table inside class_= stats-table

    def get_passing_logs(container, isHome):
        # Find the div with class 'stats-rows' inside 'home_team_rushing'
        stats_rows = container.find('div', class_='stats-rows')

        # Find all 'tr' elements with class 'no-hover data-row'
        player_rows = stats_rows.find_all('tr', class_='no-hover data-row')
        # print(player_rows)

        # Loop through each player's row and extract the data
        for player_row in player_rows:
            # Find all 'td' elements within the player's row
            player_data = player_row.find_all('td')

            # Use a list comprehension to select relevant 'td' elements
            relevant_tds = [td for td in player_data if td.get('class') in [['name-element'], ['number-element']]]

            # Extract data from the relevant 'td' elements
            player_name = relevant_tds[0].get_text(strip=True)
            player_full_name = find_full_name(player_name, home_players_names if isHome else away_players_names)
            if player_full_name is None:
                error_message = f"No match found for {player_name}"
                raise ValueError(error_message)
            # print(player_full_name)
            cp_att = relevant_tds[1].get_text(strip=True)
            completions, attempts = map(int, cp_att.split('/'))
            yards = relevant_tds[2].get_text(strip=True)
            touchdowns = relevant_tds[3].get_text(strip=True)
            interceptions = relevant_tds[4].get_text(strip=True)
            fantasy_points = relevant_tds[5].get_text(strip=True)

            passing_log = PassingGameLog(
                game_id = game_id,
                player_name = player_full_name,
                completions = completions,
                attempts = attempts,
                yards = yards,
                touchdowns = touchdowns,
                interceptions = interceptions,
                fantasy_points = fantasy_points
            )

            passing_logs.append(passing_log)

    def get_rushing_logs(container, isHome):
        # Find the div with class 'stats-rows' inside 'home_team_rushing'
        stats_rows = container.find('div', class_='stats-rows')

        # Find all 'tr' elements with class 'no-hover data-row'
        player_rows = stats_rows.find_all('tr', class_='no-hover data-row')
        # print(player_rows)

        # Loop through each player's row and extract the data
        for player_row in player_rows:
            # Find all 'td' elements within the player's row
            player_data = player_row.find_all('td')

            # Use a list comprehension to select relevant 'td' elements
            relevant_tds = [td for td in player_data if td.get('class') in [['name-element'], ['number-element']]]

            # Extract data from the relevant 'td' elements
            player_name = relevant_tds[0].get_text(strip=True)
            player_full_name = find_full_name(player_name, home_players_names if isHome else away_players_names)
            if player_full_name is None:
                error_message = f"No match found for {player_name}"
                raise ValueError(error_message)
            # print(player_full_name)
            carries = relevant_tds[1].get_text(strip=True)
            yards = relevant_tds[2].get_text(strip=True)
            touchdowns = relevant_tds[3].get_text(strip=True)
            fantasy_points = relevant_tds[5].get_text(strip=True)

            rushing_log = RushingGameLog(
                game_id = game_id,
                player_name = player_full_name,
                carries = carries,
                yards = yards,
                touchdowns = touchdowns,
                fantasy_points = fantasy_points
            )

            rushing_logs.append(rushing_log)

    def get_receiving_logs(container, isHome):
        # Find the div with class 'stats-rows' inside 'home_team_rushing'
        stats_rows = container.find('div', class_='stats-rows')

        # Find all 'tr' elements with class 'no-hover data-row'
        player_rows = stats_rows.find_all('tr', class_='no-hover data-row')
        # print(player_rows)

        # Loop through each player's row and extract the data
        for player_row in player_rows:
            # Find all 'td' elements within the player's row
            player_data = player_row.find_all('td')

            # Use a list comprehension to select relevant 'td' elements
            relevant_tds = [td for td in player_data if td.get('class') in [['name-element'], ['number-element']]]

            # Extract data from the relevant 'td' elements
            player_name = relevant_tds[0].get_text(strip=True)
            player_full_name = find_full_name(player_name, home_players_names if isHome else away_players_names)
            if player_full_name is None:
                error_message = f"No match found for {player_name}"
                raise ValueError(error_message)
            # print(player_full_name)
            targets = relevant_tds[1].get_text(strip=True)
            receptions = relevant_tds[2].get_text(strip=True)
            yards = relevant_tds[3].get_text(strip=True)
            touchdowns = relevant_tds[4].get_text(strip=True)
            fantasy_points = relevant_tds[6].get_text(strip=True)

            receiving_log = ReceivingGameLog(
                game_id = game_id,
                player_name = player_full_name,
                targets = targets,
                receptions = receptions,
                yards = yards,
                touchdowns = touchdowns,
                fantasy_points = fantasy_points
            )

            receiving_logs.append(receiving_log)

    try:

        rushing_logs = []
        passing_logs = []
        receiving_logs = []

        # fetch games for that week from the games table
        games = Game.query.filter_by(week=week_number).all()

        # loop through games
        for game in games:

            game_id = game.game_id
            home_team_abbreviation = game.home_team_abbreviation
            away_team_abbreviation = game.away_team_abbreviation
            box_score_url = game.box_score_url

            home_players = Player.query.filter_by(team_abbreviation=home_team_abbreviation).all()
            home_players_names = [player.player_name for player in home_players]
            away_players = Player.query.filter_by(team_abbreviation=away_team_abbreviation).all()
            away_players_names = [player.player_name for player in away_players]

            # print(box_score_url)

            response = requests.get(box_score_url)

            if response.status_code == 200:

                soup = BeautifulSoup(response.text, 'html.parser')

                print(f"Adding {away_team_abbreviation} @ {home_team_abbreviation} game logs...")

                home_team_stats_container = soup.find('div', id="player-stats-home")
                away_team_stats_container = soup.find('div', id="player-stats-away")

                home_team_stats = home_team_stats_container.find('div', class_='stats-ctr-container')
                away_team_stats = away_team_stats_container.find('div', class_='stats-ctr-container')

                home_team_passing = home_team_stats.find('div', class_='passing-ctr')
                home_team_rushing = home_team_stats.find('div', class_='rushing-ctr')
                home_team_receiving = home_team_stats.find('div', class_='receiving-ctr')
                away_team_passing = away_team_stats.find('div', class_='passing-ctr')
                away_team_rushing = away_team_stats.find('div', class_='rushing-ctr')
                away_team_receiving = away_team_stats.find('div', class_='receiving-ctr')

                # print(home_team_passing)
                # print(home_team_rushing)
                # print(home_team_receiving)
                # print(away_team_passing)
                # print(away_team_rushing)
                # print(away_team_receiving)

                get_passing_logs(home_team_passing, True)
                get_rushing_logs(home_team_rushing, True)
                get_receiving_logs(home_team_receiving, True)
                get_passing_logs(away_team_passing, False)
                get_rushing_logs(away_team_rushing, False)
                get_receiving_logs(away_team_receiving, False)

            else:
                print(f"Failed to retrieve data from {box_score_url}. Status code: {response.status_code}")

        db.session.add_all(passing_logs)
        db.session.add_all(rushing_logs)
        db.session.add_all(receiving_logs)
        db.session.commit()  # Commit once after adding all players
        print(f"Successfully added week {week_number} logs ✅")

    except Exception as e:
        print(f"Error inserting data: {str(e)}")


if __name__ == "__main__":
    main()
