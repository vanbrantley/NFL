import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
from models import db
from routes import *

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
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.add_url_rule("/", view_func=hello_world)
app.add_url_rule("/api/roster/<team_abbreviation>", view_func=get_team_roster)
app.add_url_rule("/api/player/<player_id>", view_func=get_player)
app.add_url_rule("/api/games", view_func=get_games)
app.add_url_rule("/api/game/logs/<game_id>", view_func=get_game_logs)
app.add_url_rule("/api/player/logs/<player_id>", view_func=get_player_game_logs)

if __name__ == "__main__":
    app.run(debug=True)
