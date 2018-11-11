import math
from tkinter import *
import time

time_counter = 0
g = 9.8  # Ускорение свободного падения для снаряда.


class Cannon:
    max_velocity = 100


    def __init__(self, x, y, canvas):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.shell_num = None  # TODO: оставшееся на данный момент количество снарядов
        self.direction = math.pi/4
        self.power = 2
        self.power_speed = 0

        self.line_length = 100
        self.line = canv.create_line(x + 70, y - 50, 160, 480, width=30, fill="black")
        self.oval = canv.create_oval(x, y, 100, 500, outline="black", fill="black")


    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        self.direction = math.atan((self.y - y)/(self.x - x))

        self.draw()


    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :param dt:  длительность клика мышки, мс
        :return: экземпляр снаряда типа Shell
        """
        print(self.stop_time)
        print(self.start_time)
        self.time_length = self.stop_time - self.start_time
        self.power_speed = (self.power * self.time_length)/3
        shell = Shell(self.x + 70 + self.line_length*math.cos(self.direction),
                      self.y - 50 + self.line_length*math.sin(self.direction),
                      self.power_speed, self.power_speed, self.canvas, self.direction)

        shells.append(shell)
        print(self.time_length)

    def draw(self):
        """
        Рисует дуло пушки, которое движется в зависимости от перемещений мышки
        :return:
        """
        self.canvas.delete(self.line)

        self.line = self.canvas.create_line(
            self.x + 70,
            self.y - 50,
            self.x + 70 + self.line_length*math.cos(self.direction),
            self.y - 50 + self.line_length*math.sin(self.direction), width=30, fill="black"
        )




class Shell:
    global standard_radius
    standard_radius = 30

    def __init__(self, x, y, Vx, Vy, canvas, direction):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.direction = direction
        self.r = standard_radius
        x1 = x - standard_radius
        y1 = y - standard_radius
        x2 = x + standard_radius
        y2 = y + standard_radius
        self.delta_x = 0
        self.delta_y = 0


        self.canvas = canvas

        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline="pink")


    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt: время элементарного перемещения
        :return: Движущийся снаряд
        """

        ax, ay = 0, g
        self.delta_x = self.Vx * dt * math.cos(self.direction) + ax * (dt ** 2) / 2
        self.delta_y = self.Vy * dt * math.sin(self.direction) + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.Vx += ax * dt
        self.Vy += -ay * dt

        self.draw()

        # TODO: Уничтожать (в статус deleted) снаряд, когда он касается земли.


    def draw(self):
        """
        Рисует движущийся снаряд
        :return:
        """
        self.canvas.move(self.oval, self.delta_x, self.delta_y)


    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r



class Target:
    standard_radius = 5

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = standard_raduis

    def go(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
        :return:
        """

        ax, ay = 0, g
        self.x += self.Vx * dt
        self.y += self.Vy * dt
        self.Vx += ax * dt
        self.Vy += - ay * dt

        # TODO: Шарики-мишени должны отражаться от стенок

    def collide(self, other):
        """
        Расчёт абсолютно упругого соударения
        :param other:
        :return:
        """

        pass  # TODO


def mouse_move_handler(event):
    """
    Направляет дуло пушки в сторону курсора
    :param event: перемещение курсора по экрану
    :return: Координаты курсорв мыши
    """
    cannon.aim(event.x, event.y)


def tick():
    """
    Считает время нажатия клавиши мыши
    :return:
    """
    global time_counter
    time_counter += 1
    for shell in shells:
        shell.go(0.1)

    root.after(10, tick)


def time_start(event):
    """
    Включает счетчик в момент нажания левой клавиши мыши
    :param event: Момент нажатия левой клавиши
    :return: Начальное значение времени
    """
    global time_counter
    cannon.start_time = time_counter


def time_stop(event):
    """
    Выключает счетчик после отпускания левой клавиши
    Обнуляет счетчик
    Запускает снаряд в момент момент отпускания левой клавиши
    :param event: Момент отпускания левой клавиши
    :return: Конечное значение времени
    """
    global time_counter
    cannon.stop_time = time_counter
    cannon.fire()
    time_counter = 0


root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

canv.bind('<Motion>', mouse_move_handler)
canv.bind("<ButtonPress-1>", time_start)
canv.bind("<ButtonRelease-1>", time_stop)
shells = []

cannon = Cannon(70, 550, canv)

tick()
root.mainloop()
