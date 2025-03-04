# Tuple
teams = ('TeamA', 'TeamB')

# Dictionary
basketball_player = {'name': 'LeBron James', 'team': 'Los Angeles Lakers'}

# Set
soccer_positions = {'Forward', 'Midfielder', 'Defender', 'Goalkeeper'}

# List of player dictionaries
players = [
    {'name': 'Patrick Mahomes', 'position': 'QB', 'jersey_number': 15, 'yards': 4300, 'touchdowns': 35},
    {'name': 'Travis Kelce', 'position': 'TE', 'jersey_number': 87, 'yards': 1100, 'touchdowns': 8},
    {'name': 'Isiah Pacheco', 'position': 'RB', 'jersey_number': 10, 'yards': 920, 'touchdowns': 7},
    {'name': 'Chris Jones', 'position': 'DT', 'jersey_number': 95, 'yards': 0, 'touchdowns': 0},
    {'name': 'L’Jarius Sneed', 'position': 'CB', 'jersey_number': 38, 'yards': 0, 'touchdowns': 0},
]
positions = {player['position'] for player in players}
# Updating stats for Isiah Pacheco
for player in players:
    if player['jersey_number'] == 10:
        player['yards'] += 80
        player['touchdowns'] += 2
        break
# Calculate average yards and touchdowns
total_yards = sum(player['yards'] for player in players)
total_touchdowns = sum(player['touchdowns'] for player in players)

average_yards = total_yards / len(players)
average_touchdowns = total_touchdowns / len(players)

print(f"Average Yards: {average_yards:.2f}")
print(f"Average Touchdowns: {average_touchdowns:.2f}")
print(f' The positions are {positions}')
for player in players:
    print(f"{player['name']} - Position: {player['position']}, Jersey: {player['jersey_number']},"
          f" Yards: {player['yards']}, Touchdowns: {player['touchdowns']}")


