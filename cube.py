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
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
        self.back = False
        self.front = False
        self.update_render(player_coords)

    def update_render(self, player_pos):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False
        self.back = False
        self.front = False
        if player_pos[2] < self.coord[2]:
            self.front = True
        if player_pos[2] > self.coord[2]:
            self.back = True
        if player_pos[0] < self.coord[0]:
            self.left = True
        if player_pos[0] > self.coord[0]:
            self.right = True
        if player_pos[1] < self.coord[1]:
            self.top = True
        if player_pos[1] > self.coord[1]:
            self.bottom = True
