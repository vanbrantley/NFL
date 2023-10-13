-- Switch to the 'nfl' database to ensure tables are deleted from correct database
USE nfl;

-- Drop tables in reverse order (tables with foreign keys first)
DROP TABLE IF EXISTS fantasy_rosters;
DROP TABLE IF EXISTS fantasy_teams;
DROP TABLE IF EXISTS receiving_game_logs;
DROP TABLE IF EXISTS rushing_game_logs;
DROP TABLE IF EXISTS passing_game_logs;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS users;

-- Drop the 'nfl' database
DROP DATABASE IF EXISTS nfl;