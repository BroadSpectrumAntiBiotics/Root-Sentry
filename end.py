from usefulFeatures import type_text

def ending(player):
    type_text("Update complete.", 0.1)
    type_text("I think you won.", 0.1)
    type_text(f"Congratulations... {player.name}.", 0.1)

def bad_ending():
    type_text("You couldn't keep the system safe.")
    type_text("You lost...", 0.1)
    
