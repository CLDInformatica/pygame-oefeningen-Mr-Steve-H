'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Eerste game!')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((800, 400))
surface.fill("blue")
pipe1 = pygame.Surface((50, 200))
pipe1.fill('Green')
pipe2 = pygame.Surface((50, 100))
pipe2.fill('Green')
pipe3 = pygame.Surface((50, 250))
pipe3.fill('Green')
pipe4 = pygame.Surface((50, 50))
pipe4.fill('Green')
pipe5 = pygame.Surface((50, 50))
pipe5.fill('Green')
pipe6 = pygame.Surface((50, 250))
pipe6.fill('Green')
flappy = pygame.Surface((20, 20))
flappy.fill('Yellow')

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(surface, (0, 0))
  screen.blit(pipe1, (200, 0))
  screen.blit(pipe2, (200, 300))
  screen.blit(pipe3, (400, 0))
  screen.blit(pipe4, (400, 350))
  screen.blit(pipe5, (600, 0))
  screen.blit(pipe6, (600, 150))
  screen.blit(flappy, (100, 200))

  
  pygame.display.update()
  clock.tick(60)
  