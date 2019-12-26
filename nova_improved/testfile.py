import json
from pprint import pprint

def read():
    #Opens file in json format or dict idk
    with open("inventory.json", "r") as read_file:
        data = json.load(read_file)

    for x in range(len(data["firework"])):
        if data["firework"][x]["type"] == "Rakett":
            print data["firework"][x]["name"]

    # for x in range(len(data["firework"])):
    #     print data["firework"][x]["name"]
    #     print data["firework"][x]["price"]
    #     print data["firework"][x]["inventory"]
    #     print data["firework"][x]["type"]
    #     print "\n"

def write(name, type_change, amount):
    with open("inventory.json", "r") as read_file:
        data = json.load(read_file)

    for x in range(len(data["firework"])):
        if data["firework"][x]["name"] == name:
            print data["firework"][x]["name"]
            tmp = data["firework"][x][type_change]
            data["firework"][x][type_change] = amount
    #tmp = data["firework"][1]["inventory"]
    #data["firework"][1]["inventory"] = "100"

    with open("inventory.json", "w") as jsonFile:
        json.dump(data, jsonFile)

#read()
write("Commando", "inventory", "666")