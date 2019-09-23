import pygame
import sys

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
isGaming = True
#主要循环
while isGaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

pygame.quit()
