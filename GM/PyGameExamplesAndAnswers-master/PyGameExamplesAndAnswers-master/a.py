import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(0)
    pygame.draw.circle(window, (255, 0, 0), (250, 250), 100)
    pygame.display.flip()
pygame.quit()
exit()