-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

\c tournament;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Matches;

CREATE TABLE Players(id serial primary key, 
                     name text);

CREATE TABLE Matches(id serial primary key,
                     winner INTEGER REFERENCES Players(id),
                     loser INTEGER REFERENCES Players(id));
					 
CREATE VIEW Player_Wins AS
            select Players.id, Players.name, count(Matches.winner) AS wins
            from Players left join Matches
            on Players.id = Matches.winner
            Group By Players.id;
			
CREATE VIEW Player_Losses AS
            select Players.id, Players.name, count(Matches.loser) AS losses
            from Players left join Matches
            on Players.id = Matches.loser
            Group By Players.id;			
	
CREATE VIEW Player_Matches AS
            select Players.id, Players.name, count(Matches.id) AS Matches_Played
            from Players left join Matches
            on Players.id = Matches.winner or Players.id = Matches.loser
            Group By Players.id; 



