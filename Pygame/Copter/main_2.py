import pygame,random
import time

pygame.init()

width = 1000
height = 600

white = 255, 255, 255
red = 255, 0, 0
black = 0,0,0
green = 0,255,0

screen = pygame.display.set_mode((width, height))

copter_1 = pygame.image.load("assets/helicopter_1.png")
copter_2 = pygame.image.load("assets/helicopter_2.png")

cop_list = [copter_1, copter_2]

clock = pygame.time.Clock()
FPS = 100

bg = pygame.image.load("assets/bg_3.jpg")

def game():
    copter_y = height / 2
    move_copter = 2

    copterCurrentImage = 1

    move_x = 5

    bg_x = 0

    wall_x = width + 20
    wall_y = random.randint(0, height)
    wall_height = random.randint(100, 300)

    alive = True

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if alive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        move_copter = -2
                elif event.type == pygame.KEYUP:
                    move_copter = 2

        copter_y += move_copter

        screen.fill(black)
        screen.blit(bg,(bg_x,0))

        if copterCurrentImage == 1:
            screen.blit(copter_1, (100, copter_y))
            copterCurrentImage = 2
        elif copterCurrentImage == 2:
            screen.blit(copter_2, (100, copter_y))
            copterCurrentImage = 1

        pygame.draw.rect(screen, green, (0,0,width,50))
        pygame.draw.rect(screen, green, (0,height-50,width,50))

        wall_rect = pygame.draw.rect(screen, green, (wall_x, wall_y, 30, wall_height))

        copter_rect = pygame.Rect(100,copter_y,copter_1.get_width(), copter_1.get_height())

        wall_x -= move_x

        bg_x -= 2

        if wall_x < 0:
            wall_x = width + 20
            wall_y = random.randint(0, height)
            wall_height = random.randint(100, 300)

        if wall_rect.colliderect(copter_rect):
            alive = False
            move_copter = 2
            move_x = 0

        if copter_y > height-110 or copter_y < 50:
            game()

        pygame.display.update()
        clock.tick(FPS)

game()