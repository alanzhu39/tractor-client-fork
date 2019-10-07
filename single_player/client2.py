import pygame
import single_player.round_copy as myConns
from time import sleep
import socket
from single_player.network import Network

# create dict of each card image
deck_dict = {}
small_deck_dict = {}
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['C', 'D', 'H', 'S']
suit_map = {'C': '\u2663','D': '\u2666','H': '\u2665','S': '\u2660'}
for rank in ranks:
    for s in suits:
        card_key = rank + suit_map[s]
        card_file = "cards_jpeg\\" + rank + s + ".jpg"
        my_card = pygame.transform.scale(pygame.image.load(card_file),(100,155))
        deck_dict[card_key] = my_card
        my_card = pygame.transform.scale(pygame.image.load(card_file), (65, 100))
        small_deck_dict[card_key] = my_card
deck_dict['BJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\BJo.jpg"),(100,155))
deck_dict['SJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\SJo.jpg"),(100,155))
small_deck_dict['BJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\BJo.jpg"),(65,100))
small_deck_dict['SJo'] = pygame.transform.scale(pygame.image.load("cards_jpeg\\SJo.jpg"),(65,100))

card_back_vert = pygame.transform.scale(pygame.image.load("cards_jpeg\\Red_back.jpg"),(65,100))
card_back_hor = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("cards_jpeg\\Red_back.jpg"),(65,100)),90)
play_btn = pygame.transform.scale(pygame.image.load("cards_jpeg\\play_button.jpg"),(120,65))
clear_btn = pygame.transform.scale(pygame.image.load("cards_jpeg\\clear_button.jpg"),(120,65))

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
        self.net = Network()
        self.playerID = int(self.net.getID())
        pygame.display.set_caption("Client " + str(self.playerID))
        self.data = None
        self.card_indices = []

    def draw_board(self):
        self.draw_hands()
        self.draw_cleared()
        self.draw_deck()
        self.draw_buttons()
        self.draw_stats()

    def draw_stats(self):
        pass
        # draws score, trump suit
        white = (255, 255, 255)
        my_font = pygame.font.SysFont('comicsansmc', 20)
        score = my_font.render('Score: ' + self.data[15], True, white)
        trump = my_font.render('Trump: ' + self.data[16], True, white)
        self.screen.blit(score, [110, 5])
        self.screen.blit(trump, [110, 25])


    def draw_hands(self):
        pass
        # draws all hands with only your own showing
        # gets hands of all players
        player_hands = []
        played_cards = []
        for i in range(4):
            player_hands.append(self.data[i*3 + 1])
            played_cards.append(self.data[i*3 + 2])
        user_hand = player_hands[self.playerID % 4]
        right_hand = player_hands[(self.playerID + 1) % 4]
        across_hand = player_hands[(self.playerID + 2) % 4]
        left_hand = player_hands[(self.playerID + 3) % 4]
        user_played = played_cards[self.playerID % 4]
        right_played = played_cards[(self.playerID + 1) % 4]
        across_played = played_cards[(self.playerID + 2) % 4]
        left_played = played_cards[(self.playerID + 3) % 4]

        if len(user_hand) > 0:
            # draws user's hand
            left_coord = 450 - (22*(len(user_hand)-1)+100)/2
            for card_index in range(len(user_hand)):
                if card_index < len(user_hand) - 1:
                    self.screen.blit(deck_dict[user_hand[card_index]], [left_coord+22*(card_index), 445], area=pygame.Rect(0, 0, 22, 155), special_flags=0)
                else:
                    self.screen.blit(deck_dict[user_hand[card_index]], [left_coord+22*(card_index), 445], area=None, special_flags=0)
                card_index += 1
        if len(across_hand) > 0:
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
        if len(left_hand) > 0:
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
        if len(right_hand) > 0:
            # draws right hand
            left_coord = 250 - (15 * (len(right_hand)) - 1 + 65) / 2
            for card_index in range(len(right_hand)):
                if card_index < len(right_hand) - 1:
                    self.screen.blit(card_back_hor, [800, left_coord + 15 * (card_index)], area=pygame.Rect(0, 0, 100, 15), special_flags=0)
                else:
                    self.screen.blit(card_back_hor, [800, left_coord + 15 * (card_index)], area=None, special_flags=0)
                card_index += 1
        if len(user_played) > 0:
            # draw played cards
            # draws user's played cards
            left_coord = 450 - (15 * (len(user_played) - 1) + 100) / 2
            for card_index in range(len(user_played)):
                if card_index < len(user_played) - 1:
                    self.screen.blit(small_deck_dict[user_played[card_index]], [left_coord + 15 * (card_index), 338],
                                     area=pygame.Rect(0, 0, 15, 100), special_flags=0)
                else:
                    self.screen.blit(small_deck_dict[user_played[card_index]], [left_coord + 15 * (card_index), 338], area=None,
                                     special_flags=0)
                card_index += 1
        if len(across_played) > 0:
            # draws across player's played cards
            left_coord = 450 - (15 * (len(across_played)) - 1 + 65) / 2
            for card_index in range(len(across_played)):
                if card_index < len(across_played) - 1:
                    self.screen.blit(small_deck_dict[across_played[card_index]], [left_coord + 15 * (card_index), 107],
                                     area=pygame.Rect(0, 0, 15, 100), special_flags=0)
                else:
                    self.screen.blit(small_deck_dict[across_played[card_index]], [left_coord + 15 * (card_index), 107],
                                     area=None, special_flags=0)
                card_index += 1
        if len(left_played) > 0:
            # draws left player's played cards
            left_coord = 108
            for card_index in range(len(left_played)):
                if card_index < len(left_played) - 1:
                    self.screen.blit(small_deck_dict[left_played[card_index]], [left_coord + 15 * (card_index), 222],
                                     area=pygame.Rect(0, 0, 15, 100), special_flags=0)
                else:
                    self.screen.blit(small_deck_dict[left_played[card_index]], [left_coord + 15 * (card_index), 222],
                                     area=None, special_flags=0)
                card_index += 1
        if len(right_played) > 0:
            # draws right player's played cards
            left_coord = 792 - (15 * (len(right_played)) - 1 + 65)
            for card_index in range(len(right_played)):
                if card_index < len(right_played) - 1:
                    self.screen.blit(small_deck_dict[right_played[card_index]], [left_coord + 15 * (card_index), 222],
                                     area=pygame.Rect(0, 0, 15, 100), special_flags=0)
                else:
                    self.screen.blit(small_deck_dict[right_played[card_index]], [left_coord + 15 * (card_index), 222], area=None, special_flags=0)
                card_index += 1

    def draw_deck(self):
        if self.data[13] == 'True':
            self.screen.blit(card_back_vert, [35,481])

    def draw_cleared(self):
        if self.data[12] == 'True':
            self.screen.blit(card_back_vert, [417,222])

    def draw_buttons(self):
        self.screen.blit(play_btn, [772,465])
        self.screen.blit(clear_btn, [772,532])

    def update(self):
        # make the game 60 fps
        self.clock.tick(60)

        # clear the screen
        self.screen.fill(0)

        # draws board over cleared screen
        self.draw_board()

        # take input
        click = None
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                myConns.connections[self.playerID].close()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                click = event.pos

        self.data = self.parse_data(self.send_data(click))

        # update the screen
        pygame.display.flip()

    def send_data(self, position):
        reply = None
        if not position:
            return self.net.send('x')
        player_hand = self.data[self.playerID * 3 + 1]
        left_offset = (22 * (len(player_hand) - 1) + 100) / 2
        if position[1] >= 445 and 450 - left_offset < position[0] < 450 + left_offset:
            # card click
            click_index = min(len(player_hand) - 1, int((position[0] - (450 - left_offset)) // 22))
            self.card_indices.append(click_index)
            print(self.card_indices)
            reply = self.net.send('x')
        elif 772 <= position[0] <= 892 and 465 <= position[1] <= 530:
            # play button press
            if not self.card_indices:
                reply = self.net.send('x')
            else:
                reply = self.net.send(str(self.card_indices))
            print('play')
            self.card_indices.clear()
        elif 772 <= position[0] <= 892 and 532 <= position[1] <= 597:
            # clear button press
            self.card_indices.clear()
            print('clear')
            reply = self.net.send('x')
        else:
            reply = self.net.send('x')
        return reply

    def parse_data(self, response):
        if not response:
            return self.data
        data = [0,None,None,1,None,None,2,None,None,3,None,None,None,None,None,None,None]
        split_data = response.split(':')
        data[1] = self.make_list(split_data[1])
        data[2] = self.make_list(split_data[2])
        data[4] = self.make_list(split_data[4])
        data[5] = self.make_list(split_data[5])
        data[7] = self.make_list(split_data[7])
        data[8] = self.make_list(split_data[8])
        data[10] = self.make_list(split_data[10])
        data[11] = self.make_list(split_data[11])
        data[12] = str(split_data[12])
        data[13] = str(split_data[13])
        data[14] = str(split_data[14])
        data[15] = str(split_data[15])
        data[16] = str(split_data[16])
        return data

    def make_list(self, list_in):
        list_out = list_in.strip('[').strip(']')
        list_out = [s.strip() for s in list_out.split(',') if s != '']
        return list_out

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

myClient = TractorClient()
'''
while True:
    for event in pygame.event.get():
        # quit if the quit button was pressed
        if event.type == pygame.QUIT:
            exit()
    if not myClient.get_data():
        myClient.set_data(myClient.parse_data(myClient.send_data((0,0))))
        continue
    break
print('starting game')
'''
while 1:
    if myClient.get_data() and myClient.get_data()[14] == "True":
        myClient.update()
    else:
        for event in pygame.event.get():
            # quit if the quit button was pressed
            if event.type == pygame.QUIT:
                exit()
        myClient.set_data(myClient.parse_data(myClient.send_data(None)))

