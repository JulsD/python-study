player = {
    'name': 'Grigoriy',
    'health': 100,
    'loc_x': 45,
    'loc_y': 30,
    'color': 'green',
    'awards': ['For courage', 'For sense of humour']
}

print(player)
print('Location X: ' + str(player['loc_x']))
print('player name is ' + player['name'])

player['age'] = 20
print(player)

del player['age']
print(player)

player['loc_x'] = player['loc_x'] + 10
player['loc_y'] = player['loc_y'] - 5
player['health'] = player['health'] - 25
if player['health'] < 80:
    player['color'] = 'yellow'

print(player)
print('=======================')

print(player.keys())
print(player.values())

all_players = []
for x in range(0, 3):
    all_players.append(player.copy())

all_players[2]['health'] = 6
all_players[1]['name'] = 'Mihal'
all_players[0]['loc_x']+= 10

for pl in all_players:
    print(pl)



