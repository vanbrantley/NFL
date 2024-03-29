from app import app, db
from models import Team, Player
import requests
from bs4 import BeautifulSoup

app.app_context().push()


def update_player_name_if_match(player, db_team_players):
    potential_matches = []

    # find potential matches based on last name
    player_last_name = player.player_name.split(" ")[-1]
    for db_team_player in db_team_players:
        db_team_player_last_name = db_team_player.player_name.split(" ")[-1]
        if db_team_player_last_name == player_last_name:
            potential_matches.append(db_team_player)

    print("Potential matches: ")
    print(potential_matches)
    # go through matches, comparing other fields
    for potential_match in potential_matches:
        if (
            potential_match.position == player.position
            and potential_match.jersey_number == player.jersey_number
            # and potential_match.height == player.height
            # and potential_match.weight == player.weight
            and potential_match.college == player.college
        ):
            print("Potential match name: " + potential_match.player_name)
            print("Departed player name: " + player.player_name)
            # if they match, update player's name & add to name_change_players
            potential_match.player_name = player.player_name
            print("new name set!!")
            return potential_match

    return None


try:
    nfl_teams = {
        # "buffalo-bills": "BUF",
        # "miami-dolphins": "MIA",
        # "new-england-patriots": "NE",
        "new-york-jets": "NYJ",
        # "baltimore-ravens": "BAL",
        # "cincinnati-bengals": "CIN",
        # "cleveland-browns": "CLE",
        # "pittsburgh-steelers": "PIT",
        # "houston-texans": "HOU",
        # "indianapolis-colts": "IND",
        # "jacksonville-jaguars": "JAC",
        # "tennessee-titans": "TEN",
        # "denver-broncos": "DEN",
        # "kansas-city-chiefs": "KC",
        # "los-angeles-chargers": "LAC",
        # "las-vegas-raiders": "LV",
        # "dallas-cowboys": "DAL",
        # "new-york-giants": "NYG",
        # "philadelphia-eagles": "PHI",
        # "washington-commanders": "WAS",
        # "chicago-bears": "CHI",
        # "detroit-lions": "DET",
        # "green-bay-packers": "GB",
        # "minnesota-vikings": "MIN",
        # "atlanta-falcons": "ATL",
        # "carolina-panthers": "CAR",
        # "new-orleans-saints": "NO",
        # "tampa-bay-buccaneers": "TB",
        # "arizona-cardinals": "ARI",
        # "los-angeles-rams": "LAR",
        # "san-francisco-49ers": "SF",
        # "seattle-seahawks": "SEA",
    }

    html_classes = {
        "players-table": "d3-o-table",
        "player_name": "nfl-o-roster__player-name",
    }

    players_new_to_db = []
    players_with_updated_names = []
    players_with_new_teams = []
    departed_players = []

    # loop through team dictionary items
    for team, abbreviation in nfl_teams.items():
        print(f"Checking rosters for Team: {abbreviation}")

        # Construct the URL for the team's roster page
        url = f"https://www.nfl.com/teams/{team}/roster"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            players_table = soup.find("table", class_=html_classes["players-table"])
            if players_table is None:
                error_message = "Players table not found. Check the web page structure."
                raise ValueError(error_message)

            rows = players_table.find_all("tr")
            if rows is None:
                error_message = "Players rows not found. Check the web page structure."
                raise ValueError(error_message)

            team_obj = Team.query.filter_by(abbreviation=abbreviation).first()
            if team_obj is None:
                error_message = (
                    f"Team with abbreviation {abbreviation} not found in the database."
                )
                raise ValueError(error_message)

            team_id = team_obj.team_id

            nfl_roster_names = []
            db_team_players = Player.query.filter_by(team_id=team_id).all()
            db_roster_names = [player.player_name for player in db_team_players]

            # so now want to add players to removed_players and new_players in here, not after the loop
            for row in players_table.find_all("tr")[1:]:
                cells = row.find_all("td")
                player_name_pic = cells[0]
                player_name_link = player_name_pic.find(
                    "a", class_=html_classes["player_name"]
                )
                player_name_span = player_name_pic.find(
                    "span", class_=html_classes["player_name"]
                )
                if player_name_link:
                    player_name = player_name_link.text.strip()
                elif player_name_span:
                    player_name = player_name_span.text.strip()
                else:
                    player_name = "Unknown"
                player_image_tag = player_name_pic.find("img")
                if player_image_tag:
                    image_url = player_image_tag["src"]
                    image_url = image_url.replace(
                        "/t_lazy/", "/"
                    )  # remove blur from image
                else:
                    image_url = None
                jersey_number_text = cells[1].text.strip()
                jersey_number = int(jersey_number_text) if jersey_number_text else None
                position = cells[2].text.strip()
                height = cells[4].text.strip()
                weight = cells[5].text.strip()
                experience = cells[6].text.strip()
                college = cells[7].text.strip()

                # print(player_name)
                nfl_roster_names.append(player_name)

                if player_name not in db_roster_names:
                    # either he's had his name changed or he's new to the team (coming from another team or new to the database entirely)
                    player = Player(
                        player_name=player_name,
                        team_id=team_id,
                        team=team_obj,
                        position=position,
                        jersey_number=jersey_number,
                        image_url=image_url,
                        height=height,
                        weight=weight,
                        experience=experience,
                        college=college,
                    )

                    existing_player = Player.query.filter_by(
                        player_name=player_name
                    ).first()
                    if existing_player is None:
                        # lets handle players with new names here.
                        # have it return tuple with the player's old name so it can be removed from db_player_names
                        updated_player = update_player_name_if_match(
                            player, db_team_players
                        )
                        print(player.player_name + " is not in the db")
                        print(updated_player)
                        if updated_player is not None:
                            players_with_updated_names.append(updated_player)
                        else:
                            players_new_to_db.append(player)
                    else:
                        players_with_new_teams.append(player)

            print("Db roster names")
            print(db_roster_names)
            print("nfl roster names")
            print(nfl_roster_names)

            departed_players_names = list(set(db_roster_names) - set(nfl_roster_names))
            print(team_obj.full_name + " departed players")
            print(departed_players_names)
            departed_team_players = [
                player
                for player in db_team_players
                if player.player_name in departed_players_names
            ]

            if departed_team_players:
                departed_players.extend(departed_team_players)
                # print("Departed players:")
                # print(departed_players)

        else:
            print(
                f"Failed to retrieve data from {url}. Status code: {response.status_code}"
            )

    # identify inactive players - players who left one team and did not join another
    inactive_players = [
        player for player in departed_players if player not in players_with_new_teams
    ]

    # todo: fix changed name inactive bug case

    print("Players new to db:")
    print([player.player_name for player in players_new_to_db])

    print("\nPlayers with updated names:")
    print([player.player_name for player in players_with_updated_names])

    print("\nPlayers with new teams:")
    print([player.player_name for player in players_with_new_teams])

    print("\nDeparted players:")
    print([player.player_name for player in departed_players])

    print("\nInactive players:")
    print([player.player_name for player in inactive_players])

    # process the moves - make database changes
    # db.session.add_all(players_to_add)

    # # update the team_id field for players who changed teams
    # for player in players_to_update:
    #     existing_player = Player.query.get(player.id)

    #     if existing_player:
    #         existing_player.team_id = player.team_id
    #         # if existing_player.player_name != player.player_name:
    #         # existing_player.player_name = player.player_name

    # # set active field to 0 for inactive players
    # for player in inactive_players:
    #     existing_player = Player.query.get(player.id)
    #     if existing_player:
    #         existing_player.active = 0

    # db.session.commit()  # Commit once after adding all players
    # print(f"Successfully updated rosters ✅")
    # print report of moves

except Exception as e:
    print(f"Error updating rosters: {str(e)}")
