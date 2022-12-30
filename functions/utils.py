"""
various functions for the engines
"""

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