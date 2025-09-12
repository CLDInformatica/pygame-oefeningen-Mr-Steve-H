'''
Gegeven zijn: een horror font dat "voetbal game" op het scherm zet en een plaatje van een bal.

We gaan de game aanpassen zodat het er beter uit ziet.

Doe het volgende:

  - Download een toepasselijk font en maak hiermee een scoreboard
  - Download 2 plaatjes van voetballers en zet deze tegenover elkaar op het scherm
  - Zet de bal in het midden van de scherm

Extra tijd:

  - Voeg 2 goals toe (links en rechts)
  - Voeg een toepasselijke achtergrond toe
  - Schrijf de namen van de spelers ergens op het scherm

Slides: https://docs.google.com/presentation/d/1c4C94q8OcMGCIFefVo18Xac4WIFJacq5Eutj1gY6rCg/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Voetbal game!')
clock = pygame.time.Clock()
running = True
test_font = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/Voetbal.ttf", 50)

background = pygame.Surface((800, 400))
background.fill("Blue")
grass = pygame.Surface((800, 100))
grass.fill("Dark green")
voetbal_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/voetbal.png")
tekst_surface = test_font.render("Score", False, "brown")
score = test_font.render('0 | 0', False, 'white' )
goal = pygame.image.load("Opdrachten/PyGame/Les2/graphics/147630.svg")
Scale = (100, 150)
goal = pygame.transform.scale(goal, Scale)
goalflip = pygame.transform.flip(goal, True, False)
player = pygame.image.load("Opdrachten/PyGame/Les2/graphics/Character01.webp")
Scale1 = (75, 75)
player = pygame.transform.scale(player, Scale1)
player2 = pygame.transform.flip(player, True, False)

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(background, (0,0))
  screen.blit(grass, (0, 300))
  screen.blit(tekst_surface, (10, 10))
  screen.blit(voetbal_surface, (375, 325))
  screen.blit(score, (10, 60))
  screen.blit(goal, (700, 250))
  screen.blit(goalflip, (0, 250))
  screen.blit(player2, (100, 325))
  screen.blit(player, (625, 325))
  
  
  pygame.display.update()
  clock.tick(60)
