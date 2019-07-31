'''
Keep track of:
everyone's cards
current Zhuang Jia
Zhuang Jia discard
current trump
current attacker's points

also play the round:
dealing, compare cards, and playing
'''
from single_player.deck import *
import single_player.player_input_methods as pim
from single_player.deck import Deck


class Round(object):
    '''
    player = list of Player (size = 4)
    '''
    num_di_pai = 8
    def __init__(self, players):
        self.deck = Deck()
        assert(len(players) == 4)
        self.players = players
        
        set_zhuang_jia = False
        for i in range(len(players)):
            if players[i].zhuang_jia:
                self.zhuang_jia_id = i
                set_zhuang_jia = True
        # draw for zhuang jia
        if not set_zhuang_jia:
            1

        self.trump_suit = "none"
        self.trump_suit_cnt = 0

    def deal(self):
        self.deck.shuffle()
        current_drawer = self.zhuang_jia_id
        while len(self.deck) > self.num_di_pai:
            self.players[current_drawer].draw(self.deck.pop())
            print(self.players[current_drawer].name)
            self.players[current_drawer].print_hand()
            self.liang_query(current_drawer)
            current_drawer = (current_drawer + 1) % 4
        if self.trump_suit == "none":
            self.flip_di_pai()
        self.choose_di_pai()


    def liang_query(self, current_drawer):
        # format is "suit cnt" or "SJo 2" or "BJo 2"
        print("Liang?")
        response = input().split()
        if len(response) == 0 or response[0] == "n" or response[0] == "no":
            print("No liang, continuing")
            return
        if len(response) != 2:
            print("invalid response, continuing")
            return
        if response[1] != "1" and response[1] != "2":
            print("invalid response, continuing")
            return
        if (response[0] == "SJo" or response[0] == "BJo") and response[1] == "2":
            new_trump_suit = "wu zhu"
            new_trump_suit_cnt = 3
        elif response[0] in Card.suit_map:
            new_trump_suit = response[0]
            new_trump_suit_cnt = int(response[1])
        else:
            print("invalid response, continuing")
            return
        if response[0] == "SJo":
            card_to_check = SMALL_JOKER
            cnt_to_check = 2
        elif response[0] == "BJo":
            card_to_check = BIG_JOKER
            cnt_to_check = 2
        else:
            card_to_check = Card(self.players[0].get_trump_rank(), new_trump_suit)
            cnt_to_check = new_trump_suit_cnt
        if new_trump_suit_cnt > self.trump_suit_cnt:
            if self.players[current_drawer].card_count(card_to_check) >= cnt_to_check:
                print("Set trump suit to: " + new_trump_suit)
                self.trump_suit = new_trump_suit
                self.trump_suit_cnt = new_trump_suit_cnt
            else:
                print("You don't have the cards necessary for that liang")
        

    # compare two cards
    def cmp_cards(a, b):
        1
    def play_turn(self):
        1

    def flip_di_pair(self):
        1

    def choose_di_pai(self):
        1

    def play_round(self):
        self.deal()


    def turn_helper(self, start):
        hand_size=len(self.players[0].gethand())

