from gameunit import *
from random import *


class Enemy(Attacker):
    """Предковый класс всех enemy"""
    pass


def generate_dragon_list(enemy_number):
    enemy_list = []
    for number in range(enemy_number):
        enemy_list.append(choice(enemies))
    return enemy_list


class Dragon(Enemy):
    """Предковый класс всех dragon"""
    def __init__(self):
        self.__answer = 0

    def set_answer(self, answer):
        """Генерирует правильный ответ"""
        self.__answer = answer

    def check_answer(self, answer):
        """
        Проверяет ответ игрока
        :param player_answer: ответ игрока
        :return: Value
        """
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'
        __quest = 0

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        __quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return __quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
        __quest = 0

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        __quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return __quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'
        __quest = 0

    def question(self):
        x = randint(1, 10)
        y = randint(1, 100)
        __quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return __quest


green_dragon = GreenDragon()
red_dragon = RedDragon()
black_dragon = BlackDragon()
enemies = [green_dragon, red_dragon, black_dragon]
