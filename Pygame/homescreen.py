import pygame
import random
from SnakeGame import *

pygame.init()

width = 900
height = 600

white = 255,255,255
red = 255,0,0
blue = 0,0,255

screen = pygame.display.set_mode((width, height))

snakeBg = pygame.image.load("snakebg.jpg")

def homeScreen():
    font = pygame.font.SysFont(None, 50)
    welcometext = font.render("Welcome to Snake Game", True, white)
    starttext = font.render("Press SPACE to Start Game", True, white)
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(snakeBg, (0,0))
        screen.blit(welcometext, (230,100))
        screen.blit(starttext, (200, 200))
        pygame.display.update()

homeScreen()