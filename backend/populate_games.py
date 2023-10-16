from app import app, db, Game, Team
import requests
from bs4 import BeautifulSoup

# Create an application context
app.app_context().push()

REG_SEASON_WEEKS = 18
cbs_city_to_abbreviation = {
    "Buffalo": "BUF",
    "Miami": "MIA",
    "New England": "NE",
    "N.Y. Jets": "NYJ",
    "Baltimore": "BAL",
    "Cincinnati": "CIN",
    "Cleveland": "CLE",
    "Pittsburgh": "PIT",
    "Houston": "HOU",
    "Indianapolis": "IND",
    "Jacksonville": "JAC",
    "Tennessee": "TEN",
    "Denver": "DEN",
    "Kansas City": "KC",
    "L.A. Chargers": "LAC",
    "Las Vegas": "LV",
    "Dallas": "DAL",
    "N.Y. Giants": "NYG",
    "Philadelphia": "PHI",
    "Washington": "WAS",
    "Chicago": "CHI",
    "Detroit": "DET",
    "Green Bay": "GB",
    "Minnesota": "MIN",
    "Atlanta": "ATL",
    "Carolina": "CAR",
    "New Orleans": "NO",
    "Tampa Bay": "TB",
    "Arizona": "ARI",
    "L.A. Rams": "LAR",
    "San Francisco": "SF",
    "Seattle": "SEA"
}

month_to_number = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

html_classes = {
    "games_table": "TableBaseWrapper",
    "date_class": "TableBase-title",
    "table-rows": "TableBase-bodyTr",
    "team-name": "TeamName"
}

for week_number in range(1, REG_SEASON_WEEKS + 1):

    games = []

    
    print(f"Adding Week {week_number} games...")

    url = f"https://www.cbssports.com/nfl/schedule/2023/regular/{week_number}/"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        game_day_tables = soup.find_all('div', class_=html_classes["games_table"])
        if not game_day_tables:
            error_message = "Error: No game day tables found. Check the web page structure."
            raise ValueError(error_message)
        
        for table in game_day_tables:

            date_string = table.find('h4', class_=html_classes["date_class"]).text.strip()
            if date_string is None:
                error_message = "Error: Game date not found. Check the web page structure."
                raise ValueError(error_message)

            rows = table.find_all('tr', class_=html_classes["table-rows"])
            if rows is None:
                error_message = "Error: No game rows found. Check the web page structure."
                raise ValueError(error_message)

            for row in rows:
                cells = row.find_all('td')

                away_cell = cells[0]
                home_cell = cells[1]

                away_team_city = away_cell.find('span', class_=html_classes["team-name"]).text
                home_team_city = home_cell.find('span', class_=html_classes["team-name"]).text

                if away_team_city is None or home_team_city is None:
                    error_message = "Error: Team cities not found for game. Check the web page structure."
                    raise ValueError(error_message)

                # convert them to team names
                away_team_abbreviation = cbs_city_to_abbreviation[away_team_city]
                home_team_abbreviation = cbs_city_to_abbreviation[home_team_city]

                home_team_obj = Team.query.filter_by(abbreviation=home_team_abbreviation).first()
                away_team_obj = Team.query.filter_by(abbreviation=away_team_abbreviation).first()

                # constuct box_score_url
                parts = date_string.split()
                month = parts[1]
                month_number = month_to_number[month]
                day_number = parts[2][:-1]
                if int(day_number) < 10:
                    day_number = f"0{day_number}"
                year = parts[3]

                # https://www.cbssports.com/nfl/gametracker/boxscore/NFL_20230907_DET@KC/
                box_score_url = f"https://www.cbssports.com/nfl/gametracker/boxscore/NFL_{year}{month_number}{day_number}_{away_team_abbreviation}@{home_team_abbreviation}"

                # make a game object
                game = Game(
                    home_team_abbreviation=home_team_abbreviation,
                    away_team_abbreviation=away_team_abbreviation,
                    season=2023,
                    week=week_number,
                    box_score_url=box_score_url,
                    home_team=home_team_obj,
                    away_team=away_team_obj
                )

                games.append(game)

        db.session.add_all(games)
        db.session.commit()
        print(f"Successfully added Week: {week_number} games ✅")


    else:
        print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")