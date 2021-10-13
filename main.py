import pygame

pygame.init()

#colors:
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

#scale factor:
sf = 35

#zone radius:
radius = 10000 / sf

#runway dimensions:
width = 100/sf
length = 500/sf
seperation = 500/sf

size = [radius*2,radius*2]
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

    #draw traffic control zone:
    pygame.draw.circle(screen, RED, (radius,radius), radius, 2)

    #draw runways:
    pygame.draw.rect(screen, BLACK, ((radius - (seperation/2)), (radius + (length/2)),width, length))
    pygame.draw.rect(screen, BLACK, ((radius + (seperation/2)), (radius + (length/2)),width, length))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()