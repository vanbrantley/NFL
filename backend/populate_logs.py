import argparse
import datetime
from app import app, db
from models import Player, Game, PassingGameLog, RushingGameLog, ReceivingGameLog
import requests
from bs4 import BeautifulSoup


def main():
    app.app_context().push()

    def current_nfl_week(current_date):
        season_start_date = datetime.date(2023, 9, 5)
        days_passed = (current_date - season_start_date).days
        nfl_week = (days_passed // 7) + 1
        return nfl_week

    parser = argparse.ArgumentParser()
    parser.add_argument("--nfl_week", type=int, help="Current NFL week")
    args = parser.parse_args()

    current_date = datetime.date.today()

    current_week = (
        args.nfl_week if args.nfl_week is not None else current_nfl_week(current_date)
    )

    weeks_to_populate = (
        [current_week] if args.nfl_week is not None else list(range(1, current_week))
    )

    def find_full_name(shortened_name, player_names_list):
        # first try to match the full name directly
        for full_name in player_names_list:
            if full_name.startswith(shortened_name[0]) and full_name.endswith(
                shortened_name[2:]
            ):
                return full_name

        # if the direct match failed, remove the "Jr."s and try again
        shortened_name_without_jr = shortened_name.replace(" Jr.", "")
        for full_name in player_names_list:
            full_name_without_jr = full_name.replace(" Jr.", "")
            if full_name_without_jr.startswith(
                shortened_name_without_jr[0]
            ) and full_name_without_jr.endswith(shortened_name_without_jr[2:]):
                return full_name

        # if "Jr." removal still didn't match, compare last names
        shortened_last_name = shortened_name.split(" ")[-1]
        for full_name in player_names_list:
            last_name = full_name.split(" ")[-1]
            if last_name == shortened_last_name:
                return full_name

        # if the shortened name is "C. Anderson," return "Robbie Chosen"
        if shortened_name == "C. Anderson":
            return "Robbie Chosen"

        # if none of the above cases matched, return None
        return None

    # HTML structure:
    # div with away team stats id= player-stats-away
    # div with home team stats id= player-stats-home
    # inside of each of those - have a div with class_= stats-ctr-container
    # inside of that there's class_= passing-ctr, rushing-ctr, receiving-ctr
    # each of those has a div class_= stats_rows
    # with a table inside class_= stats-table

    def get_passing_logs(container, isHome):
        stats_rows = container.find("div", class_="stats-rows")

        player_rows = stats_rows.find_all("tr", class_="no-hover data-row")
        # print(player_rows)

        for player_row in player_rows:
            player_data = player_row.find_all("td")

            relevant_tds = [
                td
                for td in player_data
                if td.get("class") in [["name-element"], ["number-element"]]
            ]

            player_name = relevant_tds[0].get_text(strip=True)
            player_full_name = find_full_name(
                player_name, home_players_names if isHome else away_players_names
            )
            if player_full_name is None:
                error_message = f"No match found for {player_name}"
                raise ValueError(error_message)
            # print(player_full_name)

            player_id = (
                home_player_name_to_id[player_full_name]
                if isHome
                else away_player_name_to_id[player_full_name]
            )

            cp_att = relevant_tds[1].get_text(strip=True)
            completions, attempts = map(int, cp_att.split("/"))
            yards = relevant_tds[2].get_text(strip=True)
            touchdowns = relevant_tds[3].get_text(strip=True)
            interceptions = relevant_tds[4].get_text(strip=True)
            fantasy_points = relevant_tds[5].get_text(strip=True)

            passing_log = PassingGameLog(
                game_id=game_id,
                player_id=player_id,
                completions=completions,
                attempts=attempts,
                yards=yards,
                touchdowns=touchdowns,
                interceptions=interceptions,
                fantasy_points=fantasy_points,
            )

            passing_logs.append(passing_log)

    def get_rushing_logs(container, isHome):
        stats_rows = container.find("div", class_="stats-rows")

        player_rows = stats_rows.find_all("tr", class_="no-hover data-row")
        # print(player_rows)

        for player_row in player_rows:
            player_data = player_row.find_all("td")

            relevant_tds = [
                td
                for td in player_data
                if td.get("class") in [["name-element"], ["number-element"]]
            ]

            player_name = relevant_tds[0].get_text(strip=True)
            player_full_name = find_full_name(
                player_name, home_players_names if isHome else away_players_names
            )
            if player_full_name is None:
                error_message = f"No match found for {player_name}"
                raise ValueError(error_message)
            # print(player_full_name)

            player_id = (
                home_player_name_to_id[player_full_name]
                if isHome
                else away_player_name_to_id[player_full_name]
            )

            carries = relevant_tds[1].get_text(strip=True)
            yards = relevant_tds[2].get_text(strip=True)
            touchdowns = relevant_tds[3].get_text(strip=True)
            fantasy_points = relevant_tds[5].get_text(strip=True)

            rushing_log = RushingGameLog(
                game_id=game_id,
                player_id=player_id,
                carries=carries,
                yards=yards,
                touchdowns=touchdowns,
                fantasy_points=fantasy_points,
            )

            rushing_logs.append(rushing_log)

    def get_receiving_logs(container, isHome):
        stats_rows = container.find("div", class_="stats-rows")

        player_rows = stats_rows.find_all("tr", class_="no-hover data-row")
        # print(player_rows)

        for player_row in player_rows:
            player_data = player_row.find_all("td")

            relevant_tds = [
                td
                for td in player_data
                if td.get("class") in [["name-element"], ["number-element"]]
            ]

            player_name = relevant_tds[0].get_text(strip=True)
            player_full_name = find_full_name(
                player_name, home_players_names if isHome else away_players_names
            )
            if player_full_name is None:
                error_message = f"No match found for {player_name}"
                raise ValueError(error_message)
            # print(player_full_name)

            player_id = (
                home_player_name_to_id[player_full_name]
                if isHome
                else away_player_name_to_id[player_full_name]
            )

            targets = relevant_tds[1].get_text(strip=True)
            receptions = relevant_tds[2].get_text(strip=True)
            yards = relevant_tds[3].get_text(strip=True)
            touchdowns = relevant_tds[4].get_text(strip=True)
            fantasy_points = relevant_tds[6].get_text(strip=True)

            receiving_log = ReceivingGameLog(
                game_id=game_id,
                player_id=player_id,
                targets=targets,
                receptions=receptions,
                yards=yards,
                touchdowns=touchdowns,
                fantasy_points=fantasy_points,
            )

            receiving_logs.append(receiving_log)

    # html_classes = {

    # }

    for week in weeks_to_populate:
        try:
            print(f"Adding week {week} game logs...")

            rushing_logs = []
            passing_logs = []
            receiving_logs = []

            home_player_name_to_id = {}
            away_player_name_to_id = {}

            games = Game.query.filter_by(week=week).all()

            # loop through games
            for game in games:
                game_id = game.game_id
                home_team_id = game.home_team_id
                home_team_abbreviation = game.home_team.abbreviation
                away_team_id = game.away_team_id
                away_team_abbreviation = game.away_team.abbreviation
                box_score_url = game.box_score_url

                home_players = Player.query.filter_by(team_id=home_team_id).all()
                away_players = Player.query.filter_by(team_id=away_team_id).all()

                home_player_name_to_id.update(
                    {player.player_name: player.player_id for player in home_players}
                )
                away_player_name_to_id.update(
                    {player.player_name: player.player_id for player in away_players}
                )

                home_players_names = [player.player_name for player in home_players]
                away_players_names = [player.player_name for player in away_players]

                # print(box_score_url)

                response = requests.get(box_score_url)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")

                    print(
                        f"Adding {away_team_abbreviation} @ {home_team_abbreviation} game logs..."
                    )

                    home_team_stats_container = soup.find("div", id="player-stats-home")
                    away_team_stats_container = soup.find("div", id="player-stats-away")
                    if (
                        home_team_stats_container is None
                        or away_team_stats_container is None
                    ):
                        error_message = "Error: Stats container not found. Check the web page structure."
                        raise ValueError(error_message)

                    home_team_stats = home_team_stats_container.find(
                        "div", class_="stats-ctr-container"
                    )
                    away_team_stats = away_team_stats_container.find(
                        "div", class_="stats-ctr-container"
                    )
                    if home_team_stats is None or away_team_stats is None:
                        error_message = "Error: Stats inner container not found. Check the web page structure."
                        raise ValueError(error_message)

                    home_team_passing = home_team_stats.find(
                        "div", class_="passing-ctr"
                    )
                    if home_team_passing is None:
                        error_message = "Error: Home team passing stats not found. Check the web page structure."
                        raise ValueError(error_message)
                    home_team_rushing = home_team_stats.find(
                        "div", class_="rushing-ctr"
                    )
                    home_team_receiving = home_team_stats.find(
                        "div", class_="receiving-ctr"
                    )
                    away_team_passing = away_team_stats.find(
                        "div", class_="passing-ctr"
                    )
                    away_team_rushing = away_team_stats.find(
                        "div", class_="rushing-ctr"
                    )
                    away_team_receiving = away_team_stats.find(
                        "div", class_="receiving-ctr"
                    )

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
                    print(
                        f"Failed to retrieve data from {box_score_url}. Status code: {response.status_code}"
                    )

            db.session.add_all(passing_logs)
            db.session.add_all(rushing_logs)
            db.session.add_all(receiving_logs)
            db.session.commit()  # Commit once after adding all players
            print(f"Successfully added week {week} game logs ✅")

        except Exception as e:
            print(f"Error inserting data for week {week}: {str(e)}")


if __name__ == "__main__":
    main()
