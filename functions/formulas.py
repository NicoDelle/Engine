def electrical_force(particle1, particle2):

    import math, decimal

    xDistance = decimal.Decimal(particle1.position[0]) - decimal.Decimal(particle2.position[0])
    yDistance = decimal.Decimal(particle1.position[1]) - decimal.Decimal(particle2.position[1])
    distance = decimal.Decimal(math.sqrt(xDistance**2 + yDistance**2))

    if xDistance:
        angle1 = decimal.Decimal(math.atan(yDistance / xDistance))
    else:
        angle1 = decimal.Decimal(math.pi / 2)
        
    force = decimal.Decimal(
        (abs(particle1.charge * particle2.charge) * decimal.Decimal('10e12')) / (decimal.Decimal('111.16') * (distance**2))
        )

    xForce = force * decimal.Decimal(math.cos(angle1))
    yForce = force * decimal.Decimal(math.sin(angle1))
    

    return (xForce, yForce)