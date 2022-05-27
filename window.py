import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Symulator')
clock = pygame.time.CLock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)