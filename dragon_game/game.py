from enemies import *
from hero import *


def input_check(message=''):
    answer = None
    while answer is None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Твой сопреник - ', dragon.color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = input_check('Ответ:\n')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно!')
            else:
                dragon.attack(hero)
                print('Ошибка! \nБудь внимательнее!')
        if dragon.is_alive():
            break
        print('Дракон', dragon.color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero.experience)
    else:
        print('К сожалению, Вы проиграли...')


def start_game():
        print('Добро пожаловать на поле арифметической битвы!')
        print('Представьтесь, пожалуйста: ', end='')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        print('У Вас на пути', dragon_number, 'дракона!')
        game_tournament(hero, dragon_list)
