import pygame
import player
import math

class Game:
    def __init__(self):
        self.player = player.Player()

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
                pygame.draw.rect(screen, (255, 0, 0), pygame.rect.Rect(point[0]-10 + screen_x/2, point[1]-10 + screen_y/2, 20, 20))
                ps.append((point[0] + screen_x/2, point[1] + screen_y/2, 20, 20))
            else:
                ps.append(("ez", "ez"))
        return ps, vspoints

    def view_matrix(self):
        return (math.sin(self.player.camX)*math.sin(self.player.camY),
                math.sin(self.player.camX)*math.cos(self.player.camY),
                math.cos(self.player.camX)*math.cos(self.player.camY),
                math.cos(self.player.camX)*math.sin(self.player.camY))
