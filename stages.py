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

def stagedGame():
    corrupt_files = Stages().corruptfilesStager()
    valid_files = Stages().validfilesStager()
    allFiles = Stages().stager(corrupt_files, valid_files)
    
    for file in allFiles:
        clear_screen()
        filePars = Parameter(file[:(file.find("."))], file[(file.find(".")):])
        if file in corrupt_files:

            detection = input(f"""
               EXPECTED FILE PROPERTIES:   |    DOWNLOADED FILE PROPERTIES:
File Name: {filePars.name:^32}|{filePars.corruptedName():^34}
File Type: {filePars.type:^32}|{filePars.corruptedType():^34}
Creation Date: {filePars.creation:^28}|    {filePars.corruptedCreation():^30}
|
                              
""")
        if file in valid_files:
            detection = input(f"""
               EXPECTED FILE PROPERTIES:   |    DOWNLOADED FILE PROPERTIES:
File Name: {filePars.name:^32}|{filePars.name:^34}
File Type: {filePars.type:^32}|{filePars.type:^34}
Creation Date: {filePars.creation:^27}|{filePars.creation:^30}
|
                              
""")



#virusCreator.virus.difficulty += 1
#player.budget_control(int(virusCreator.virus.difficulty * 10))
