from .engine import Engine

class SimpleInteraction(Engine):


    def __init__(self, surface, parts: dict) -> None:
        """
        inits the particles as objects in a dictionary. it needs a dictionary containing the speed and the initial position associated with the kind of particle as an input 
        """

        import particle

        super().__init__(surface)

        self.particles = dict()
        n = 0
        for item in parts.items():
            particle_type = item[1][0]
            speed = item[1][1]
            position = item[1][2]
            if particle_type:
                self.particles[n] = particle.Electron(self.surface, position, speed)
            else:
                self.particles[n] = particle.Proton(self.surface, position, speed)
                n += 1
    
    def scale_speed(self, scale_factor):

        """
        method that retrieves the fastest particle (in modulus) and then divides the speed components of each particle by the components of the speed of said particle
        """

        import math

        maxSpeed = 0
        for _, particle in self.particles.items():
            xSpeed = particle.speed[0]
            ySpeed = particle.speed[1]
            if xSpeed > maxSpeed:
                maxSpeed = xSpeed
            if ySpeed > maxSpeed:
                maxSpeed = ySpeed
        
        scaler = maxSpeed / scale_factor

        for _, particle in self.particles.items():
            scaledVx = particle.speed[0] / scaler
            scaledVy = particle.speed[1] / scaler
            particle.speed = (scaledVx, scaledVy)


    def run(self):
        for _, particle in self.particles.items():
            particle.draw()
        for _, particle in self.particles.items():
            particle.move_linear()
