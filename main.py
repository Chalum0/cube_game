from setting import *
import pygame
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

    points = ((10, 10, 30), (10, -10, 30), (-10, -10, 30), (-10, 10, 30), (10, 10, 60), (10, -10, 60), (-10, -10, 60), (-10, 10, 60))
    view_matrix = game.view_matrix()
    ps = game.display_rect(points, view_matrix, screen_x, screen_y, screen)


    for i in points_to_display:
        pygame.draw.line(screen, (255, 255, 0), (ps[i[0]][0], ps[i[0]][1]), (ps[i[1]][0], ps[i[1]][1]))


    pygame.display.flip()
    clock.tick(max_fps)
    pygame.display.set_caption(f"{clock.get_fps()}")
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False
