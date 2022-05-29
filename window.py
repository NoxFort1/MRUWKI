import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1600, 800))
pygame.display.set_caption('Symulator')
clock = pygame.time.Clock()

background_surface = pygame.image.load('graphics/background.jpg').convert()

ant_surface = pygame.image.load('graphics/antmodel.png').convert_alpha()
ant_x_pos = 0
ant_vel = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    screen.blit(ant_surface, (ant_x_pos, 0))
    ant_x_pos += ant_vel
    if ant_x_pos >= 1600:
        ant_x_pos = 0
    pygame.display.update()
    clock.tick(60)