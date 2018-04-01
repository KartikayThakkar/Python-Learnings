import pygame
import random

pygame.init()

width = 900
height = 600

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width, height))

x = 0
y = 0

snake_width = 50

move_x = 0
move_y = 0

apple = pygame.image.load("apple.png")

apple_x = random.randint(0, width - 54)
apple_y = random.randint(0, height - 68)

clock = pygame.time.Clock()
FPS = 90

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 5
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -5
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 5
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -5
                move_x = 0

    screen.fill(white)
    pygame.draw.rect(screen, red, [x,y,snake_width,50])
    screen.blit(apple, (apple_x, apple_y))

    snake_rect = pygame.Rect(x,y,50,50)
    apple_rect = pygame.Rect(apple_x, apple_y, apple.get_width(), apple.get_height())

    # snake_rect.left
    # snake_rect.right
    # snake_rect.top
    # snake_rect.bottom
    #
    # snake_rect.x
    # snake_rect.y

    if snake_rect.colliderect(apple_rect):
        apple_x = random.randint(0, width - 54)
        apple_y = random.randint(0, height - 68)
        snake_width += 10

    x += move_x
    y += move_y

    pygame.display.update()
    clock.tick(FPS)