import pygame

pygame.init()

red = 255,0,0
green = 0,255,0
white = 255,255,255
yellow = 255,255,0

screen = pygame.display.set_mode((900, 600))

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(red)

    pygame.display.update()
