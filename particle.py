#define the particle object
import pygame

class Particle():

    def __init__(self, surface, position: tuple, speed: tuple, acceleration=(0,0)) -> None:
        import decimal

        self.surface = surface
        self.position = (decimal.Decimal(position[0]), decimal.Decimal(position[1])) #m
        self.speed = (decimal.Decimal(speed[0]), decimal.Decimal(speed[1])) #m/s
        self.acceleration = (decimal.Decimal(acceleration[0]), decimal.Decimal(acceleration[1]))#m/s^2

        self.color = (255, 255, 255)
        self.radius = 5.0

    def move(self):
        self.speed = (self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1])
        self.position = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])
    
    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.position, self.radius, 0)

    def __repr__(self) -> str:
        return "mass: {} Kg\ncharge: {} C\nPosition: {}x, {}y\nSpeed: {}x, {}y".format(self.mass, self.charge, self.position[0], self.position[1], self.speed[0], self.position[1])
        


class Electron(Particle):

    def __init__(self, surface, position: tuple, speed: tuple) -> None:
        super().__init__(surface, position, speed, acceleration=(0,0))
        import decimal

        self.charge = decimal.Decimal('-1.60e-19') #C
        self.mass =  decimal.Decimal('9.11e-31') #Kg
        self.color = (0, 0, 255)
        self.radius = 3.0

class Proton(Particle):

    def __init__(self, surface, position: tuple, speed: tuple) -> None:
        super().__init__(surface, position, speed, acceleration=(0,0))
        import decimal

        self.charge = decimal.Decimal('1.60e-19') #C
        self.mass = decimal.Decimal('1.67e-27') #Kg
        self.color = (255, 0, 0)
        self.radius = 5.5
    
