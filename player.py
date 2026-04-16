

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.scripts = []
        self.budget = 0
        self.update = 0
    
    def budget_control(self, addition):
        self.budget += addition

    def hp_control(self, addition):
        self.hp += addition
        

