class Attacker:
    """Общий класс для всех объектов игры"""
    health = None
    attack = None
    answer = None

    def attack(self, target):
        """
        Нападение на соперника
        :param target: соперник
        :return: Value
        """
        target.health -= self.attack

    def is_alive(self):
        """
        Проверка health
        :return: Value
        """

        return self.health > 0
