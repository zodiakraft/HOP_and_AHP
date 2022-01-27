import pygame
import sys
import random

FPS = 120
WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
 
r = 30
x = WIN_WIDTH // 2
y = WIN_HEIGHT // 2
x0 = 1 

def d():
    global x, y, x0
    pygame.draw.circle(sc, ORANGE,
                       (x, y), r)
    # обновляем окно
    pygame.display.update()
 
    # Если круг полностью скрылся
    # за правой границей,
    x = x + x0 + (1 ** 2) / 2
    x0 += 1
    print(x, x0)

    if x >= WIN_WIDTH - r:
        x = WIN_WIDTH - r
    if x <= r:
        x = r
    if y >= WIN_HEIGHT - r:
        y = WIN_HEIGHT - r
    if y <= r:
        y = r

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    d()
 
    clock.tick(FPS)