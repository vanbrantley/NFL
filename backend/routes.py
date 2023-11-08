from flask import jsonify, request

# from app import app
from models import Game, Player, PassingGameLog, RushingGameLog, ReceivingGameLog


# @app.route("/", methods=["GET", "POST"])
def hello_world():
    data = "hello world"
    return jsonify({"data": data})


# @app.route("/api/roster/<team_abbreviation>", methods=["GET"])
def get_team_roster(team_abbreviation):
    team_players = Player.query.filter_by(team_abbreviation=team_abbreviation).all()

    # Convert the player objects to a list of dictionaries
    player_list = []
    for player in team_players:
        player_list.append(
            {
                "player_id": player.player_id,
                "player_name": player.player_name,
                "team_abbreviation": player.team_abbreviation,
                "position": player.position,
                "jersey_number": player.jersey_number,
                "image_url": player.image_url,
                "height": player.height,
                "weight": player.weight,
                "experience": player.experience,
                "college": player.college,
            }
        )

    return jsonify(player_list)


# @app.route("/api/player/<int:player_id>", methods=["GET"])
def get_player(player_id):
    player = Player.query.filter_by(player_id=player_id).first()

    if player:
        return jsonify(
            {
                "player_id": player.player_id,
                "player_name": player.player_name,
                "team_abbreviation": player.team_abbreviation,
                "position": player.position,
                "jersey_number": player.jersey_number,
                "image_url": player.image_url,
                "height": player.height,
                "weight": player.weight,
                "experience": player.experience,
                "college": player.college,
            }
        )
    else:
        return jsonify({"message": "Player not found"}, 404)


# @app.route("/api/games", methods=["GET"])
def get_games():
    games = Game.query.all()
    game_list = []
    for game in games:
        game_list.append(
            {
                "game_id": game.game_id,
                "home_team_abbreviation": game.home_team_abbreviation,
                "away_team_abbreviation": game.away_team_abbreviation,
                "season": game.season,
                "week": game.week,
                "box_score_url": game.box_score_url,
            }
        )

    return jsonify(game_list)


# @app.route("/api/game/logs/<int:game_id>", methods=["GET"])
def get_game_logs(game_id):
    passing_logs = PassingGameLog.query.filter_by(game_id=game_id).all()
    rushing_logs = RushingGameLog.query.filter_by(game_id=game_id).all()
    receiving_logs = ReceivingGameLog.query.filter_by(game_id=game_id).all()

    passing_logs_list = []
    rushing_logs_list = []
    receiving_logs_list = []

    # for log in passing_logs:

    return jsonify(passing_logs_list)
