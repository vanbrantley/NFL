from app import app, db
from models import Team, Player
import requests
from bs4 import BeautifulSoup

app.app_context().push()

try:
    nfl_teams = {
        "buffalo-bills": "BUF",
        "miami-dolphins": "MIA",
        "new-england-patriots": "NE",
        "new-york-jets": "NYJ",
        "baltimore-ravens": "BAL",
        "cincinnati-bengals": "CIN",
        "cleveland-browns": "CLE",
        "pittsburgh-steelers": "PIT",
        "houston-texans": "HOU",
        "indianapolis-colts": "IND",
        "jacksonville-jaguars": "JAC",
        "tennessee-titans": "TEN",
        "denver-broncos": "DEN",
        "kansas-city-chiefs": "KC",
        "los-angeles-chargers": "LAC",
        "las-vegas-raiders": "LV",
        "dallas-cowboys": "DAL",
        "new-york-giants": "NYG",
        "philadelphia-eagles": "PHI",
        "washington-commanders": "WAS",
        "chicago-bears": "CHI",
        "detroit-lions": "DET",
        "green-bay-packers": "GB",
        "minnesota-vikings": "MIN",
        "atlanta-falcons": "ATL",
        "carolina-panthers": "CAR",
        "new-orleans-saints": "NO",
        "tampa-bay-buccaneers": "TB",
        "arizona-cardinals": "ARI",
        "los-angeles-rams": "LAR",
        "san-francisco-49ers": "SF",
        "seattle-seahawks": "SEA",
    }

    html_classes = {
        "players-table": "d3-o-table",
        "player_name": "nfl-o-roster__player-name",
    }

    # loop through team dictionary items
    for team, abbreviation in nfl_teams.items():
        print(f"Adding players for Team: {abbreviation}")

        team_obj = Team.query.filter_by(abbreviation=abbreviation).first()
        if team_obj is None:
            error_message = (
                f"Team with abbreviation {abbreviation} not found in the database."
            )
            raise ValueError(error_message)

        team_id = team_obj.team_id

        # Construct the URL for the team's roster page
        url = f"https://www.nfl.com/teams/{team}/roster"

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            players_table = soup.find("table", class_=html_classes["players-table"])
            if players_table is None:
                error_message = "Players table not found. Check the web page structure."
                raise ValueError(error_message)

            players = []

            rows = players_table.find_all("tr")
            if rows is None:
                error_message = "Players rows not found. Check the web page structure."
                raise ValueError(error_message)

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
                status = cells[3].text.strip()
                height = cells[4].text.strip()
                weight = cells[5].text.strip()
                experience = cells[6].text.strip()
                college = cells[7].text.strip()

                # prints to help with debugging
                # print("Name: ", player_name)
                # print("Team: ", team)
                # print("Position: ", position)
                # print("#: ", jersey_number)
                # print("Image URL: ", image_url)
                # print("Height: ", height)
                # print("Weight: ", weight)
                # print("Experience: ", experience)
                # print("College: ", college)

                accepted_positions = ["QB", "RB", "WR", "TE"]
                accepted_statuses = ["ACT", "RES", "RSR", "RSN"]

                if status in accepted_statuses and position in accepted_positions:
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
                        active=1,
                    )

                    players.append(player)

            # print([player.player_name for player in players])
            db.session.add_all(players)
            db.session.commit()  # Commit once after adding all players
            print(f"Successfully added players for Team: {abbreviation} ✅")

        else:
            print(
                f"Failed to retrieve data from {url}. Status code: {response.status_code}"
            )

except Exception as e:
    print(f"Error inserting data: {str(e)}")
