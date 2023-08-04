from setting import *
import pygame
import random
import math


class Block:
    def __init__(self, coord, player_coords, map_, matrix_coords):
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
        self.update_render(player_coords, map_)
        self.player_distance = math.dist(self.coord, player_coords)

    def __lt__(self, other):
        return self.player_distance < other.player_distance

    def update_distance(self, player_pos):
        self.player_distance = math.dist(self.coord, player_pos)

    def update_render(self, player_pos, map_):
        self.faces = []
        if player_pos[2] < self.coord[2]-half_block:
            if not self.matrix_coords[0] == 0:
                if map_[self.matrix_coords[0] - 1][self.matrix_coords[1]] != 1:
                    self.faces.append(((1, 2, 3, 0), math.dist((self.coord[0], self.coord[1], self.coord[2] - half_block), player_pos)))  # front
            else:
                self.faces.append(((1, 2, 3, 0), math.dist((self.coord[0], self.coord[1], self.coord[2] - half_block), player_pos)))  # front

        if player_pos[2] > self.coord[2]+half_block:
            if not self.matrix_coords[0] == len(map_)-1:
                if map_[self.matrix_coords[0] + 1][self.matrix_coords[1]] != 1:
                    self.faces.append(((7, 6, 5, 4), math.dist((self.coord[0], self.coord[1], self.coord[2] + half_block), player_pos)))  # back
            else:
                self.faces.append(((7, 6, 5, 4), math.dist((self.coord[0], self.coord[1], self.coord[2] + half_block), player_pos)))  # back

        if player_pos[0] < self.coord[0]-half_block:
            if not self.matrix_coords[1] == 0:
                if map_[self.matrix_coords[0]][self.matrix_coords[1] - 1] != 1:
                    self.faces.append(((7, 6, 2, 3), math.dist((self.coord[0] - half_block, self.coord[1], self.coord[2]), player_pos)))  # left
            else:
                self.faces.append(((7, 6, 2, 3), math.dist((self.coord[0] - half_block, self.coord[1], self.coord[2]), player_pos)))  # left

        if player_pos[0] > self.coord[0]+half_block:
            if not self.matrix_coords[1] == len(map_[self.matrix_coords[0]])-1:
                if map_[self.matrix_coords[0]][self.matrix_coords[1] + 1] != 1:
                    self.faces.append(((1, 5, 4, 0), math.dist((self.coord[0] + half_block, self.coord[1], self.coord[2]), player_pos)))  # right
            else:
                self.faces.append(((1, 5, 4, 0), math.dist((self.coord[0] + half_block, self.coord[1], self.coord[2]), player_pos)))  # right

        if player_pos[1] < self.coord[1]-half_block:
            self.faces.append(((1, 2, 6, 5), math.dist((self.coord[0], self.coord[1] - half_block, self.coord[2]), player_pos)))  # top
        if player_pos[1] > self.coord[1]+half_block:
            self.faces.append(((7, 4, 0, 3), math.dist((self.coord[0], self.coord[1] + half_block, self.coord[2]), player_pos)))  # bottom
        self.faces.sort(key=lambda tup: tup[1])
