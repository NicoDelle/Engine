class Engine():

    def __init__(self, surface) -> None:
        """
        Initializes the particles in the engine. It needs a pygame surface object on which to draw particles.
        This empty class serves only as a backbone to more elavorate engines
        """

        self.surface = surface
        self.size = self.surface.get_size()
