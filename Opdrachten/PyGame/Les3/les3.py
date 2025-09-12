'''
Voeg de volgende 2 dingen aan de game toe:

  - Laat de auto aan de linkerkant van het scherm terugkomen als de auto aan de rechterkant van het scherm af rijdt HINT: Gebruik een ```if``` met daarin de ```x_pos```
  - Laat een aantal regendruppels van de bovenkant van het scherm naar beneden vallen

Slides: https://docs.google.com/presentation/d/16rz2C4Pqhx4YNCokEU_5mc3rtQXXNEoi7gFAGzv9s_A/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background_surface = pygame.Surface((800, 400))
background_surface.fill("white")

auto_surface = pygame.image.load("Opdrachten/PyGame/Les3/graphics/auto.png").convert_alpha()
auto_x_pos = 200

rain = pygame.image.load("Opdrachten/PyGame/Les3/graphics/purepng.com-raindropsnaturestylenaturalbeautifulgreen-541521126280eg699.png").convert_alpha()
Scale1 = (400, 200)
rain = pygame.transform.scale(rain, Scale1)
rain_y_pos = -200
rain_y_pos2 = 0
rain_y_pos3 = -200
rain_y_pos4 = 0
rain_y_pos5 = 200
rain_y_pos6 = 200

while running:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False

    screen.blit(background_surface, (0, 0))

    auto_x_pos += 1
    screen.blit(auto_surface, (auto_x_pos, 200))
    if auto_x_pos == 800:
      auto_x_pos = -200

    screen.blit(rain, (0, rain_y_pos))
    screen.blit(rain, (0, rain_y_pos2))
    screen.blit(rain, (400, rain_y_pos3))
    screen.blit(rain, (400, rain_y_pos4))
    screen.blit(rain, (0, rain_y_pos5))
    screen.blit(rain, (400, rain_y_pos6))

    rain_y_pos += 1
    rain_y_pos2 += 1
    rain_y_pos3 += 1
    rain_y_pos4 += 1
    rain_y_pos5 += 1
    rain_y_pos6 += 1

    if rain_y_pos == 400:
      rain_y_pos = -200
    if rain_y_pos2 == 400:
      rain_y_pos2 = -200
    if rain_y_pos3 == 400:
      rain_y_pos3 = -200
    if rain_y_pos4 == 400:
      rain_y_pos4 = -200
    if rain_y_pos5 == 400:
      rain_y_pos5 = -200
    if rain_y_pos6 == 400:
      rain_y_pos6 = -200

    pygame.display.update()
    clock.tick(60)