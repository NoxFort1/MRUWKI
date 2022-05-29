import pygame
from models import x_pos, y_pos
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Symulator')
clock = pygame.time.Clock()

background_surface = pygame.image.load('graphics/background.jpg').convert()

ant_surface = pygame.image.load('graphics/antmodel.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    for i in range (50):
        screen.blit(ant_surface, (x_pos[i], y_pos[i]))
    pygame.display.update()
    clock.tick(60)