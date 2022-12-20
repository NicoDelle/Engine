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
            if item[0]:
                self.particles[n] = particle.Electron(self.surface, item[1][1], item[1][0])
            else:
                self.particles[n] = particle.Proton(self.surface, item[1][1], item[1][0])
                n += 1

    def run(self):
        for key, particle in self.particles.items():
            particle.draw()
        for key, particle in self.particles.items():
            particle.move_linear()
