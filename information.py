from usefulFeatures import clear_screen, type_text

commands_list = f"""
'continue' (in the main menu) resumes the update and by that you can progress in the game.
'shop' (in the main menu) lists items or scripts that you can buy to make progressing easier.
'info' (in the main menu) information on certain topics.
'exit' (in the main menu) saves the game and exits.
{"="*60}
'valid' (while detecting files, resuming the update) marks the file as valid.
'corrupted' (while detecting files, resuming the update) marks the file as corrupted.
'scripts' (while detecting files, resuming the update) lists scripts you own.
"""

resources_list = f"""
'System Integrity' is your system's health. Marking files incorrectly causes harm to the system.
'Budget' is your currency. You can spend it to buy scripts.
'Scripts' are used for making progressing easier and fun. Each script has its own feature.
'Update Level' is updating bar. You should fill it to 100% to finish the update. 
"""

def info():
    while True:
        try:
            clear_screen()
            about = input("""
\033[33mInfo Menu:\033[0m
                
'commands' for available commands.
'resources' for game resources.

'exit' to leave this menu.

>>>""")
            if about == 'commands':
                clear_screen()
                type_text(commands_list, 0.01)
                input('Press enter to exit.')
            if about == 'resources':
                clear_screen()
                type_text(resources_list, 0.01)
                input('Press enter to exit.')
            if about == 'exit':
                break
        except:
            type_text("\033[31mWrong command, please try again.\033[0m")
            
