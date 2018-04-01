import pygame

pygame.init()

width = 900
height = 600

white = 255, 255, 255
red = 255, 0, 0

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
FPS = 50

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    pygame.display.update()
    clock.tick(FPS)