import pygame

pygame.init()

red = 255,0,0
green = 0,255,0
white = 255,255,255
black = 0,0,0
yellow = 255,255,0

screen = pygame.display.set_mode((900, 600))

x = 0
y = 0

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

##    for i in range(0,601):
##        screen.fill(red)
##
##        pygame.draw.rect(screen, black, [10,i * 0.5,50,50])
##
##        pygame.display.update()


    screen.fill(red)
    pygame.draw.rect(screen, black, [x,y,50,50])

    x += 5
    y += 5

    print(x,y)
    
    pygame.display.update()
    clock.tick(FPS)
