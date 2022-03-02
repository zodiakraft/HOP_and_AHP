import os
import math

from operator import itemgetter
import pygame

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
pygame.init()

FPS = 60
WIDTH = 800
HEIGHT = 600
K = 100
HUE = 140
NX = WIDTH/2 - (K / 2)
NY = HEIGHT/2 - (K / 2)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
angle = 0

# cube - 100
# x y z - пока x и z [0, 2]
coordinates = [[0, -50, 50, 50, 1, 3, 4], [1, 50, 50, 50, 0, 2, 5], [2, 50, -50, 50, 1, 3, 6], [3, -50, -50, 50, 0, 2, 7],
               [4, -50, 50, -50, 0, 5, 7], [5, 50, 50, -50, 1, 4, 6], [6, 50, -50, -50, 2, 5, 7], [7, -50, -50, -50, 3, 4, 6]]

def draw_cube(local_angle, local_coordinates):
    
    polygon_coordinates = sorted(local_coordinates, key=itemgetter(3))
    view_coordinates = [sorted(local_coordinates, key=itemgetter(1))[0][1], sorted(local_coordinates, key=itemgetter(1))[-1][1]]
    print(view_coordinates)

    color = pygame.Color(255, 255, 255)
    hsv = color.hsva
    color2 = pygame.Color(255, 255, 255)
    hsv2 = color2.hsva
    color3 = pygame.Color(255, 255, 255)
    hsv3 = color3.hsva

    color.hsva = (HUE, hsv[1] + 100, hsv[2] - 25, hsv[3])
    color2.hsva = (HUE, hsv2[1] + 100, hsv2[2], hsv[3])
    color3.hsva = (HUE, hsv3[1] + 100, hsv3[2] - 50, hsv[3])

    pygame.draw.polygon(screen, color, ((NX, NY), (NX + K, NY),
                                        (NX + K, NY + K), (NX, NY + K)))

    pygame.draw.polygon(screen, color2, ((NX, NY), (NX + K, NY),
                                        (NX + K, NY + K), (NX, NY + K)))

    pygame.draw.polygon(screen, color3, ((NX, NY), (NX + K, NY),
                                        (NX + K, NY + K), (NX, NY + K)))

draw_cube(angle, coordinates)

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                angle -= 1
                draw_cube(angle, coordinates)
            elif i.key == pygame.K_RIGHT:
                angle += 1
                draw_cube(angle, coordinates)

    pygame.display.update()
    clock.tick(FPS)