import pygame
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep

class TractorClient(ConnectionListener):

    def initGraphics(self):
        # creates surface from uploaded card image
        self.testCard = pygame.transform.scale(pygame.image.load("C:\\Users\\Alan Zhu\\Documents\\GitHub\\tractor-client\\single_player\\cards_jpeg\\2C.jpg"),(66,101))
        
    def __init__(self):
        
        pygame.init()
        width, height = 900,600
        
        # initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tractor")
        
        # initialize pygame clock
        self.clock=pygame.time.Clock()
        self.initGraphics()
        
        self.Connect()
        
    def drawBoard(self):
        # draws card on screen
        self.screen.blit(self.testCard, [0,0])
        
    def update(self):
        # make the game 60 fps
        self.clock.tick(60)

        connection.Pump()
        self.Pump()

        # clear the screen
        self.screen.fill(0)

        # draws board over cleared screen
        self.drawBoard()

        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()

        # update the screen
        pygame.display.flip()

myClient = TractorClient()
while 1:
    myClient.update()
