# pygame.transform module
# https://www.pygame.org/docs/ref/transform.html
#
# How to rotate an image around its center while its scale is getting larger(in Pygame)
# https://stackoverflow.com/questions/54462645/how-to-rotate-an-image-around-its-center-while-its-scale-is-getting-largerin-py/54713639#54713639
#
# GitHub - PyGameExamplesAndAnswers - Collision and Intersection - Circle and circle
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_surface_rotate.md

import pygame
import os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../resource'))
pygame.init()

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
try:
    image = pygame.image.load('icon/AirPlaneFront1-128.png')
except:
    text = pygame.font.SysFont('Times New Roman', 50).render('image', False, (255, 255, 0))
    image = pygame.Surface((text.get_width()+1, text.get_height()+1))
    pygame.draw.rect(image, (0, 0, 255), (1, 1, *text.get_size()))
    image.blit(text, (1, 1))

start = False
angle = 0
zoom = 1.0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            start = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    w, h = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    pivot        = pygame.math.Vector2(w/2, -h/2)
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    move   = (-pivot[0] + min_box[0] - pivot_move[0], pivot[1] - max_box[1] + pivot_move[1])
    origin = (pos[0] + zoom * move[0], pos[1] + zoom * move[1])

    screen.fill(0)
    rotozoom_image = pygame.transform.rotozoom(image, angle, zoom)
    if start:
        angle += 1
        zoom += 0.01

    screen.blit(rotozoom_image, origin)
    pygame.draw.rect (screen,(255, 0, 0), (*origin, *rotozoom_image.get_size()),2)
    
    pygame.draw.line(screen, (0, 255, 0), (pos[0]-20, pos[1]), (pos[0]+20, pos[1]), 3)
    pygame.draw.line(screen, (0, 255, 0), (pos[0], pos[1]-20), (pos[0], pos[1]+20), 3)
    pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()

pygame.quit()
exit()