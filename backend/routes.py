from flask import jsonify, request

# from app import app
from models import Game, Team, Player, PassingGameLog, RushingGameLog, ReceivingGameLog


# @app.route("/", methods=["GET", "POST"])
def hello_world():
    data = "hello world"
    return jsonify({"data": data})


# @app.route("/api/roster/<team_abbreviation>", methods=["GET"])
def get_team_roster(team_abbreviation):
    # get team's id from the abbreviation
    team = Team.query.filter_by(abbreviation=team_abbreviation).first()
    team_id = team.team_id

    team_players = Player.query.filter_by(team_id=team_id).all()

    # Convert the player objects to a list of dictionaries
    results = []
    for player in team_players:
        results.append(
            {
                "player_id": player.player_id,
                "player_name": player.player_name,
                "team_id": player.team_id,
                "position": player.position,
                "jersey_number": player.jersey_number,
                "image_url": player.image_url,
                "height": player.height,
                "weight": player.weight,
                "experience": player.experience,
                "college": player.college,
            }
        )

    return jsonify(results)


# @app.route("/api/player/<int:player_id>", methods=["GET"])
def get_player(player_id):
    player = Player.query.filter_by(player_id=player_id).first()

    if player:
        return jsonify(
            {
                "player_id": player.player_id,
                "player_name": player.player_name,
                "team_id": player.team_id,
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
    results = []
    for game in games:
        results.append(
            {
                "game_id": game.game_id,
                "home_team_id": game.home_team_id,
                "away_team_id": game.away_team_id,
                "home_team_abbreviation": game.home_team.abbreviation,
                "away_team_abbreviation": game.away_team.abbreviation,
                "season": game.season,
                "week": game.week,
                "box_score_url": game.box_score_url,
            }
        )

    return jsonify(results)


def get_player_game_logs(player_id):
    player = Player.query.filter_by(player_id=player_id).first()

    if player:
        results = []
        position = player.position
        if position == "QB":
            passing_logs = PassingGameLog.query.filter_by(player_id=player_id).all()
            for log in passing_logs:
                results.append(
                    {
                        "passing_log_id": log.passing_log_id,
                        "game_id": log.game_id,
                        "player_id": log.player_id,
                        "completions": log.completions,
                        "attempts": log.attempts,
                        "yards": log.yards,
                        "touchdowns": log.touchdowns,
                        "interceptions": log.interceptions,
                        "fantasy_points": log.fantasy_points,
                    }
                )
            return results
        elif position == "RB":
            rushing_logs = RushingGameLog.query.filter_by(player_id=player_id).all()
            for log in rushing_logs:
                results.append(
                    {
                        "rushing_log_id": log.rushing_log_id,
                        "game_id": log.game_id,
                        "player_id": log.player_id,
                        "carries": log.carries,
                        "yards": log.yards,
                        "touchdowns": log.touchdowns,
                        "fantasy_points": log.fantasy_points,
                    }
                )
            return results
        elif position == "WR":
            receiving_logs = ReceivingGameLog.query.filter_by(player_id=player_id).all()
            for log in receiving_logs:
                results.append(
                    {
                        "receiving_log_id": log.receiving_log_id,
                        "game_id": log.game_id,
                        "player_id": log.player_id,
                        "targets": log.targets,
                        "receptions": log.receptions,
                        "yards": log.yards,
                        "touchdowns": log.touchdowns,
                        "fantasy_points": log.fantasy_points,
                    }
                )
            return results
        else:
            return jsonify({"message": "Invalid player position"}, 400)

    else:
        return jsonify({"message": "Player not found"}, 404)


# @app.route("/api/game/logs/<int:game_id>", methods=["GET"])
def get_game_logs(game_id):
    game = Game.query.filter_by(game_id=game_id).first()
    passing_logs = PassingGameLog.query.filter_by(game_id=game_id).all()
    rushing_logs = RushingGameLog.query.filter_by(game_id=game_id).all()
    receiving_logs = ReceivingGameLog.query.filter_by(game_id=game_id).all()

    passing_logs_list = []
    rushing_logs_list = []
    receiving_logs_list = []
    result = {}

    # for log in passing_logs:

    # what you want the result to look like
    result = {
        "passing": [
            # info of a passing game log but with the players name
            {}
        ],
        "rushing": [],
        "receiving": [],
    }

    return jsonify(passing_logs_list)
