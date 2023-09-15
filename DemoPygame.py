import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
f = False
while not f:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            f = True  
    pygame.display.flip()
