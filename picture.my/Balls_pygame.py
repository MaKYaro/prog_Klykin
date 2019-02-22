import pygame
import random
import math

# Define some colors
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


def make_ball():

    ball = Ball()

    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)

    return ball


def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Moving Balls")
    done = False
    clock = pygame.time.Clock()

    ball_list = []

    for number in range(2):
        ball = make_ball()
        ball_list.append(ball)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)

        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
            for globe in ball_list:
                distance_cc = math.sqrt((ball.x - globe.x) ** 2 + (ball.y - globe.y) ** 2)
                if 0 < distance_cc <= 2 * BALL_SIZE + 1:
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
                        ball.change_x = ball.change_x * math.cos(angle) + ball.change_y * math.sin(angle)
                        ball.change_y = -ball.change_x * math.sin(angle) + ball.change_y * math.cos(angle)
                        globe.change_x = globe.change_x * math.cos(angle) + globe.change_y * math.sin(angle)
                        globe.change_y = -globe.change_x * math.sin(angle) + globe.change_y * math.cos(angle)
                        variable = ball.change_x
                        ball.change_x = globe.change_x
                        globe.change_x = variable
                        ball.change_x = math.ceil(ball.change_x * math.cos(angle) - ball.change_y * math.sin(angle))
                        ball.change_y = math.ceil(ball.change_x * math.sin(angle) + ball.change_y * math.cos(angle))
                        globe.change_x = math.ceil(globe.change_x * math.cos(angle) - globe.change_y * math.sin(angle))
                        globe.change_y = math.ceil(globe.change_x * math.sin(angle) + globe.change_y * math.cos(angle))

        screen.fill(BLACK)

        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

        clock.tick(40)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()