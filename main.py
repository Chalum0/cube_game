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
    for k in game.all_blocks:
        ps, vspoints = game.display_rect(k.points, view_matrix, screen_x, screen_y, screen)


        for i in points_to_display:
            if vspoints[i[0]][2]>=zcd and vspoints[i[1]][2]>=zcd:
                pygame.draw.line(screen, (255, 255, 0), (ps[i[0]][0], ps[i[0]][1]), (ps[i[1]][0], ps[i[1]][1]))
            elif not (vspoints[i[0]][2]<=zcd and vspoints[i[1]][2]<=zcd):
                clipped = clip3D(vspoints[i[0]], vspoints[i[1]])
                if vspoints[i[0]][2] < zcd <= vspoints[i[1]][2]:
                    pygame.draw.line(screen, (255, 255, 0), (clipped[0], clipped[1]), (ps[i[1]][0], ps[i[1]][1]))
                if vspoints[i[0]][2] >= zcd > vspoints[i[1]][2]:
                    pygame.draw.line(screen, (255, 255, 0), (ps[i[0]][0], ps[i[0]][1]), (clipped[0], clipped[1]))
        k.update_render(game.player.pos)
        faces_displayed += len(k.faces)


        for i in k.faces:
            points = [(vspoints[i[0]][0], vspoints[i[0]][1], vspoints[i[0]][2]), (vspoints[i[1]][0], vspoints[i[1]][1], vspoints[i[1]][2]), (vspoints[i[2]][0], vspoints[i[2]][1], vspoints[i[2]][2]), (vspoints[i[3]][0], vspoints[i[3]][1], vspoints[i[3]][2])]
            points2 = [(ps[i[0]][0], ps[i[0]][1]), (ps[i[1]][0], ps[i[1]][1]), (ps[i[2]][0], ps[i[2]][1]), (ps[i[3]][0], ps[i[3]][1])]
            if ("ez", "ez") in points2:
                lst = []
                for x in range(len(points) - 1):
                    if points2[x] != ("ez", "ez"):
                        lst.append(points2[x])
                        if points2[x+1] == ("ez", "ez"):
                            lst.append(clip3D(points[x+1], points[x]))

                if len(lst) >= 3:
                    pygame.draw.polygon(screen, colors[0], lst)
            else:
                pygame.draw.polygon(screen, colors[0], points2)



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
