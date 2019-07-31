"""
Keep track of:
everyone's cards
current Zhuang Jia
Zhuang Jia discard
current trump
current attacker's points

also play the round:
dealing, compare cards, and playing
"""
from single_player.deck import *
import single_player.player_input_methods as pim


class Round(object):
    """
    players = list of Player (size = 4) (list of Player object)
    zhuang_jia_id = ID of zhuang jia in players (int)
    set_zhuang_jia = True if there is a zhuang jia at the start of the round (boolean)
    trump_suit = trump suit (string)
    trump_suit_cnt = number of cards used to liang the trump suit (exceptions: 0 if no liang and 3 if wu zhu)
    """
    num_di_pai = 8

    def __init__(self, players):
        self.deck = Deck()
        assert(len(players) == 4)
        self.players = players

        # find ID of zhuang jia, set_zhuang_jia is True if someone is zhuang jia
        self.set_zhuang_jia = False
        for i in range(len(players)):
            if players[i].is_zhuang_jia:
                self.zhuang_jia_id = i
                self.set_zhuang_jia = True

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
        # no liang -> flip di pai
        if self.trump_suit == "none":
            self.flip_di_pai()
        # zhuang jia chooses 8 cards for di pai
        self.choose_di_pai()

    def liang_query(self, current_drawer):
        # format is "suit cnt" or "SJo 2" or "BJo 2"
        print("Liang?")
        response = input().split()
        # "n" "no" or nothing means no liang
        if len(response) == 0 or response[0] == "n" or response[0] == "no":
            print("No liang, continuing")
            return
        # check for validity of the response
        if len(response) != 2:
            print("invalid response, continuing")
            return
        if response[1] != "1" and response[1] != "2":
            print("invalid response, continuing")
            return
        if (response[0] == "SJo" or response[0] == "BJo") and response[1] == "2":
            # wu zhu liang
            new_trump_suit = "wu zhu"
            new_trump_suit_cnt = 3
        elif response[0] in Card.suit_map:
            # other liang
            new_trump_suit = response[0]
            new_trump_suit_cnt = int(response[1])
        else:
            print("invalid response, continuing")
            return

        # check whether the liang is valid
        if response[0] == "SJo":
            card_to_check = SMALL_JOKER
            cnt_to_check = 2
        elif response[0] == "BJo":
            card_to_check = BIG_JOKER
            cnt_to_check = 2
        else:
            card_to_check = Card(self.players[0].get_trump_rank(), new_trump_suit)
            cnt_to_check = new_trump_suit_cnt

        if self.players[current_drawer].card_count(card_to_check) >= cnt_to_check:
            if new_trump_suit_cnt > self.trump_suit_cnt:
                print("Set trump suit to: " + new_trump_suit)
                self.trump_suit = new_trump_suit
                self.trump_suit_cnt = new_trump_suit_cnt
            else:
                print("You don't have the cards necessary for that liang")
        else:
            print("You don't have the cards necessary for that liang")
        

    def cmp_cards(a, b):
        1

    def play_turn(self):
        1

    def flip_di_pai(self):
        1

    def choose_di_pai(self):
        1

    def play_round(self):
        self.deal()
        while len(self.players[0].get_hand()) > 0:
            self.play_turn()

    def turn_helper(self, start):
        hand_size=len(self.players[0].gethand())

