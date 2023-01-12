"""
various functions for the engines
"""
def addToPartMap(surface, particleSpecs: list) -> dict:
    """
    creates a particle object given a list of specs in the following format: [particle type, (particle speed), (particle position)]
    it doesn't support passing the acceleration (yet)
    """

    import particle

    particle_type = particleSpecs[0]
    position = particleSpecs[1]
    speed = particleSpecs[2]
    if particle_type:
        return particle.Electron(surface, position, speed)
    else:
        return particle.Proton(surface, position, speed)


def max_speed(particles):
    """
    finds the maximum speed among all the components in a dict with particle objects
    """
    maxSpeed = 1
    for _, particle in particles:
        xSpeed = particle.speed[0]
        ySpeed = particle.speed[1]
        if xSpeed > maxSpeed:
            maxSpeed = xSpeed
        if ySpeed > maxSpeed:
            maxSpeed = ySpeed
    return maxSpeed
