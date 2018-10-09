import json
filename = "files/usersettings.txt"
myFile = open(filename, mode="w")

player1 = {
    "name": "Donny",
    "score": 345,
    "wards": ["OR", "NV", "NY"]
}

player2 = {
    "name": "Hylly",
    "score": 355,
    "wards": ["TX", "IX", "MI"]
}

myPlayers = []
myPlayers.append(player1)
myPlayers.append(player2) 

json.dump(myPlayers, myFile)

myFile.close()

myFile = open(filename, mode="r")
json_data = json.load(myFile)

for user in json_data:
    print("Player name is " + str(user["name"]))
    print("Player score is " + str(user["score"]))
    print("Player awards: " + str(user["wards"]))
    print("\n----------------\n")