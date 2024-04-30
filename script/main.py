import random
import os
# belajar OOP
class Player():
    def __init__(self,name = 'iwan',healt= 100,energy=100):
        self.name = name
        self.healt = healt
        self.energy = energy
    def attack (self,target,damage=10):
        target.healt -= damage
        print(f"Berhasil menyerang {Monster().name}")


class Monster():
    def __init__(self,name ='goblin',healt=500):
        self.name = name
        self.healt = healt
    def attack (self,target,damage=20):
        if Monster().healt <= 500:
            target.healt -= damage 
            print(f"berhasil menyerang balik {Player().name}")    
        else :
            print("Monster Sedang Tidur") 

    
player = Player()
goblin = Monster()
# player.attack(goblin)
goblin.attack (player)
print(goblin)




    