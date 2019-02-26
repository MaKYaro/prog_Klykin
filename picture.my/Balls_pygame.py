import pygame
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25


class Ball:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

        self.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        self.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

        self.change_x = 1
        self.change_y = 1

    def speed_change_strait(self, angle, globe):
        self.change_x = self.change_x * math.cos(angle) + self.change_y * math.sin(angle)
        self.change_y = -self.change_x * math.sin(angle) + self.change_y * math.cos(angle)
        globe.change_x = globe.change_x * math.cos(angle) + globe.change_y * math.sin(angle)
        globe.change_y = -globe.change_x * math.sin(angle) + globe.change_y * math.cos(angle)
        variable = self.change_x
        self.change_x = globe.change_x
        globe.change_x = variable

    def speed_change_back(self, angle):
        self.change_x = math.ceil(self.change_x * math.cos(angle) - self.change_y * math.sin(angle))
        self.change_y = math.ceil(self.change_x * math.sin(angle) + self.change_y * math.cos(angle))

    def speed_change_after_wall(self):
        if self.y > SCREEN_HEIGHT - BALL_SIZE or self.y < BALL_SIZE:
            self.change_y *= -1
        if self.x > SCREEN_WIDTH - BALL_SIZE or self.x < BALL_SIZE:
            self.change_x *= -1

    def coords_change(self):
        self.x += self.change_x
        self.y += self.change_y

    #def push_apart(self, globe):
     #   distance_cc = math.sqrt((self.x - globe.x) ** 2 + (self.y - globe.y) ** 2)



def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Moving Balls")
    done = False
    clock = pygame.time.Clock()

    ball_list = []

    for number in range(2):
        ball = Ball()
        ball_list.append(ball)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = Ball()
                    ball_list.append(ball)

        for ball in ball_list:

            ball.coords_change()
            ball.speed_change_after_wall()
            for globe in ball_list:
                distance_cc = math.sqrt((ball.x - globe.x) ** 2 + (ball.y - globe.y) ** 2)
                if distance_cc <= 2 * BALL_SIZE:
                    leg_1 = globe.y - ball.y
                    leg_2 = globe.x - ball.x
                    if leg_2 == 0:
                        variable = ball.change_y
                        ball.change_y = globe.change_y
                        globe.change_y = variable
                    elif leg_1 == 0:
                        variable = ball.change_x
                        ball.change_x = globe.change_x
                        globe.change_x = variable
                    else:
                        angle = math.atan(leg_1 / leg_2)
                        ball.speed_change_strait(angle, globe)
                        ball.speed_change_back(angle)
                        globe.speed_change_back(angle)

        screen.fill(BLACK)

        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

        clock.tick(200)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()