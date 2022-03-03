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
coordinates = [[0, -50, 50, 50], [1, 50, 50, 50], [2, 50, -50, 50], [3, -50, -50, 50],
               [4, -50, 50, -50], [5, 50, 50, -50], [6, 50, -50, -50], [7, -50, -50, -50]]

segments = [[0, 0, 1], [1, 0, 3], [2, 0, 4], [3, 1, 2], 
            [4, 1, 5], [5, 2, 3], [6, 2, 6], [7, 3, 7], 
            [8, 4, 5], [9, 4, 7], [10, 5, 6], [11, 6, 7]]

facets = [[0, 0, 3, 5, 1], [1, 3, 4, 6, 10], [2, 8, 9, 10, 11], [3, 1, 2, 7, 9], [4, 0, 2, 4, 8], [5, 5, 6, 7, 11]]

def draw_cube(local_angle, local_coordinates, local_segments, local_facets):
    
    index_polygon = lambda lambda_angle: 3 if ((lambda_angle >= 0 and lambda_angle < 45) or (lambda_angle >= 135 and lambda_angle < 225) or (lambda_angle >= 315 and lambda_angle <= 359)) else 1
    print(index_polygon(local_angle))
    polygon_coordinates = sorted(local_coordinates, key=itemgetter(index_polygon(local_angle)))
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

# draw_cube(angle, coordinates, segments, facets)

while True:

    keys = pygame.key.get_pressed()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

    if keys[pygame.K_LEFT]:
        angle -= 1
        draw_cube(angle, coordinates, segments, facets)
        print(angle)
    elif keys[pygame.K_RIGHT]:
        angle += 1
        draw_cube(angle, coordinates, segments, facets)
        print(angle)

    pygame.display.update()
    clock.tick(FPS)