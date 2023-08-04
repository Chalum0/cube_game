from setting import *
import pygame
import random
import math


class Block:
    def __init__(self, coord, player_coords, map_, matrix_coords, vm, screen, fov):
        self.points = ((coord[0] + half_block, coord[1] + half_block, coord[2] - half_block),
                (coord[0] + half_block, coord[1] - half_block, coord[2] - half_block),
                (coord[0] - half_block, coord[1] - half_block, coord[2] - half_block),
                (coord[0] - half_block, coord[1] + half_block, coord[2] - half_block),
                (coord[0] + half_block, coord[1] + half_block, coord[2] + half_block),
                (coord[0] + half_block, coord[1] - half_block, coord[2] + half_block),
                (coord[0] - half_block, coord[1] - half_block, coord[2] + half_block),
                (coord[0] - half_block, coord[1] + half_block, coord[2] + half_block))
        self.coord = coord
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.faces = []
        self.type = map_[matrix_coords[0]][matrix_coords[1]]
        self.matrix_coords = matrix_coords
        self.player_distance = math.dist(self.coord, player_coords)
        self.sphere_size = math.sqrt(half_block**2 *3)
        self.vm = vm
        screen_x, screen_y = screen.get_size()
        self.fx = screen_x/2 / fov
        self.fy = screen_y/2 / fov
        self.fxd = math.sqrt(half_block**2 * 3+self.fx**2)/2+half_block
        self.fyd = math.sqrt(half_block**2 * 3+self.fy**2)/2+half_block




        # a laisser tout en bas connard
        self.update_render(player_coords, map_, vm)


    def __lt__(self, other):
        return self.player_distance < other.player_distance

    def update_distance(self, player_pos, vm):
        self.player_distance = math.dist(self.coord, player_pos)
        boolean = False
        point = (self.coord[0]-player_pos[0], self.coord[1]-player_pos[1], self.coord[2]-player_pos[2])
        transformed_point = (point[0] * vm[7] + point[2] * vm[6],
                point[0] * vm[0] + point[1] * vm[5] - point[2] * vm[1],
                point[1] * vm[4] + point[2] * vm[2] - point[0] * vm[3])
        if not(transformed_point[2] < -self.sphere_size or self.type == 0):
            if not (abs(transformed_point[0]) >transformed_point[2] * self.fx + self.fxd) or (abs(transformed_point[1]) >transformed_point[2] * self.fy + self.fyd):
                boolean = True
        return boolean

    def update_render(self, player_pos, map_, vm):
                self.faces = []
                if player_pos[2] < self.coord[2]-half_block:
                    if not self.matrix_coords[0] == 0:
                        if map_[self.matrix_coords[0] - 1][self.matrix_coords[1]] != 1:
                            self.faces.append((1, 2, 3, 0))  # front
                    else:
                        self.faces.append((1, 2, 3, 0))  # front

                if player_pos[2] > self.coord[2]+half_block:
                    if not self.matrix_coords[0] == len(map_)-1:
                        if map_[self.matrix_coords[0] + 1][self.matrix_coords[1]] != 1:
                            self.faces.append((7, 6, 5, 4))  # back
                    else:
                        self.faces.append((7, 6, 5, 4))  # back

                if player_pos[0] < self.coord[0]-half_block:
                    if not self.matrix_coords[1] == 0:
                        if map_[self.matrix_coords[0]][self.matrix_coords[1] - 1] != 1:
                            self.faces.append((7, 6, 2, 3))  # left
                    else:
                        self.faces.append((7, 6, 2, 3))  # left

                if player_pos[0] > self.coord[0]+half_block:
                    if not self.matrix_coords[1] == len(map_[self.matrix_coords[0]])-1:
                        if map_[self.matrix_coords[0]][self.matrix_coords[1] + 1] != 1:
                            self.faces.append((1, 5, 4, 0))  # right
                    else:
                        self.faces.append((1, 5, 4, 0))  # right

                if player_pos[1] < self.coord[1]-half_block:
                    self.faces.append((1, 2, 6, 5))  # top
                if player_pos[1] > self.coord[1]+half_block:
                    self.faces.append((7, 4, 0, 3))  # bottom
