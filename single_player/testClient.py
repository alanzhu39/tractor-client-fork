import pygame
import single_player.round_copy as myConns
from time import sleep
import socket
from single_player.network import Network

class TractorClient():

    def initGraphics(self):
        pass

    def __init__(self):

        pygame.init()
        width, height = 900,600

        # initialize the screen
        self.screen = pygame.display.set_mode((width, height))

        # initialize pygame clock
        self.clock=pygame.time.Clock()
        self.initGraphics()
        pygame.display.set_caption("Client -1")
        self.data = None
        self.card_indices = []

    def draw_stats(self):
        pass
        # draws score, trump suit
        white = (255, 255, 255)
        my_font = pygame.font.SysFont('comicsansms', 20)
        score = my_font.render('Score: ', True, white)
        trump = my_font.render('Trump: ', True, white)
        self.screen.blit(score, [110, 0])
        self.screen.blit(trump, [110, 20])

    def update(self):
        # make the game 60 fps
        self.clock.tick(60)

        # clear the screen
        self.screen.fill(0)

        # draws board over cleared screen
        self.draw_stats()

        # take input
        click = None
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                click = event.pos

        # update the screen
        pygame.display.flip()

while 1:
    myClient = TractorClient()
    myClient.update()