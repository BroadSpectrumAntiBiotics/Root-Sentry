import time

from stages import stagedGame
from shop import shopping
from information import info

def UI(name, hp, scripts, budget):
    print("=" * 30)
    print(f"User: {name}")
    print(f"System Integrity: {hp}\nBudget: {budget}")
    print(f"Scripts: {scripts}")
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