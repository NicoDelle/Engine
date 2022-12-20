#Third party
import pygame

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

pygame.init()
surface = drawings.setSurface(size, bgColor)

def main():
    from engines import twoParticles as engine

    position = (10, 300)
    FPS = 60

    n = int(input("how many particles do you need? "))

    partMap = dict()
    i = 0
    while i< n :
        string = 'number {}: type 0 for proton, 1 for electron '.format(str(i + 1))
        part = int(input(string))
        xSpeed = int(input("what's its speed on the x axis? "))
        ySpeed = int(input("what's its speed on the y axis? "))
        xPosition = int(input("And what's its x coordinate? "))
        yPosition = int(input("Finally, what's its y coordinate? "))

        if part == 1 or part == 0:
            partMap[part] = [(xSpeed, ySpeed), (xPosition, yPosition)]
            i += 1
        else:
            print("Bad input: retry")


    engine = engine.SimpleInteraction(surface, partMap)
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