-- Create a new database if it doesn't exist
CREATE DATABASE IF NOT EXISTS nfl;

-- Use the newly created database
USE nfl;

-- Create tables

CREATE TABLE users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE teams(
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    team_name VARCHAR(50) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    abbreviation VARCHAR(3) NOT NULL,
    conference VARCHAR(3) NOT NULL,
    division VARCHAR(10) NOT NULL,
    bye INT NOT NULL,
    primary_color VARCHAR(7) NOT NULL,
    secondary_color VARCHAR(7) NOT NULL,
    tertiary_color VARCHAR(7) NULL
);

CREATE TABLE players(
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    team_id INT REFERENCES teams(team_id),
    position VARCHAR(3) NOT NULL,
    jersey_number INT NULL,
    image_url VARCHAR(100) NULL,
    height INT NOT NULL,
    weight INT NOT NULL,
    experience VARCHAR(2) NOT NULL,
    college VARCHAR(100) NOT NULL,
    active TINYINT(1) NOT NULL
);

CREATE TABLE games(
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    home_team_id INT REFERENCES team(team_id),
    away_team_id INT REFERENCES team(team_id),
    season INT NOT NULL,
    week INT NOT NULL,
    box_score_url VARCHAR(100) NOT NULL,
    home_team_score INT NULL,
    away_team_score INT NULL
);

CREATE TABLE passing_game_logs(
    passing_log_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT REFERENCES games(game_id),
    player_id INT REFERENCES players(player_id),
    team_id INT REFERENCES team(team_id),
    completions INT NOT NULL,
    attempts INT NOT NULL,
    yards INT NOT NULL,
    touchdowns INT NOT NULL,
    interceptions INT NOT NULL,
    fantasy_points INT NOT NULL
);

CREATE TABLE rushing_game_logs(
    rushing_log_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT REFERENCES games(game_id),
    player_id INT REFERENCES players(player_id),
    team_id INT REFERENCES team(team_id),
    carries INT NOT NULL,
    yards INT NOT NULL,
    touchdowns INT NOT NULL,
    fantasy_points INT NOT NULL
);

CREATE TABLE receiving_game_logs(
    receiving_log_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT REFERENCES games(game_id),
    player_id INT REFERENCES players(player_id),
    team_id INT REFERENCES team(team_id),
    targets INT NOT NULL,
    receptions INT NOT NULL,
    yards INT NOT NULL,
    touchdowns INT NOT NULL,
    fantasy_points INT NOT NULL
);

CREATE TABLE fantasy_teams(
    fantasy_team_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    team_name VARCHAR(100) NOT NULL,
    season INT NOT NULL,
    logo_image_url VARCHAR(100) NULL
);

CREATE TABLE fantasy_rosters(
    fantasy_team_id INT REFERENCES fantasy_teams(fantasy_team_id),
    player_id INT REFERENCES players(player_id),
    PRIMARY KEY (fantasy_team_id, player_id)
);