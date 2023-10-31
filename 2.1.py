import random
import time

class Warrior:
    def __init__(self, name, health = 100):         
        self.name= name
        self.health = health
        self.damage = 20
    def __del__(self):
        print("Ты храбро сражался, ", self.name, "!")

def battle (warrior_1, warrior_2):
    while ((warrior_1.health > 0) and (warrior_2.health > 0)):
        if (random.randrange(1, 3, 1) == 1):
            print("Аттакует ", warrior_1.name)
            warrior_2.health -= warrior_1.damage
            print("У ", warrior_2.name, "осталось ", warrior_2.health, " очков здоровья")
        else:
            print("Аттакует ", warrior_2.name)
            warrior_1.health -= warrior_2.damage
            print("У ", warrior_1.name, "осталось ", warrior_1.health, " очков здоровья")
        
    if (warrior_1.health <= 0):
        print("Победил ", warrior_2.name, "! ", warrior_1.name, " теперь в лучшем мире, ибо нет мира лучше Совнгарда!")
        return True
    else:
        print("Победил ", warrior_1.name, "! ", warrior_2.name, " теперь в лучшем мире, ибо нет мира лучше Совнгарда!")
        return False

first_warrior = Warrior("Ульфрик Буревестник")
second_warrior = Warrior("Генерал Туллий")

result = battle(first_warrior, second_warrior)
if (result):
    del first_warrior
else:
    del second_warrior

time.sleep(5)
