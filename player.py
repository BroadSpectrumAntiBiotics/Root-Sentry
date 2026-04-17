
 
class Player:
    def __init__(self, name, hp, scripts, budget):
        self.name = name
        self.hp = hp
        self.scripts = scripts
        self.budget = budget
        self.update = 0
    
    def budget_control(self, addition):
        self.budget += addition

    def hp_control(self, addition):
        self.hp += addition
        

