from fileNames import file_names
from perks import currentfile_perk, hinter
import scripts
import virusCreator
from usefulFeatures import type_text, clear_screen
from fileParameters import Parameter
import time, random

class Stages:
    def __init__(self):
        self.stage = []
        self.numberofcorrupt = random.randint(1, virusCreator.virus.difficulty)
        self.numberofvalid = random.randint(1, virusCreator.virus.difficulty)
        self.corruptFiles = []
        self.validFiles = []

    def corruptfilesStager(self):
        for corruptfile in range(self.numberofcorrupt):
            self.corruptFiles.append(random.choice(file_names))
        return self.corruptFiles
        
    def validfilesStager(self):
        for validfile in range(self.numberofvalid):
            self.validFiles.append(random.choice(file_names))
        return self.validFiles
    
    def stager(self, corrupt_files, valid_files):
        self.stage = corrupt_files + valid_files
        random.shuffle(self.stage)
        
        return self.stage

def hash_properties(filehash, difficulty, filePars):
    if difficulty > 4:
        return f"Hash: {filehash:<46}|Hash: {filePars.hash:<20}"
    else:
        return ""

def stagedGame(player):
    current_stage = Stages()
    corrupt_files = current_stage.corruptfilesStager()
    valid_files = current_stage.validfilesStager()
    allFiles = current_stage.stager(corrupt_files, valid_files)
    files = allFiles.copy()
    counter = 0 
    
    if virusCreator.virus.difficulty == 6:
        clear_screen()
        type_text(f"{"\033[33mNew perk unlocked! With a small chance, you will be shown whether a file is corrupted or not.\033[0m":^135}", 0.02)
        input(f"{"Press enter to continue.":^125}")
        clear_screen()

    if virusCreator.virus.difficulty > 2:
        if virusCreator.virus.difficulty == 3:
            clear_screen()
            type_text(f"{"\033[33mNew perk unlocked! Now you know how many files are corrupted in each stage before you begin.\033[0m":^135}", 0.02)
            input(f"{"Press enter to continue.":^125}")
            clear_screen()
        hinter(player, current_stage)
    
    
    
        
    for file in files:
        clear_screen()
        filePars = Parameter(file[:(file.find("."))], file[(file.find(".")):])
        filename = filePars.name
        filetype = filePars.type
        filecreation = filePars.creation
        filemodification = filePars.modification
        filehash = filePars.hash
        if file in corrupt_files:
            filePars.corruptChoice(virusCreator.virus.difficulty)
            if virusCreator.virus.difficulty > 5:
                chance = random.randint(1, 100)
                if chance > 80: #For every file, there's a 10 percent chance that you'll get notified about its corruption.
                    currentfile_perk()



        while True:
            try:
                clear_screen()
                if virusCreator.virus.difficulty == 1:
                    print(f"""
             {"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
             {f"To use a script you downloaded, type its full name. To see your scripts, type 'scripts'.":^100}""")
                detection = input(f"""
            \033[34m
                    EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:
                    =================================                   |=================================
                    File Name: {filename:<41}|File Name: {filePars.name:<30}
                    File Type: {filetype:<41}|File Type: {filePars.type:<30}
                    Creation Date: {filecreation:<37}|Creation Date: {filePars.creation:<20}
                    Last Modified: {filemodification:<37}|Last Modified: {filePars.modification:<20} 
                    {hash_properties(filehash, virusCreator.virus.difficulty, filePars)}                          \033[0m
            {f"{len(files)-counter} files left.":^100}

>>>""")
                if ((detection == "valid") and (file in valid_files)) or ((detection == "corrupted") and (file in corrupt_files)):
                    player.budget_control(int(virusCreator.virus.difficulty * random.randint(1, 5)))
                    player.update += random.randint(3, 5)
                else:
                    if detection in player.scripts:
                        if detection == "autoCheck.exe":
                            scripts.autoCheck(file, valid_files, corrupt_files)
                        if detection == "average_av.exe":
                            if player.hp == 100:
                                type_text("You already have 100 system integrity!")
                                time.sleep(1.5)
                                continue
                            scripts.average_av(player)
                            player.scripts.pop(player.scripts.index(detection))
                            continue
                        if detection == "advanced_av.exe":
                            pass
                        player.scripts.pop(player.scripts.index(detection))
                        counter += 1
                        time.sleep(1.5)
                    elif (detection == "valid") or (detection == "corrupted"):
                        player.budget_control(-(int(virusCreator.virus.difficulty * random.randint(1, 5))))
                        player.hp_control(-(int(virusCreator.virus.difficulty * random.randint(1, 5))))
                    elif detection == "scripts":
                        type_text(f"""\nYou currently have:
            {f"{player.scripts.count("autoCheck.exe")} 'autoCheck.exe'":^100}
            {f"{player.scripts.count("average_av.exe")} 'average_av.exe'":^100}
             {f"{player.scripts.count("advanced_av.exe")} 'advanced_av.exe'":^100}""", 0.01)
                        input("\nPress enter to continue.")
                        continue
                    else:
                        raise KeyError()
                if detection not in scripts.script_names:
                    type_text(f"\nFile marked as {detection}.")
                    time.sleep(0.7)
                    counter += 1
                break
            except:
                type_text("\033[31mWrong command. Please try again.\033[0m")
                time.sleep(1)
        
    if virusCreator.virus.difficulty < 10:
        virusCreator.virus.difficulty += 1

        



