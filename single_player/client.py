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

r = Round(players)

# create dict of each card image
deck_dict = {}
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['C', 'D', 'H', 'S']
suit_map = {'C': 'clubs','D': 'diamonds','H': 'hearts','S': 'spades'}
for rank in ranks:
    for s in suits:
        card_key = rank + suit_map[s]
        card_file = "cards_jpeg\\" + rank + s + ".jpg"
        deck_dict[card_key] = pygame.transform.scale(pygame.image.load(card_file),(70,110))
deck_dict['BJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\BJo.jpg"),(70,110))
deck_dict['SJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\SJo.jpg"),(70,110))

class TractorClient():

    def initGraphics(self):
        pass

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
        self.playerID = int(self.net.getID())
        
    def drawBoard(self):
        self.drawHands()

    def drawHands(self):
        pass
        # draws all hands with only your own showing
        # gets hands of all players
        player_hands = []
        for player in r.get_players():
            player_hand_cards = player.get_hand()
            player_hand = []
            for raw_card in player_hand_cards:
                if raw_card.get_is_big_joker:
                    player_hand.append("BJo")
                elif raw_card.get_is_small_joker:
                    player_hand.append("SJo")
                else:
                    parsed_card = raw_card.get_rank() + raw_card.get_suit()
                    player_hand.append(parsed_card)
            player_hands.append(player_hand)
        user_hand = player_hands[self.playerID]
        print(user_hand)
        right_hand = player_hands[(self.playerID + 1) % 4]
        across_hand = player_hands[(self.playerID + 2) % 4]
        left_hand = player_hands[(self.playerID + 3) % 4]

        # draws user's hand
        left_coord = 450 - (18*(len(user_hand)-1)+70)/2
        for card_index in range(len(user_hand)):
            if card_index < len(user_hand) - 1:
                self.screen.blit(deck_dict[user_hand[card_index]], [left_coord+18*(card_index), 490], area=pygame.Rect(0, 0, 18, 110), special_flags=0)
            else:
                self.screen.blit(deck_dict[user_hand[card_index]], [left_coord+18*(card_index), 490], area=None, special_flags=0)
            card_index += 1

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
r.deal()
while 1:
    myClient.update()
