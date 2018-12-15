from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        self.health = 100
        self.attack = 50
        self.name = name
        self.experience = 0

    def attack(self, target):
        """
        Атакует соперника, уменьшая его health
        :param target: сопеник
        :return: измененные target._health, self.experience
        """
        target.health -= self.attack
        self.experience += target.attack
