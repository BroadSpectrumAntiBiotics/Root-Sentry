
from fileNames import file_names
import random
import string
import hashlib

alphabet_list = list(string.ascii_lowercase)


class Parameter:
    def __init__(self, filename, filetype):
        self.name = filename
        self.type = filetype
        self.creationDay = random.randint(1, 30)
        self.creationMonth = random.randint(1, 12)
        self.creationYear = random.randint(2000, 2025)
        self.modificationDay = random.randint(1, 30)
        self.modificationMonth = random.randint(1, 12)
        self.modificationYear = random.randint(self.creationYear, 2026)
        self.creation = str(self.creationDay) + "." + str(self.creationMonth) + "." + str(self.creationYear)
        self.modification = str(self.modificationDay) + "." + str(self.modificationMonth) + "." + str(self.modificationYear)
        self.hash = (hashlib.sha256(filename.encode('utf-8')).hexdigest())[:8]
    
    def corruptedName(self):
        for letter in alphabet_list:
            letter = random.choice(alphabet_list)
            if letter not in self.name: 
                corruptedLetter = letter
                break

        self.corruptname = list(self.name)
        self.corruptname[random.randint(0, len(self.name)-1)] = corruptedLetter

        self.name = ("".join(self.corruptname))
        
        return self.name

    def corruptedType(self):
        types = []
        for type in file_names:
            typeExt = type[(type.find(".")):]
            types.append(typeExt)
        self.type = random.choice(types)
        return self.type

    def corruptedCreation(self):
        one = [self.creationDay, self.creationMonth, self.creationYear]
        two = random.choice(one)
        if two == self.creationDay:
            self.creationDay = random.randint(1, 30)
        if two == self.creationMonth:
            self.creationMonth = random.randint(1, 12)
        if two == self.creationYear:
            self.creationYear = random.randint(2000, 2026)
        self.creation = str(self.creationDay) + "." + str(self.creationMonth) + "." + str(self.creationYear)
        return self.creation

    def corruptedModification(self):
        one = [self.modificationDay, self.modificationMonth, self.modificationYear]
        two = random.choice(one)
        if two == self.modificationDay:
            self.modificationDay = random.randint(1, 30)
        if two == self.modificationMonth:
            self.modificationMonth = random.randint(1, 12)
        if two == self.modificationYear:
            self.modificationYear = random.randint(self.creationYear+1, 2026)
            
            

        self.modification = str(self.modificationDay) + "." + str(self.modificationMonth) + "." + str(self.modificationYear)
        return self.modification
        
    def corruptedHash(self):
        self.hash = hashlib.sha256(random.choice(alphabet_list).encode('utf-8')).hexdigest()[:8]
        
        return self.hash
    
    def corruptChoice(self, difficulty):
        corruption = ["name", "type", "creation", "modification"]
        if difficulty > 3:
            corruption.append("hash")
        corruptionChoice = random.choice(corruption)
        if corruptionChoice == "name":
            return self.corruptedName()
        if corruptionChoice == "type":
            return self.corruptedType()
        if corruptionChoice == "creation":
            return self.corruptedCreation()
        if corruptionChoice == "modification":
            return self.corruptedModification()
        if corruptionChoice == "hash":
            return self.corruptedHash()


    

        

