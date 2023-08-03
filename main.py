import settings
import pygame
import random
import time
import game
import math

pygame.init()
pygame.font.init()
pygame.display.set_caption("")
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
max_fps = 60
screen_x, screen_y = screen.get_size()

game = game.Game()

playing = True
while playing:


    pygame.display.flip()
    clock.tick(max_fps)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False
