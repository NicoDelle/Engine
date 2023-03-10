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
    from functions import config

    #PROGRAM PARAMETERS
    FPS = 60

    #ENGINE PARAMETERS
    newConf = int(input("Do you want to load an existing configuration or do you want to build a new one? [0 -> load one /  1 -> create new] "))
    if newConf:
        scaling_factor, particlesComponents = config.get_info()
    else:
        scaling_factor, particlesComponents = config.load_configuration()

    engine = engine.SimpleInteraction(surface, particlesComponents)
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

    if newConf:
        save_conf = input("Do you want to save the configuration? [Y/n]")
        if save_conf.lower() in ["yes", "y", ""]:
            config.save_config(particlesComponents)

    pygame.quit()

if __name__ == "__main__":
    main()