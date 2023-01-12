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

def get_info():
    """
    get the info to build a model
    """
    scaling_factor = (float(input("What do you want the scaling factor for the speed to be? ")))
    n = int(input("how many particles do you need? "))
    particlesComponents = []
    i = 0
    while i< n :
        try:
            string = 'number {}: type 0 for proton, 1 for electron '.format(str(i + 1))
            particleType = int(input(string))
            xSpeed = float(input("what's its speed on the x axis? "))
            ySpeed = float(input("what's its speed on the y axis? "))
            xPosition = int(input("And what's its x coordinate? "))
            yPosition = int(input("Finally, what's its y coordinate? "))

            if particleType == 1 or particleType == 0:
                particlesComponents.append([particleType, (xPosition, yPosition), (xSpeed, ySpeed)])
                i += 1
            else:
                print("Bad input: retry")
        except:
                print("Bad input: retry")
    return scaling_factor, particlesComponents

def load_configuration():
    """
    config format:
    title:particle1/particle2.../particlen
    """
    config = open("data/configurations.txt", 'r')

    #mapping the title of the configuration of particles to the specs
    print("CONFIGURATIONS:")
    configMap = dict()
    for line in config:
        data = line.split(':')
        configMap[data[0]] =  data[1].split('/')
        
    i = 0
    indexTitleMap = dict()
    for title, _ in configMap.items():
        indexTitleMap[i] = title
        print("{}: {}".format(i, title))
        i += 1
    
    print('*'*15)
    confIndex = int(input("what configuration do you want to load? (type the number in) "))

    try:
        particles = configMap[indexTitleMap[confIndex]]
    except:
        raise IndexError("value must be one among the previously listed")

    particlesComponents= []
    for particleSpecs in particles:
        particleSpecs = particleSpecs.split(',')
        refinedSpecs = [
            int(particleSpecs[0]), 
            (int(particleSpecs[1]), int(particleSpecs[2])), 
            (int(particleSpecs[3]), int(particleSpecs[4]))
            ]
        particlesComponents.append(refinedSpecs)
    
    scaling_factor = 1

    return scaling_factor, particlesComponents

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

