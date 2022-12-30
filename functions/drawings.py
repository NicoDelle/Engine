import pygame
pygame.init()

def setSurface(size, color):
    surface = pygame.display.set_mode(size)
    surface.fill(color)

    return surface

