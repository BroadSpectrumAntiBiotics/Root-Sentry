from fileNames import file_names
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

def stagedGame(player):
    current_stage = Stages()
    corrupt_files = current_stage.corruptfilesStager()
    valid_files = current_stage.validfilesStager()
    allFiles = current_stage.stager(corrupt_files, valid_files)
    files = allFiles.copy()
    counter = 0
    clear_screen()
    type_text(f"{f"{" "*8}{current_stage.numberofcorrupt} number of files are corrupt among the next {len(current_stage.stage)} files.":^120}", 0.01)
    input(f"{f"{" "*8}Press enter to continue, {player.name}.":^120}") 
    
    for file in files:
        clear_screen()
        filePars = Parameter(file[:(file.find("."))], file[(file.find(".")):])
        filename = filePars.name
        filetype = filePars.type
        filecreation = filePars.creation
        filemodification = filePars.modification
        if file in corrupt_files:
            filePars.corruptChoice()

        while True:
            try:
                clear_screen()
                detection = input(f"""
                {"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
                {f"To use a script you downloaded, type its full name. You currently have {player.scripts} installed.":^100}
                {f"{len(files)-counter} files left.":^100}

                    EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:
                    =================================                   |=================================
                    File Name: {filename:<41}|File Name: {filePars.name:<30}
                    File Type: {filetype:<41}|File Type: {filePars.type:<30}
                    Creation Date: {filecreation:<37}|Creation Date: {filePars.creation:<20}
                    Last Modified: {filemodification:<37}|Last Modified: {filePars.modification:<20}
>>>""")
                if ((detection == "valid") and (file in valid_files)) or ((detection == "corrupted") and (file in corrupt_files)):
                    player.budget_control(int(virusCreator.virus.difficulty * random.randint(5, 10)))
                else: #Add budget control for specific types of viruses
                    if detection in player.scripts:
                        if detection == "autoCheck.exe":
                            scripts.autoCheck(file, valid_files, corrupt_files)
                            player.scripts.pop(player.scripts.index(detection))
                            counter += 1
                            time.sleep(2)
                    elif (detection == "valid") or (detection == "corrupted"):
                        player.budget_control(-(int(virusCreator.virus.difficulty * random.randint(1, 5))))
                        player.hp_control(-(int(virusCreator.virus.difficulty * random.randint(1, 5))))
                    else:
                        raise KeyError()
                if detection not in scripts.script_names:
                    type_text(f"\nFile marked as {detection}.")
                    counter += 1
                break
            except:
                type_text("Wrong command. Please try again.")
                time.sleep(1)
        
    if virusCreator.virus.difficulty < 5:
        virusCreator.virus.difficulty += 1

        



