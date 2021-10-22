from Gladiator import *
import random

class Luk(Gladiator):
    def __init__(self):
        super().__init__("Arcus",7,2,1000,20,random.randint(1,5),random.randint(1,3),
              random.randint(1,10)/10, random.randint(1,10)/10)
        self.maxHP = 20
class MecAStit(Gladiator):
    def __init__(self):
        super().__init__("Gladius",4,5,900,25,random.randint(1,5),random.randint(1,3),
              random.randint(1,10)/10, random.randint(1,10)/10)
        self.maxHP = 25
class Jezdec(Gladiator):
    def __init__(self):
        super().__init__("Equus",14,7,7000,75,random.randint(1,5),random.randint(1,3),
              random.randint(1,10)/10, random.randint(1,10)/10)
        self.maxHP = 75
