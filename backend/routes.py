from flask import jsonify, request
from sqlalchemy import func, desc

# from app import app
from models import (
    db,
    Game,
    Team,
    Player,
    PassingGameLog,
    RushingGameLog,
    ReceivingGameLog,
)


# "/"
def hello_world():
    data = "hello world"
    return jsonify({"data": data})


# "/api/team/details/<team_abbreviation>"
def get_team_details(team_abbreviation):
    team = Team.query.filter_by(abbreviation=team_abbreviation).first()

    if team:
        return jsonify(
            {
                "team_id": team.team_id,
                "city": team.city,
                "team_name": team.team_name,
                "full_name": team.full_name,
                "abbreviation": team.abbreviation,
                "conference": team.conference,
                "division": team.division,
                "bye": team.bye,
                "primary_color": team.primary_color,
                "secondary_color": team.secondary_color,
                "teriary_color": team.tertiary_color,
            }
        )
    else:
        return jsonify({"message": "Team not found"}, 404)


# "/api/team/roster/<team_abbreviation>"
def get_team_roster(team_abbreviation):
    team = Team.query.filter_by(abbreviation=team_abbreviation).first()
    team_id = team.team_id

    team_players = Player.query.filter_by(team_id=team_id).all()

    # Convert the player objects to a list of dictionaries
    results = []
    for player in team_players:
        offensive_positions = ["QB", "RB", "WR", "TE", "K"]
        player_position = player.position

        if player_position in offensive_positions:
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


# "/api/player/<player_id>"
def get_player(player_id):
    player = Player.query.filter_by(player_id=player_id).first()

    if player:
        return jsonify(
            {
                "player_id": player.player_id,
                "player_name": player.player_name,
                "team_id": player.team_id,
                "team_abbreviation": player.team.abbreviation,
                "team_full_name": player.team.full_name,
                "team_primary_color": player.team.primary_color,
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


# "/api/games"
def get_games():
    games = Game.query.all()
    results = []
    for game in games:
        # home_team = Team.query.filter_by(team_id=game.home_team_id)
        # away_team = Team.query.filter_by(team_id=game.away_team_id)

        # home_team_name = home_team.full_name
        # home_team_abbreviation = home_team.abbreviation
        # home_team_primary_color = home_team.primary_color
        # home_team_secondary_color = home_team.secondary_color
        # home_team_tertiary_color = home_team.tertiary_color

        # away_team_name = away_team.full_name
        # away_team_abbreviation = away_team.abbreviation
        # away_team_primary_color = away_team.primary_color
        # away_team_secondary_color = away_team.secondary_color
        # away_team_tertiary_color = away_team.tertiary_color

        results.append(
            {
                "game_id": game.game_id,
                "home_team_id": game.home_team_id,
                "home_team_full_name": game.home_team.full_name,
                "home_team_abbreviation": game.home_team.abbreviation,
                "home_team_primary_color": game.home_team.primary_color,
                "home_team_secondary_color": game.home_team.secondary_color,
                "home_team_tertiary_color": game.home_team.tertiary_color,
                "away_team_id": game.away_team_id,
                "away_team_full_name": game.away_team.full_name,
                "away_team_abbreviation": game.away_team.abbreviation,
                "away_team_primary_color": game.away_team.primary_color,
                "away_team_secondary_color": game.away_team.secondary_color,
                "away_team_tertiary_color": game.away_team.tertiary_color,
                "season": game.season,
                "week": game.week,
                "box_score_url": game.box_score_url,
            }
        )

    return jsonify(results)


# "/api/player/logs/<player_id>"
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
                        "week": log.game.week,
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
                        "week": log.game.week,
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
                        "week": log.game.week,
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


# "/api/game/logs/<int:game_id>"
def get_game_logs(game_id):
    game = Game.query.filter_by(game_id=game_id).first()
    passing_logs = game.passing_game_logs
    rushing_logs = game.rushing_game_logs
    receiving_logs = game.receiving_game_logs

    passing_logs_list = []
    rushing_logs_list = []
    receiving_logs_list = []

    for log in passing_logs:
        passing_logs_list.append(
            {
                "passing_log_id": log.passing_log_id,
                "game_id": log.game_id,
                "week": log.game.week,
                "player_id": log.player_id,
                "player_name": log.player.player_name,
                "completions": log.completions,
                "attempts": log.attempts,
                "yards": log.yards,
                "touchdowns": log.touchdowns,
                "interceptions": log.interceptions,
                "fantasy_points": log.fantasy_points,
            }
        )

    for log in rushing_logs:
        rushing_logs_list.append(
            {
                "rushing_log_id": log.rushing_log_id,
                "game_id": log.game_id,
                "week": log.game.week,
                "player_id": log.player_id,
                "player_name": log.player.player_name,
                "carries": log.carries,
                "yards": log.yards,
                "touchdowns": log.touchdowns,
                "fantasy_points": log.fantasy_points,
            }
        )

    for log in receiving_logs:
        receiving_logs_list.append(
            {
                "receiving_log_id": log.receiving_log_id,
                "game_id": log.game_id,
                "week": log.game.week,
                "player_id": log.player_id,
                "player_name": log.player.player_name,
                "targets": log.targets,
                "receptions": log.receptions,
                "yards": log.yards,
                "touchdowns": log.touchdowns,
                "fantasy_points": log.fantasy_points,
            }
        )

    results = {
        "passing": passing_logs_list,
        "rushing": rushing_logs_list,
        "receiving": receiving_logs_list,
    }

    return jsonify(results)


# "/api/player/logs/filter"
def filter_player_logs():
    position = request.args.get("position")
    start_week = request.args.get("start_week")
    end_week = request.args.get("end_week")
    team = request.args.get("team")

    results = []

    # check arguments against null
    # handle join based on the position - All/QB/RB/WR/TE/FLEX

    if position == "QB":
        joined_table = (
            db.session.query(
                Player.player_id,
                Player.player_name,
                Player.image_url,
                func.sum(PassingGameLog.completions).label("total_completions"),
                func.sum(PassingGameLog.attempts).label("total_attempts"),
                func.sum(PassingGameLog.yards).label("total_yards"),
                func.sum(PassingGameLog.touchdowns).label("total_touchdowns"),
                func.sum(PassingGameLog.interceptions).label("total_interceptions"),
                func.sum(PassingGameLog.fantasy_points).label("total_fantasy_points"),
            )
            .join(PassingGameLog, Player.player_id == PassingGameLog.player_id)
            .join(Game, PassingGameLog.game_id == Game.game_id)
            .filter(Game.week >= start_week, Game.week <= end_week)
            .group_by(Player.player_id)
            .order_by(desc("total_fantasy_points"))
            .all()
        )

        for row in joined_table:
            results.append(
                {
                    "player_id": row.player_id,
                    "player_name": row.player_name,
                    "image_url": row.image_url,
                    "total_completions": row.total_completions,
                    "total_attempts": row.total_attempts,
                    "total_yards": row.total_yards,
                    "total_touchdowns": row.total_touchdowns,
                    "total_interceptions": row.total_interceptions,
                    "total_fantasy_points": row.total_fantasy_points,
                }
            )

    elif position == "WR":
        joined_table = (
            db.session.query(
                Player.player_id,
                Player.player_name,
                Player.image_url,
                func.sum(ReceivingGameLog.targets).label("total_targets"),
                func.sum(ReceivingGameLog.receptions).label("total_receptions"),
                func.sum(ReceivingGameLog.yards).label("total_yards"),
                func.sum(ReceivingGameLog.touchdowns).label("total_touchdowns"),
                func.sum(ReceivingGameLog.fantasy_points).label("total_fantasy_points"),
            )
            .join(ReceivingGameLog, Player.player_id == ReceivingGameLog.player_id)
            .join(Game, ReceivingGameLog.game_id == Game.game_id)
            .filter(
                Game.week >= start_week,
                Game.week <= end_week,
                Player.position != "QB",
                Player.position != "RB",
            )
            .group_by(Player.player_id)
            .order_by(desc("total_fantasy_points"))
            .all()
        )

        for row in joined_table:
            results.append(
                {
                    "player_id": row.player_id,
                    "player_name": row.player_name,
                    "image_url": row.image_url,
                    "total_targets": row.total_targets,
                    "total_receptions": row.total_receptions,
                    "total_yards": row.total_yards,
                    "total_touchdowns": row.total_touchdowns,
                    "total_fantasy_points": row.total_fantasy_points,
                }
            )

    elif position == "RB":
        joined_table = (
            db.session.query(
                Player.player_id,
                Player.player_name,
                Player.image_url,
                func.sum(RushingGameLog.carries).label("total_carries"),
                func.sum(RushingGameLog.yards).label("total_yards"),
                func.sum(RushingGameLog.touchdowns).label("total_touchdowns"),
                func.sum(RushingGameLog.fantasy_points).label("total_fantasy_points"),
            )
            .join(RushingGameLog, Player.player_id == RushingGameLog.player_id)
            .join(Game, RushingGameLog.game_id == Game.game_id)
            .filter(
                Game.week >= start_week,
                Game.week <= end_week,
                Player.position != "QB",
                Player.position != "WR",
            )
            .group_by(Player.player_id)
            .order_by(desc("total_fantasy_points"))
            .all()
        )

        for row in joined_table:
            results.append(
                {
                    "player_id": row.player_id,
                    "player_name": row.player_name,
                    "image_url": row.image_url,
                    "total_carries": row.total_carries,
                    "total_yards": row.total_yards,
                    "total_touchdowns": row.total_touchdowns,
                    "total_fantasy_points": row.total_fantasy_points,
                }
            )

    else:
        return jsonify({"message": "Invalid player position"}, 400)

    return jsonify(results)
