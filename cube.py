from setting import *
import pygame
import math


class Block:
    def __init__(self, coord):
        self.points = ((coord[0] + block_size, coord[1] + block_size, coord[2] - block_size),
                       (coord[0] + block_size, coord[1] - block_size, coord[2] - block_size),
                       (coord[0] - block_size, coord[1] - block_size, coord[2] - block_size),
                       (coord[0] - block_size, coord[1] + block_size, coord[2] - block_size),
                       (coord[0] + block_size, coord[1] + block_size, coord[2] + block_size),
                       (coord[0] + block_size, coord[1] - block_size, coord[2] + block_size),
                       (coord[0] - block_size, coord[1] - block_size, coord[2] + block_size),
                       (coord[0] - block_size, coord[1] + block_size, coord[2] + block_size))
