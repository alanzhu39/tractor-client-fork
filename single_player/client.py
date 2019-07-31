import pygame

class TractorClient():
    def __init__(self):
        
        pygame.init()
        width, height = 900,600
        
        #initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tractor")
        
        #initialize pygame clock
        self.clock=pygame.time.Clock()
        
    def update(self):
        #sleep to make the game 60 fps
        self.clock.tick(60)

        #clear the screen
        self.screen.fill(0)

        for event in pygame.event.get():
            #quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        #update the screen
        pygame.display.flip()

myClient = TractorClient()
while 1:
    myClient.update()
