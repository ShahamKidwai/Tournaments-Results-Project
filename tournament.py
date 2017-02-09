#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Matches")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Players")
    conn.commit()
    conn.close()
    

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT (*) FROM Players;")
    rows = c.fetchone()
    player_count = rows[0]
    conn.commit()
    conn.close()
    return player_count

def registerPlayer(name):
    """Adds a player to the tournament database.
     
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Players(name) VALUES (%s)",(name,))
    conn.commit()
    conn.close()

def playerStandings():
   """
    Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    
   conn = connect()
   c = conn.cursor()
   c.execute("select Player_Wins.id, Player_Wins.name, Player_Wins.wins, Player_Matches.Matches_Played from Player_Wins join Player_Matches on Player_Wins.id = Player_Matches.id  Order By Player_Wins.wins desc;")
   rows = c.fetchall()
   conn.close()
   return rows
   

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Matches(winner, loser) VALUES(%s, %s)",(winner, loser,))
    conn.commit()
    conn.close()


def swissPairings():
   """
    Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
   players = playerStandings()
   r1 = []
   r2 = []
   r3 = []
   i = 0
   while i < len(players):
        r1.append(players[i])
        i += 2
   j = 1
   while j < len(players):
        r2.append(players[j])
        j += 2
   for (p1,p2) in zip(r1, r2):
      r3.append((p1[0], p1[1], p2[0], p2[1]))
   return r3
  
   

