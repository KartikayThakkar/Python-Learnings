import pygame,random

pygame.init()

width = 1000
height = 600

white = 255, 255, 255
red = 255, 0, 0
black = 0,0,0
green = 0,255,0

screen = pygame.display.set_mode((width, height))

copter = pygame.image.load("assets/helicopter_1.png")

clock = pygame.time.Clock()
FPS = 100

copter_y = height/2

move_x = 5

wall_x = width + 20
wall_y = random.randint(0, height)
wall_height = random.randint(100,300)

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(black)

    screen.blit(copter, (100, copter_y))

    pygame.draw.rect(screen, green, (0,0,width,50))
    pygame.draw.rect(screen, green, (0,height-50,width,50))

    pygame.draw.rect(screen, green, (wall_x, wall_y, 30, wall_height))

    wall_x -= move_x

    if wall_x < 0:
        wall_x = width + 20
        wall_y = random.randint(0, height)
        wall_height = random.randint(100, 300)

    pygame.display.update()
    clock.tick(FPS)