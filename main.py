import setting
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

camX = 0
camY = 0

player_pos = (0, 0, 0)
fov = 400

playing = True
while playing:

    view_matrix = (math.sin(camX)*math.sin(camY), math.sin(camX)*math.cos(camY), math.cos(camX)*math.cos(camY), math.cos(camX)*math.sin(camY))

    point = (0, 0, -10)  # coordonnées dans le world space
    point = (point[0]-player_pos[0], point[1]-player_pos[1], point[2]-player_pos[2])
    transformed_point = (point[0] * math.cos(camY) + point[2] * math.sin(camY), point[0] * view_matrix[0] + point[1] * math.cos(camX) - point[2] * view_matrix[1], point[1] * math.sin(camX) + point[2] * view_matrix[2] - point[0] * view_matrix[3])
    print(transformed_point)
    if transformed_point[2] > 0:
        print("point devant la caméra")
        point = (transformed_point[0] * fov / transformed_point[2], transformed_point[1] * fov / transformed_point[2]) #coordonnées dans le screen space, soit point = (x*fov/z, y*fov/z)
        pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect(point[0]-10, point[1]-10, 20, 20))
    else:
        print("point derrière la caméra")
        pass #le point est derrière la caméra


    pygame.display.flip()
    clock.tick(max_fps)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False
