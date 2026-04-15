from usefulFeatures import clear_screen, type_text
import time
script_names = ["autoCheck.exe", "Average_antivirus.exe", "Advanced_antivirus.exe"]
script_prices = [20, 30, 50]

 
def autoCheck(file, valid_files, corrupt_files):
    if file in valid_files:
        return type_text("File is valid.")
    if file in corrupt_files:
        return type_text("File is corrupt.")
    

    