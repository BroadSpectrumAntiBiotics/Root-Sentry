import time
from assetControl import load_ascii_art
from stages import stagedGame
from shop import shopping
from information import info

def UI(name, hp, scripts, budget, update):
    hp = (hp//10)*"|"
    update = str((update//10)) + "." + str(update)[-1]
    art = load_ascii_art("ui", "basicUI.txt")
    
    art = art.replace("PingOfDeath.sh   x1 ", "autoCheck.exe    x" + f"{str(scripts.count("autoCheck.exe")):2}")
    art = art.replace("Trojan_Horse.exe x2 ", "average_av.exe   x" + f"{str(scripts.count("average_av.exe")):2}")
    art = art.replace("Port_Scanner.py  x3 ", "advanced_av.exe  x" + f"{str(scripts.count("advanced_av.exe")):2}")
    
    art = art.replace("NEON_KNIGHT_777", f"{name:15}")
    art = art.replace("8450", f"{budget:04d}")
    art = art.replace("||||||||||", f"{hp:10}")
    art = art.replace("4.2", f"{update:3}")
    print(art)


def doing(do, player, budget):
    if do == "continue":
        return stagedGame(player)
    if do == "shop":
        return shopping(budget, player)
    if do == "info":
        return info()
    else:
        print("Wrong command type. Please try again.")
        time.sleep(1)