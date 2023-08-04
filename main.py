from setting import *
import pygame
import random
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
font = pygame.font.Font("assets/pixel.ttf", 25)

game = game.Game()
previous_mouse_pos = 0

def calculate_new_xy(old_xy, speed, angle_in_radians):
    new_x = old_xy[0] + -(speed * math.cos(angle_in_radians))
    new_y = old_xy[1] + (speed * math.sin(angle_in_radians))
    return new_x, new_y


def clip3D(p1, p2):

    step = ((zcd-p1[2])/(p2[2]-p1[2]))
    return ((p1[0] + (p2[0]-p1[0])*step) * game.player.fov / zcd + screen_x/2, (p1[1] + (p2[1]-p1[1])*step) * game.player.fov / zcd + screen_y/2)


playing = True
while playing:
    screen.fill((0, 0, 0))

    view_matrix = game.view_matrix()
    faces_displayed = 0
    game.update_cube_list()
    for k in game.all_blocks:
        ps, vspoints = game.display_rect(k.points, view_matrix, screen_x, screen_y, screen)
        k.update_render(game.player.pos, game.map, view_matrix)
        faces_displayed += len(k.faces)
        
        for i in k.faces:
            j = i[0]
            points = [(vspoints[j[0]]), (vspoints[j[1]]), (vspoints[j[2]]), (vspoints[j[3]])]
            points2 = [(ps[j[0]]), (ps[j[1]]), (ps[j[2]]), (ps[j[3]])]
            if False in points2:
                lst = []
                for x in range(len(points)):
                    if points2[x] != False:
                        lst.append(points2[x])
                    if (points2[(x+1)%len(points2)] == False and points2[x] != False) or (points2[(x+1)%len(points2)] != False and points2[x] == False):
                        lst.append(clip3D(points[(x+1)%len(points2)], points[x]))
                if len(lst)>=3:
                    pygame.draw.polygon(screen, k.color, lst)
            else:
                pygame.draw.polygon(screen, k.color, points2)



    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x, y = calculate_new_xy((game.player.pos[0], game.player.pos[2]), player_speed, -game.player.camY + math.radians(180))
        game.player.pos = [x, game.player.pos[1], y]
    if keys[pygame.K_q]:
        x, y = calculate_new_xy((game.player.pos[0], game.player.pos[2]), player_speed, -game.player.camY)
        game.player.pos = [x, game.player.pos[1], y]
    if keys[pygame.K_z]:
        x, y = calculate_new_xy((game.player.pos[0], game.player.pos[2]), player_speed, -game.player.camY + math.radians(360)/4)
        game.player.pos = [x, game.player.pos[1], y]
    if keys[pygame.K_s]:
        x, y = calculate_new_xy((game.player.pos[0], game.player.pos[2]), -player_speed, -game.player.camY + math.radians(360)/4)
        game.player.pos = [x, game.player.pos[1], y]
    if keys[pygame.K_SPACE]:
        game.player.pos[1] -= player_speed
    if keys[pygame.K_LCTRL]:
        game.player.pos[1] += player_speed

    if keys[pygame.K_LEFT]:
        game.player.camY += cam
    if keys[pygame.K_RIGHT]:
        game.player.camY -= cam
    if keys[pygame.K_DOWN] and not math.degrees(game.player.camX) > 90:
        game.player.camX += cam
    if keys[pygame.K_UP] and not math.degrees(game.player.camX) < -90:
        game.player.camX -= cam

    screen.blit(font.render(f"Coords: {round(game.player.pos[0], 1)}, {round(game.player.pos[1], 1)}, {round(game.player.pos[2], 1)}, CamX: {round(math.degrees(game.player.camX), 1)}, CamY: {round(math.degrees(game.player.camY), 1)}", True, (255, 255, 255)), (5, 5))
    screen.blit(font.render(f"Faces rendered: {faces_displayed}", True, (255, 255, 255)), (5, 25))
    screen.blit(font.render(f"Fps: {round(clock.get_fps(), 1)}", True, (255, 255, 255)), (5, 45))

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
