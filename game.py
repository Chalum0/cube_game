from setting import *
import pygame
import player
import math
import cube
import numpy

class Game:
    def __init__(self):
        self.player = player.Player()
        self.all_blocks = []
        self.map = [[1 for i in range(20)] for k in range(20)]
        self.map[0][1] = 0
        self.sphere_size = math.sqrt(((block_size/2)**2) * 3)
        print(numpy.array(self.map))

        self.make_map_out_of_list(self.map)
    def display_rect(self, points: tuple, view_matrix: tuple, screen_x: int, screen_y: int, screen: pygame.surface.Surface):
        ps = []
        vspoints = []
        for point in points:
            point = (point[0]-self.player.pos[0], point[1]-self.player.pos[1], point[2]-self.player.pos[2])
            transformed_point = (point[0] * math.cos(self.player.camY) + point[2] * math.sin(self.player.camY),
                                 point[0]*view_matrix[0] + point[1] * math.cos(self.player.camX) - point[2] * view_matrix[1],
                                 point[1] * math.sin(self.player.camX) + point[2] * view_matrix[2] - point[0] * view_matrix[3])
            vspoints.append(transformed_point)
            if transformed_point[2]>0:
                point = (transformed_point[0] * self.player.fov / transformed_point[2], transformed_point[1] * self.player.fov / transformed_point[2]) #coordonnées dans le screen space, soit point = (x*fov/z, y*fov/z)
                # pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect(point[0]-10 + screen_x/2, point[1]-10 + screen_y/2, 20, 20))
                
                ps.append((point[0] + screen_x/2, point[1] + screen_y/2, 20,))
            else:
                ps.append(("ez", "ez"))
        return ps, vspoints

    def view_matrix(self):
        return (math.sin(self.player.camX)*math.sin(self.player.camY),
                math.sin(self.player.camX)*math.cos(self.player.camY),
                math.cos(self.player.camX)*math.cos(self.player.camY),
                math.cos(self.player.camX)*math.sin(self.player.camY))

    def make_map_out_of_list(self, list_of_voxels: list[list]):
        for z in range(len(list_of_voxels)):
            for x in range(len(list_of_voxels[z])):
                if list_of_voxels[z][x] == 1:
                    self.all_blocks.append(cube.Block((x * block_size, 0, z * block_size), self.player.pos, self.map, (z, x)))
                else:
                    print("a")
        print(len(self.all_blocks))

    def update_cube_list(self):
        all_displayed_blocks = []
        for block in self.all_blocks:
            block.update_distance(self.player.pos)
            if block.player_distance < -self.sphere_size:
                all_displayed_blocks.append(0)
            else:
                all_displayed_blocks.append(1)
        self.all_blocks = sorted(self.all_blocks)
        self.all_blocks.reverse()
