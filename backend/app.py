import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv

load_dotenv()

# creating a Flask app
app = Flask(__name__)
CORS(app)

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# dialect+driver://username:password@host:port/database
DB_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    team_name = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(3), nullable=False)
    conference = db.Column(db.String(3), nullable=False)
    division = db.Column(db.String(10), nullable=False)
    bye = db.Column(db.Integer, nullable=False)
    primary_color = db.Column(db.String(7), nullable=False)
    secondary_color = db.Column(db.String(7), nullable=False)
    tertiary_color = db.Column(db.String(7), nullable=True)

    # relationships
    players = relationship('Player', back_populates='team')
    home_games = relationship('Game', foreign_keys='Game.home_team_abbreviation', back_populates='home_team')
    away_games = relationship('Game', foreign_keys='Game.away_team_abbreviation', back_populates='away_team')

    def __repr__(self):
        return f'<Team {self.abbreviation}>'
    
class Player(db.Model):
    __tablename__ = 'players'
    player_id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(100), nullable=False)
    team_abbreviation = db.Column(db.String(3), db.ForeignKey('teams.abbreviation'), nullable=False)
    position = db.Column(db.String(3), nullable=False)
    jersey_number = db.Column(db.Integer, nullable=True)
    image_url = db.Column(db.String(100), nullable=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.String(2), nullable=False)
    college = db.Column(db.String(100), nullable=False)

    # relationships
    team = relationship('Team', back_populates='players')

    passing_game_logs = relationship('PassingGameLog', back_populates='player')
    rushing_game_logs = relationship('RushingGameLog', back_populates='player')
    receiving_game_logs = relationship('ReceivingGameLog', back_populates='player')

    def __repr__(self):
        return f'<Team {self.player_name}>'

class Game(db.Model):
    __tablename__ = 'games'
    game_id = db.Column(db.Integer, primary_key=True)
    home_team_abbreviation = db.Column(db.String(3), db.ForeignKey('teams.abbreviation'), nullable=False)
    away_team_abbreviation = db.Column(db.String(3), db.ForeignKey('teams.abbreviation'), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    week = db.Column(db.Integer, nullable=False)
    box_score_url = db.Column(db.String(100), nullable=False)

    # relationships
    home_team = relationship('Team', foreign_keys=[home_team_abbreviation], back_populates='home_games')
    away_team = relationship('Team', foreign_keys=[away_team_abbreviation], back_populates='away_games')

    passing_game_logs = relationship('PassingGameLog', back_populates='game')
    rushing_game_logs = relationship('RushingGameLog', back_populates='game')
    receiving_game_logs = relationship('ReceivingGameLog', back_populates='game')

    def __repr__(self):
        return f'<Game {self.home_team_abbreviation} {self.away_team_abbreviation}>'
    
class PassingGameLog(db.Model):
    __tablename__ = 'passing_game_logs'
    passing_log_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    player_name = db.Column(db.String(100), db.ForeignKey('players.player_name'), nullable=False)
    completions = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, nullable=False)
    yards = db.Column(db.Integer, nullable=False)
    touchdowns = db.Column(db.Integer, nullable=False)
    interceptions = db.Column(db.Integer, nullable=False)
    fantasy_points = db.Column(db.Integer, nullable=False)

    # relationships
    game = relationship('Game', back_populates='passing_game_logs')
    player = relationship('Player', back_populates='passing_game_logs')

class RushingGameLog(db.Model):
    __tablename__ = 'rushing_game_logs'
    rushing_log_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    player_name = db.Column(db.String(100), db.ForeignKey('players.player_name'), nullable=False)
    carries = db.Column(db.Integer, nullable=False)
    yards = db.Column(db.Integer, nullable=False)
    touchdowns = db.Column(db.Integer, nullable=False)
    fantasy_points = db.Column(db.Integer, nullable=False)

    # relationships
    game = relationship('Game', back_populates='rushing_game_logs')
    player = relationship('Player', back_populates='rushing_game_logs')

class ReceivingGameLog(db.Model):
    __tablename__ = 'receiving_game_logs'
    receiving_log_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    player_name = db.Column(db.String(100), db.ForeignKey('players.player_name'), nullable=False)
    targets = db.Column(db.Integer, nullable=False)
    receptions = db.Column(db.Integer, nullable=False)
    yards = db.Column(db.Integer, nullable=False)
    touchdowns = db.Column(db.Integer, nullable=False)
    fantasy_points = db.Column(db.Integer, nullable=False)

    # relationships
    game = relationship('Game', back_populates='receiving_game_logs')
    player = relationship('Player', back_populates='receiving_game_logs')

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"
        return jsonify({'data': data})
    
@app.route('/api/roster/<team_abbreviation>', methods=['GET'])
def get_team_roster(team_abbreviation):
    
    team_players = Player.query.filter_by(team_abbreviation=team_abbreviation).all()

    # Convert the player objects to a list of dictionaries
    player_list = []
    for player in team_players:
        player_list.append({
            'player_id': player.player_id,
            'player_name': player.player_name,
            'team_abbreviation': player.team_abbreviation,
            'position': player.position,
            'jersey_number': player.jersey_number,
            'image_url': player.image_url,
            'height': player.height,
            'weight': player.weight,
            'experience': player.experience,
            'college': player.college
        })

    return jsonify(player_list)

@app.route('/api/player/<int:player_id>', methods=['GET'])
def get_player(player_id):
    
    player = Player.query.filter_by(player_id=player_id).first()

    if player:
        return jsonify({
            'player_id': player.player_id,
            'player_name': player.player_name,
            'team_abbreviation': player.team_abbreviation,
            'position': player.position,
            'jersey_number': player.jersey_number,
            'image_url': player.image_url,
            'height': player.height,
            'weight': player.weight,
            'experience': player.experience,
            'college': player.college
        })
    else:
        return jsonify({'message': 'Player not found'}, 404)
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)