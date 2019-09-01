import pygame
from time import sleep
import socket
from single_player.network import Network

# create dict of each card image
deck_dict = {}
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['C', 'D', 'H', 'S']
suit_map = {'C': '\u2663','D': '\u2666','H': '\u2665','S': '\u2660'}
for rank in ranks:
    for s in suits:
        card_key = rank + suit_map[s]
        card_file = "cards_jpeg\\" + rank + s + ".jpg"
        my_card = pygame.transform.scale(pygame.image.load(card_file),(100,155))
        deck_dict[card_key] = my_card
deck_dict['BJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\BJo.jpg"),(100,155))
deck_dict['SJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\SJo.jpg"),(100,155))

card_back_vert = pygame.transform.scale(pygame.image.load("cards_jpeg\\Red_back.jpg"),(65,100))
card_back_hor = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards_jpeg\\Red_back.jpg"),(65,100)),90)

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
        self.data = []
        
    def draw_board(self):
        pass
    '''
    def draw_hands(self):
        pass
        # draws all hands with only your own showing
        # gets hands of all players
        player_hands = []
        for player in r.get_players():
            player_hand_cards = player.get_hand()
            player_hand = []
            for raw_card in player_hand_cards:
                player_hand.append(str(raw_card))
            player_hands.append(player_hand)
        user_hand = player_hands[self.playerID % 4]
        right_hand = player_hands[(self.playerID + 1) % 4]
        across_hand = player_hands[(self.playerID + 2) % 4]
        left_hand = player_hands[(self.playerID + 3) % 4]

        # draws user's hand
        left_coord = 450 - (22*(len(user_hand)-1)+100)/2
        for card_index in range(len(user_hand)):
            if card_index < len(user_hand) - 1:
                self.screen.blit(deck_dict[user_hand[card_index]], [left_coord+22*(card_index), 445], area=pygame.Rect(0, 0, 22, 155), special_flags=0)
            else:
                self.screen.blit(deck_dict[user_hand[card_index]], [left_coord+22*(card_index), 445], area=None, special_flags=0)
            card_index += 1

        # draws across hand
        left_coord = 450 - (15*(len(across_hand))-1+65)/2
        for card_index in range(len(across_hand)):
            if card_index < len(across_hand) - 1:
                self.screen.blit(card_back_vert, [left_coord + 15 * (card_index), 0],
                             area=pygame.Rect(0, 0, 15, 100), special_flags=0)
            else:
                self.screen.blit(card_back_vert, [left_coord + 15 * (card_index), 0],
                                 area=None, special_flags=0)
            card_index += 1

        # draws left hand
        left_coord = 250 - (15*(len(left_hand))-1+65)/2
        for card_index in range(len(left_hand)):
            if card_index < len(left_hand) - 1:
                self.screen.blit(card_back_hor, [0, left_coord + 15 * (card_index)],
                             area=pygame.Rect(0, 0, 100, 15), special_flags=0)
            else:
                self.screen.blit(card_back_hor, [0, left_coord + 15 * (card_index)],
                                 area=None, special_flags=0)
            card_index += 1

        # draws right hand
        left_coord = 250 - (15 * (len(right_hand)) - 1 + 65) / 2
        for card_index in range(len(right_hand)):
            if card_index < len(right_hand) - 1:
                self.screen.blit(card_back_hor, [800, left_coord + 15 * (card_index)], area=pygame.Rect(0, 0, 100, 15), special_flags=0)
            else:
                self.screen.blit(card_back_hor, [800, left_coord + 15 * (card_index)], area=None, special_flags=0)
            card_index += 1
    '''
    def draw_deck(self):
        pass

    def update(self):
        # make the game 60 fps
        self.clock.tick(60)

        # clear the screen
        self.screen.fill(0)

        reply = self.net.send("x")
        print(reply)

        # draws board over cleared screen
        self.draw_board()

        # take input
        click = ''
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                global client_conns
                client_conns[self.playerID].close()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                click = event.pos

        print(click)

        # update the screen
        pygame.display.flip()

    def send_data(self):
        data = "indices"
        reply = self.net.send(data)
        return reply

    def click_index(self,position):
        pass

myClient = TractorClient()
while 1:
    myClient.update()
