#Third party
import pygame

#personal
import functions.drawings as drawings

#<------------------------------>
#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#SURFACE PARAMETERS
bgColor = BLACK
size = (900, 600)

#<------------------------------>

pygame.init()
surface = drawings.setSurface(size, bgColor)

def main():
    #imports
    from engines import twoParticles as engine

    #PROGRAM PARAMETERS
    FPS = 60

    #ENGINE PARAMETERS
    scaling_factor = (float(input("What do you want the scaling factor for the speed to be? ")))
    n = int(input("how many particles do you need? "))
    partMap = dict()
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
                partMap[i] = [particleType, (xSpeed, ySpeed), (xPosition, yPosition)]
                i += 1
            else:
                print("Bad input: retry")
        except:
                print("Bad input: retry")

    engine = engine.SimpleInteraction(surface, partMap)
    scaler = engine.scale_speed(scaling_factor)
    clock = pygame.time.Clock()
    
    run = True
    while run:
        
        surface.fill(BLACK)

        engine.run(scaler)

        clock.tick(FPS)
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()