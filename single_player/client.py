import pygame
from time import sleep
import socket
from single_player.network import Network
from single_player.round import *
from single_player.player import *

sheng_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_ids = [0, 0, 0, 0]

zj_id = 0
players = [Player("Adam", sheng_order[0]), Player("Andrew", sheng_order[0]),
           Player("Alan", sheng_order[0]), Player("Raymond", sheng_order[0])]
players[zj_id].set_is_zhuang_jia(True)

class TractorClient():

    def initGraphics(self):
        # creates surface from uploaded card image
        self.testCard = pygame.transform.scale(pygame.image.load("cards_jpeg\\2C.jpg"),(66,101))
        
    def __init__(self):
        
        pygame.init()
        width, height = 900,600
        
        # initialize the screen
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tractor")
        
        # initialize pygame clock
        self.clock=pygame.time.Clock()
        self.initGraphics()
        self.net = Network()
        self.playerID = self.net.getID()
        
    def drawBoard(self):
        # draws card on screen
        self.screen.blit(self.testCard, [0,0])

    def drawHands(self):
        # draws all hands with only your own showing
        pass

    def update(self):
        # make the game 60 fps
        self.clock.tick(60)

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
