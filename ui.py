import time

from stages import stagedGame
from shop import shopping
from information import info

def UI(name, hp, scripts, budget, update):
    print("=" * 30)
    print(f"User: {name}")
    print(f"System Integrity: {hp}\nBudget: {budget}")
    print(f"Scripts: {f"{scripts.count("autoCheck.exe")} 'autoCheck.exe'"}, {f"{scripts.count("average_av.exe")} 'average_av.exe'"}, {f"{scripts.count("advanced_av.exe")} 'advanced_av.exe'"}")
    print("Update level: " + (update//10)*"⬤" + (10-(update//10))*"◯")
    print("=" * 30)


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