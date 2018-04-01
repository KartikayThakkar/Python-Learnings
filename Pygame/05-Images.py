import pygame

pygame.init()

red = 255, 0, 0
green = 0, 255, 0
white = 255, 255, 255
black = 0, 0, 0
yellow = 255, 255, 0

height = 600
width = 900

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.jpg")

x = 0
y = 0

move_x = 2
move_y = 2

clock = pygame.time.Clock()
FPS = 500

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    screen.blit(ball, (x,y))

    x += move_x
    y += move_y
    if x >= width - 224:
        move_x = -2
    elif y >= height - 224:
        move_y = -2
    elif x < 0:
        move_x = 2
    elif y < 0:
        move_y = 2

    pygame.display.update()
    clock.tick(FPS)
