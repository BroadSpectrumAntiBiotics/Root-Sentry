from usefulFeatures import clear_screen, type_text
import random

script_names = ["autoCheck.exe", "average_av.exe", "advanced_av.exe"]
script_prices = [10, 20, 50]

script_list = f"""
{"Script name":^20}|{"Price":^10}
{"="*30}
{script_names[0]:^20}|{script_prices[0]:^8}
{script_names[1]:^20}|{script_prices[1]:^8}
{script_names[2]:^20}|{script_prices[2]:^8}
"""

 
def autoCheck(file, valid_files, corrupt_files):
    if file in valid_files:
        return type_text("\033[32mFile is valid.\033[0m")
    if file in corrupt_files:
        return type_text("\033[31mFile is corrupt.\033[0m")
    
def average_av(player):
    if ((100 - player.hp) <= 15):
        x = 100 - player.hp
        player.hp = 100
    else: 
        x = random.randint(10, 15)
        player.hp += x
    type_text(f"\033[32mRestored {x} system integrity.\033[0m")
    return player.hp

def advanced_av():
    pass
