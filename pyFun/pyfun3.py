# Make a list of 5 dictionaries with each dictionary being a NFL Player. 
# Each NFL Player needs a name, team, position, division, city
# Create a function that views the specified players
# Create a function that adds a player to the list

# Arrays | .append() | .pop()

def viewPlayerStats(playerName):
    """
        what do you have: playername
        what are you looking for: stats of the player
        where will you look for it: nflPlayers
        looking for player name in nflPlayers

        you will go into nfl player and look at each player
        you will compare that players name to what player you are searching for

        a for loop will start at 0 and end at the last player
    """

    stats = None
    for i in range(0, len(nflPlayers)):
        currentPlayer = nflPlayers[i]

           # Chase Young == nflPlayers[i]['name]
        if playerName == currentPlayer['name']:
            stats = currentPlayer
            break
    
    return stats

def addPlayers():
    pass

def deletePlayers():
    pass

if __name__ == "__main__":
    # Define Players

    nflPlayers = [
        {'name': 'Patrick Mahomes', 'team': 'Chiefs', 'position': 'Quarterback', 'division': 'AFC North', 'city': 'Kansas City'},
        {'name': 'Chase Young', 'team': 'Redskins', 'position': 'Defensive End', 'division': 'NFC West', 'city': 'Washington'},
        {'name': 'Derrick Henry', 'team': 'Titans', 'position': 'Runningback', 'division': 'AFC West', 'city': 'Tennessee'},
        {'name': 'Aaron Donald', 'team': 'Rams', 'position': 'Defensive End', 'division': 'NFC East', 'city': 'Los Angeles'},
        {'name': 'Julio Jones', 'team': 'Falcons', 'position': 'Wide Receiver', 'division': 'NFC South', 'city': 'Atlanta'}
    ]
    
    print(nflPlayers[4]['team'])

    names = ['Patrick Mahomes', 'Chase Young', 'Derrick Henry', 'Aaron Donald', 'Julio Jones']
    print(names[1])

    player = {'name': 'Matt Ryan', 'team': 'Falcons', 'city': 'Atlanta'}
    print(player['team'])

    # Write code to call the functions and display remaining players

    stats = viewPlayerStats('Chase Young')
    print(stats)