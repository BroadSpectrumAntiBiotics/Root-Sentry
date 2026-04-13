import random
from fileNames import file_names
import virusCreator
from usefulFeatures import type_text, clear_screen
from fileParameters import Parameter

class Stages:
    def __init__(self):
        self.stage = []
        self.numberofcorrupt = random.randint(1, 2 * virusCreator.virus.difficulty)
        self.numberofvalid = random.randint(1, 2 * virusCreator.virus.difficulty)
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
    corrupt_files = Stages().corruptfilesStager()
    valid_files = Stages().validfilesStager()
    allFiles = Stages().stager(corrupt_files, valid_files)
    files = allFiles.copy()
    counter = 0
    for file in files:
        
        filePars = Parameter(file[:(file.find("."))], file[(file.find(".")):])
        if file in corrupt_files:
            choice = filePars.corruptChoice()
            if choice == "corruptedName":

                detection = input(f"""
{"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
{f"{len(files)-counter} files left.":^100}

EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:                    
====================================================|===============================================
File Name: {filePars.name:<41}|File Name: {filePars.corruptedName():<58}                            
File Type: {filePars.type:<41}|File Type: {filePars.type:<58}                                       
Creation Date: {filePars.creation:<37}|Creation Date: {filePars.creation:<46}                       
Last Modified: {filePars.modification:<37}|Last Modified: {filePars.modification:<42}                                   
>>>""")
            if choice == "corruptedType":

                detection = input(f"""
{"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
{f"{len(files)-counter} files left.":^100}

EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:                    
====================================================|===============================================
File Name: {filePars.name:<41}|File Name: {filePars.name:<58}                                       
File Type: {filePars.type:<41}|File Type: {filePars.corruptedType():<58}                            
Creation Date: {filePars.creation:<37}|Creation Date: {filePars.creation:<46}                       
Last Modified: {filePars.modification:<37}|Last Modified: {filePars.modification:<42}               
>>>""")
            if choice == "corruptedCreation":

                detection = input(f"""
{"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
{f"{len(files)-counter} files left.":^100}

EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:
====================================================|===============================================
File Name: {filePars.name:<41}|File Name: {filePars.name:<34}
File Type: {filePars.type:<41}|File Type: {filePars.type:<34}
Creation Date: {filePars.creation:<37}|Creation Date: {filePars.corruptedCreation():<30}
Last Modified: {filePars.modification:<37}|Last Modified: {filePars.modification:<30}
>>>""")

            if choice == "corruptedModification":

                detection = input(f"""
{"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
{f"{len(files)-counter} files left.":^100}

EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:
====================================================|===============================================
File Name: {filePars.name:<41}|File Name: {filePars.name:<34}
File Type: {filePars.type:<41}|File Type: {filePars.type:<34}
Creation Date: {filePars.creation:<37}|Creation Date: {filePars.creation:<30}
Last Modified: {filePars.modification:<37}|Last Modified: {filePars.corruptedModification():<30}
>>>""")
        
        
        
        
        
        
        
        
        if file in valid_files:
            detection = input(f"""
{"For assigning a file as valid, type 'valid'. For a corrupted file, type 'corrupted'.":^100}
{f"{len(files)-counter} files left.":^100}

EXPECTED FILE PROPERTIES:                           |DOWNLOADED FILE PROPERTIES:
====================================================|===============================================
File Name: {filePars.name:<41}|File Name: {filePars.name:<34}
File Type: {filePars.type:<41}|File Type: {filePars.type:<34}
Creation Date: {filePars.creation:<37}|Creation Date: {filePars.creation:<30}
Last Modified: {filePars.modification:<37}|Last Modified: {filePars.modification:<30}
>>>""")
        if (detection == "valid") and (file in valid_files):
            type_text("File marked as valid.")
            player.budget_control(int(virusCreator.virus.difficulty * 10))
        elif (detection == "corrupted") and (file in corrupt_files):
            type_text("File marked as corrupted.")
            player.budget_control((int(virusCreator.virus.difficulty * 10)))
        else:
            #add marking valid a corrupt causing virus and falseInfo
            #marking corrupt a valid causing no progress
            #for example, if file was .bat and user let virus in, random script(item) will be demolished.
            #or if it was a video file, system integrity will fall (or it'll fall everytime a virus gets in.)
            type_text(f"File marked as {detection}.")
            player.budget_control(-(int(virusCreator.virus.difficulty * 5)))
        counter += 1
    virusCreator.virus.difficulty += 1
        



