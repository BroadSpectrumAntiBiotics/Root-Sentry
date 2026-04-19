from usefulFeatures import clear_screen, type_text

def hinter(player, current_stage):
    clear_screen()
    type_text(f"{f"{" "*8}{current_stage.numberofcorrupt} number of files are corrupt among the next {len(current_stage.stage)} files.":^120}", 0.01)
    input(f"{f"{" "*8}Press enter to continue, {player.name}.":^120}")

def currentfile_perk():
    type_text(f"{f"{" "*8} ATTENTION! THIS FILE IS CORRUPTED!":^120}", 0.01)
    input(f"{f"{" "*8}Press enter to continue.":^120}")
