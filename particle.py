#define the particle object
import pygame

class Particle():

    def __init__(self, surface, position: tuple, speed: tuple, acceleration=(0,0)) -> None:
        self.surface = surface
        self.position = position
        self.speed = speed
        self.acceleration = acceleration

        self.color = (255, 255, 255)
        self.radius = 5.0

    def move(self):
        self.speed = (self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1])
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
    
