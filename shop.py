from scripts import script_names, script_prices
from usefulFeatures import type_text, clear_screen

def shopping(budget, player):
    clear_screen()
    type_text(f"Scripts: {script_names}", 0.01)
    while True:
        try:
            buy = input("Enter a script name to download it." \
            "\n>>>")
            
            if budget >= script_prices[script_names.index(buy)]:
                player.scripts.append(buy)
                player.budget_control(-int(script_prices[script_names.index(buy)]))

            break
        except:
            type_text("Invalid script name. Please try again.")
    

    