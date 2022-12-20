#define the particle object
import pygame

class Particle():

    def __init__(self, surface, position: tuple, speed: tuple) -> None:
        self.surface = surface
        self.position = position
        self.speed = speed
        self.color = (255, 255, 255)
        self.radius = 5.0

    def move_linear(self):
        self.position = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])
    
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.position, self.radius, 0)


class Electron(Particle):

    def __init__(self, surface, position: tuple, speed: tuple) -> None:
        super().__init__(surface, position, speed)
        self.charge = -1
        self.mass = 9.11
        self.color = (0, 0, 255)
        self.radius = 3.0

class Proton(Particle):

    def __init__(self, surface, position: tuple, speed: tuple) -> None:
        super().__init__(surface, position, speed)
        self.charge = 1
        self.mass = 16000
        self.color = (255, 0, 0)
        self.radius = 5.5
    
