from setting import *
import pygame
import numpy
import time
import game
import math


pygame.init()
pygame.font.init()
pygame.display.set_caption("")
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
max_fps = 60
screen_x, screen_y = screen.get_size()
pygame.mouse.set_visible(False)

game = game.Game()
previous_mouse_pos = 0

playing = True
while playing:
    screen.fill((0, 0, 0))

    points = ((10, 10, 30), (10, -10, 30), (-10, -10, 30), (-10, 10, 30), (10, 10, 60), (10, -10, 60), (-10, -10, 60), (-10, 10, 60))
    view_matrix = game.view_matrix()
    ps = game.display_rect(points, view_matrix, screen_x, screen_y, screen)

    game.player.camY -= numpy.clip((pygame.mouse.get_rel()[0])/200, -0.2, .2)


    for i in points_to_display:
        zcd = ps[i][2] - game.player.pos[2]
        if 


        try:
            pygame.draw.line(screen, (255, 255, 0), (ps[i[0]][0], ps[i[0]][1]), (ps[i[1]][0], ps[i[1]][1]))
        except IndexError:
            pass


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        game.player.pos[0] += player_speed
    if keys[pygame.K_q]:
        game.player.pos[0] -= player_speed
    if keys[pygame.K_z]:
        game.player.pos[2] += player_speed
    if keys[pygame.K_s]:
        game.player.pos[2] -= player_speed
    if keys[pygame.K_SPACE]:
        game.player.pos[1] -= player_speed
    if keys[pygame.K_LCTRL]:
        game.player.pos[1] += player_speed


    pygame.display.flip()
    clock.tick(max_fps)
    pygame.display.set_caption(f"{game.player.camY}")
    # pygame.mouse.set_pos((screen_x/2, screen_y/2))
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                time.sleep(0.2)
                playing = False
