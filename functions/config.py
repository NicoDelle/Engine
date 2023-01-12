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
        title, scaling_factor = data[0].split(',')
        configMap[title] =  data[1].split('/')
        
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
    
    return scaling_factor, particlesComponents

def save_config(particlesComponents):
    pass