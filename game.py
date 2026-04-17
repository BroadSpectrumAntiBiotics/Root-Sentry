from player import Player
import virusCreator
from stages import Stages
import usefulFeatures
from introduction import intro
from ui import UI, doing
from end import ending, bad_ending
from dataMan import data
import json




def gameF():
    with open("data.json", "r") as file:
        data = json.load(file)
    usefulFeatures.clear_screen()
    if data["name"] == "":
        name = input("Enter your name: ")
        data["name"] = name
        usefulFeatures.clear_screen()
        intro(name)
    player = Player(data["name"], data["hp"], data["scripts"], data["budget"], data["update"])
    
    while True:
        usefulFeatures.clear_screen()
        if player.update > 100:
            ending(player)
            break
        if player.hp <= 0:
            bad_ending()
            break
        UI(player.name, player.hp, player.scripts, player.budget, player.update)
        data["budget"] = player.budget
        data["scripts"] = player.scripts
        data["hp"] = player.hp
        data["update"] = player.update
        do = input("""
Type:
                   
"continue" for resuming update,
"shop" for viewing shop,
"info" for general info,
"exit" for... obviously.
                   
>>>""")
        if do == "exit":
            with open("data.json", "w") as file:
                json.dump(data, file)
            break
        doing(do, player, player.budget)
        



if __name__ == "__main__":
    gameF()

