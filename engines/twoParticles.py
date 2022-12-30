from .engine import Engine

class SimpleInteraction(Engine):


    def __init__(self, surface, parts: dict) -> None:
        """
        inits the particles as objects in a dictionary. it needs a dictionary containing the speed and the initial position associated with the kind of particle as an input 
        """

        import particle

        super().__init__(surface)

        #make a dict mapping an index to a particle object
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
        import decimal
        from functions import utils

        maxSpeed = utils.max_speed(self.particles.items())
        
        scaler = decimal.Decimal(maxSpeed / decimal.Decimal(scale_factor))

        for _, particle in self.particles.items():
            scaledVx = particle.speed[0] / scaler
            scaledVy = particle.speed[1] / scaler
            particle.speed = (scaledVx, scaledVy)
        
        return scaler
    
    def interactions(self, scaler):

        from functions import formulas
        
        for key1, particle1 in self.particles.items():
            key2 = key1 + 1

            if key2 >= len(self.particles.items()):
                break
            
            while key2 < len(self.particles.items()):
                particle2 = self.particles[key2]

                force = formulas.electrical_force(particle1, particle2)

                if particle1.charge * particle2.charge < 0:
                    force1 = force
                    force2 = (-force[0], -force[1])
                else:
                    force1 = (-force[0], -force[1])
                    force2 = force
                    
                xAcc1 = (force1[0] / particle1.mass) / scaler
                yAcc1 = (force1[1] / particle1.mass) / scaler
                xAcc2 = (force2[0] / particle2.mass) / scaler
                yAcc2 = (force2[1] / particle2.mass) / scaler
                
                particle1.acceleration = (particle1.acceleration[0] + xAcc1, particle1.acceleration[1] + yAcc1)
                particle2.acceleration = (particle2.acceleration[0] + xAcc2, particle2.acceleration[1] + yAcc2)

                key2 += 1 



    def run(self, scaler):
        for _, particle in self.particles.items():
            particle.draw()
        for _, particle in self.particles.items():
            self.interactions(scaler)
            particle.move()
