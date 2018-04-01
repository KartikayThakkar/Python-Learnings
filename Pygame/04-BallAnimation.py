import pygame
import random

pygame.init()

red = 255, 0, 0
green = 0, 255, 0
white = 255, 255, 255
black = 0, 0, 0
yellow = 255, 255, 0

colorList = [black, green, white, yellow]
color = random.choice(colorList)

height = 600
width = 900

screen = pygame.display.set_mode((width, height))

x = 0
y = 0

move_x = 2
move_y = 2

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)
    pygame.draw.circle(screen, color, (x,y), 80)

    x += move_x
    y += move_y
    if x >= width - 80:
        move_x = -2
        color = random.choice(colorList)
    elif y >= height - 80:
        move_y = -2
        color = random.choice(colorList)
    elif x < 80:
        move_x = 2
        color = random.choice(colorList)
    elif y < 80:
        move_y = 2
        color = random.choice(colorList)

    pygame.display.update()
    clock.tick(FPS)
