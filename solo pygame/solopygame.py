import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Solo pygame')
clock = pygame.time.Clock()
running = True

achtergrond = pygame.Surface((1000,500))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(achtergrond, (0,0))

    pygame.display.update()
    clock.tick(60)
