import pygame
import generate_planes

pygame.init()

#colors:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#scale factor:
sf = 35

#zone radius:
global radiusZ 
radiusZ = 10000 / sf

#hold pattern radius:
radiusH = 1000 / sf

#runway dimensions:
width = 100 / sf
length = 500 / sf
seperation = 500 / sf
numRunways = 2

#speed of plane
v = 140 / sf

#frequency of transmission
freq = 10 #Hz

#safe distance between planes
safeDistance = 100 / sf

size = [radiusZ*2,radiusZ*2]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Traffic Control")

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    #logic goes here:

    #drawings:
    screen.fill(WHITE)

    #draw traffic control zone as a circle:
    pygame.draw.circle(screen, RED, (radiusZ,radiusZ), radiusZ, 2)

    #draw runways as rectangles:
    pygame.draw.rect(screen, BLACK, ((radiusZ - (seperation/2)), (radiusZ + (length/2)),width, length))
    pygame.draw.rect(screen, BLACK, ((radiusZ + (seperation/2)), (radiusZ + (length/2)),width, length))

    #draw airplanes as points:
    pygame.draw.line(screen, GREEN, (generate_planes.generatePlane(radiusZ)), (generate_planes.generatePlane(radiusZ)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()