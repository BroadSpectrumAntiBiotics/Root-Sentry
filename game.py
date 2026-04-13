from player import Player
import virusCreator
from stages import Stages
import usefulFeatures
from introduction import intro
from ui import UI, doing




def gameF():
    usefulFeatures.clear_screen()
    name = input("Enter your name: ")
    player = Player(name)
    intro(player.name)
    

    while True:
        usefulFeatures.clear_screen()
        UI(player.name, player.hp, player.scripts, player.budget)
        do = input("""
Type:
                                "continue" for resuming update,
                                "shop" for viewing shop,
                                "info" for general info,
                                "exit" for... obviously.
                   
>>>""")
        if do == "exit":
            break
        doing(do, player)
        



if __name__ == "__main__":
    gameF()

