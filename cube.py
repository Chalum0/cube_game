from setting import *
import pygame
import math


class Block:
    def __init__(self, coord, player_coords):
        self.points = ((coord[0] + block_size, coord[1] + block_size, coord[2] - block_size),
                       (coord[0] + block_size, coord[1] - block_size, coord[2] - block_size),
                       (coord[0] - block_size, coord[1] - block_size, coord[2] - block_size),
                       (coord[0] - block_size, coord[1] + block_size, coord[2] - block_size),
                       (coord[0] + block_size, coord[1] + block_size, coord[2] + block_size),
                       (coord[0] + block_size, coord[1] - block_size, coord[2] + block_size),
                       (coord[0] - block_size, coord[1] - block_size, coord[2] + block_size),
                       (coord[0] - block_size, coord[1] + block_size, coord[2] + block_size))
        self.coord = coord
        self.faces = []
        self.update_render(player_coords)

    def update_render(self, player_pos):
        self.faces = []
        if player_pos[2] < self.coord[2]-block_size:
            self.faces.append((1, 2, 3, 0))  # front
        if player_pos[2] > self.coord[2]+block_size:
            self.faces.append((7, 6, 5, 4))  # back
        if player_pos[0] < self.coord[0]-block_size:
            self.faces.append((7, 6, 2, 3))  # left
        if player_pos[0] > self.coord[0]+block_size:
            self.faces.append((1, 5, 4, 0))  # right
        if player_pos[1] < self.coord[1]-block_size:
            self.faces.append((1, 2, 6, 5))  # top
        if player_pos[1] > self.coord[1]+block_size:
            self.faces.append((7, 4, 0, 3))  # bottom
