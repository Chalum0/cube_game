import random
points_to_display = ((0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7))
player_speed = 1
cam = 0.05
block_size = 10
front_face = (1, 2, 3, 0)
back_face = (7, 6, 5, 4)
left_face = (7, 6, 2, 3)
right_face = (1, 5, 4, 0)
top_face = (1, 2, 6, 5)
bottom_face = (7, 4, 0, 3)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (255, 255, 0), (0, 255, 255)]

face = {}

for i in range(7):
    face[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
