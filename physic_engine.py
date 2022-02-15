import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

class Object:
	def __init__(self, type = 'plain_central_symmetry',
                       size = {},
	                   xyz = [0,0,0],
	                   weight = 1):
		self.info = {}
		self.weight = weight
		self.xyz = xyz

	def update(self):
		self.info['type'] = 'plain_central_symmetry'
		self.info['xyz'] = self.xyz
		self.info['weight'] = self.weight

	def interact(self, object):
		#define type
		#calculate xyz
		self.weight += object.weight

	def join(self, object):
		pass


def draw_cube():
    nx = 400 - (k / 2)
    ny = 300 - (k / 2)
    k2 = k / 2

    color = pygame.Color(255, 255, 255)
    hsv = color.hsva
    color2 = pygame.Color(255, 255, 255)
    hsv2 = color2.hsva
    color3 = pygame.Color(255, 255, 255)
    hsv3 = color3.hsva

    color.hsva = (hue, hsv[1], hsv[2] - 25, hsv[3])
    color2.hsva = (hue, hsv2[1], hsv2[2], hsv[3])
    color3.hsva = (hue, hsv3[1], hsv3[2] - 50, hsv[3])
    print(color.hsva, color2.hsva, color3.hsva)

    pygame.draw.polygon(screen, color, ((nx, ny), (nx + k, ny),
                                        (nx + k, ny + k), (nx, ny + k)))

    pygame.draw.polygon(screen, color2, ((nx + k2, ny - k2), (nx + k2 + k, ny - k2),
                                         (nx + k, ny), (nx, ny)))

    pygame.draw.polygon(screen, color3, ((nx + k2, ny - k2 + 200), (nx + k2 + k, ny - k2 + 200),
                                         (nx + k, ny + 200), (nx, ny + 200)))

    pygame.draw.polygon(screen, color3,
                        ((nx + k, ny), (nx + k2 + k, ny - k2),
                         (nx + k2 + k, ny + k2), (nx + k, ny + k)))


#while True:
#    try:
#        k, hue = [int(i) for i in input('Введите размер стороны куба и его оттенок через пробел: ').split()]
#        break
#    except:
#        print('Произошла ошибка. Попробуйте еще раз')

cube = Object(xyz = [0,0,0], size = {''}, weight = 13)
milk = Object(weight = 2)

cube.interact(milk)
cube.update()

print(cube.info)

while pygame.event.wait().type != pygame.QUIT:

    nx = 32.5
    ny = 577.5
    k = 500
    k2 = 250

    pygame.draw.polygon(screen, pygame.Color(255, 255, 255), ((nx, ny), (nx + k, ny),
                                        (nx + k, ny + k), (nx, ny + k)))

    pygame.draw.polygon(screen, pygame.Color(255, 255, 255), ((nx + k2, ny - k2), (nx + k2 + k, ny - k2),
                                         (nx + k, ny), (nx, ny)))

    pygame.draw.polygon(screen, pygame.Color(255, 255, 255),
                        ((nx + k, ny), (nx + k2 + k, ny - k2),
                         (nx + k2 + k, ny + k2), (nx + k, ny + k)))

    k = 100
    hue = 0

    draw_cube()
    pygame.display.flip()
pygame.quit()
