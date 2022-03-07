#alex -2 Watching videos in class
#Angel -1 
#Jonathan -1
import pygame, sys
from sys import exit

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Whatever")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,50))
test_surface.fill('Blue')
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  clock.tick(60)
  #Draw things
  screen.blit(test_surface, (50,50))
  #update Everything
  pygame.display.update()