import pygame
from pygame.locals import *
import random

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 255)

screen_width = 400
screen_height = 400

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake game')
icon = pygame.image.load('img/snake_icon.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

score = 0

font_over = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
font_hub = pygame.font.SysFont("bahnschrift", 15)

def on_grid_random():
    x = random.randint(0, screen_width-10)
    y = random.randint(0, screen_height-10)
    return x//10 * 10, y//10 * 10

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def collision_snake(c1):
    for i in range(len(c1) - 1, 0, -1):
        if c1[i] == c1[0]:
            return True

def text(msg, color, x1, y1, font):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [x1, y1])

def Score(score):
    v = score_font.render("Your Score: " + str(score), True, (BLUE))
    screen.blit(v, [5, 5])

def gameLoop():
    game_over = False
    snake = [(screen_width/2, screen_height/2)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill(WHITE)

    apple_pos = on_grid_random()
    apple = pygame.Surface((10, 10))
    apple.fill(RED)

    my_direction = LEFT

    while True:
        clock.tick(15)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_r:
                    gameLoop()
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT

        if collision(snake[0], apple_pos):
            apple_pos = on_grid_random()
            snake.append((0, 0))

        if collision_snake(snake):
            game_over = True;

        if (snake[0][0] < 0) or (snake[0][0] > screen_width-10) or (snake[0][1] < 0) or (snake[0][1] > screen_height-10):
            game_over = True

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1]-10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0]+10, snake[0][1])
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1]+10)
        if my_direction == LEFT:
            snake[0] = (snake[0][0]-10, snake[0][1])

        screen.fill(BLACK)
        screen.blit(apple, apple_pos)

        Score(len(snake)-1)

        text("R - Restart  /  Q - Quit", BLUE, 10, screen_height-20, font_hub)


        for pos in snake:
            screen.blit(snake_skin, pos)

        if game_over == True:
            screen.fill(BLACK)
            text("You Lost!", RED, 20, 50, font_over)
            text("Press R to Play Again or Q to Quit", RED, 10, 100, font_over)
            pygame.display.update()

        pygame.display.update()

gameLoop()