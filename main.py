#Third party
import pygame
print("ma che cazzo")

#personal
import drawings

#<------------------------------>
#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#SURFACE PARAMETERS
bgColor = BLACK
size = (900, 600)

#<------------------------------>

print("wtf?")
pygame.init()
surface = drawings.setSurface(size, bgColor)

def main():
    #imports
    from engines import twoParticles as engine

    #PROGRAM PARAMETERS
    FPS = 60

    #ENGINE PARAMETERS
    n = int(input("how many particles do you need? "))
    partMap = dict()
    i = 0
    while i< n :
        try:
            string = 'number {}: type 0 for proton, 1 for electron '.format(str(i + 1))
            part = int(input(string))
            xSpeed = float(input("what's its speed on the x axis? "))
            ySpeed = float(input("what's its speed on the y axis? "))
            xPosition = int(input("And what's its x coordinate? "))
            yPosition = int(input("Finally, what's its y coordinate? "))

            if part == 1 or part == 0:
                partMap[i] = [part, (xSpeed, ySpeed), (xPosition, yPosition)]
                i += 1
            else:
                print("Bad input: retry")
        except:
                print("Bad input: retry")

    engine = engine.SimpleInteraction(surface, partMap)
    engine.scale_speed(3)
    clock = pygame.time.Clock()
    
    run = True
    while run:
        
        surface.fill(BLACK)

        engine.run()

        clock.tick(FPS)
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()