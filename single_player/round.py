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
from deck import *
class Round(object):
    '''
    player = list of Player (size = 4)
    '''
    num_di_pai = 8
    def __init__(self, players):
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
        self.deck = Deck()
        self.deck.shuffle()
        self.current_drawer = self.zhuang_jia_id
        while len(self.deck) > self.num_di_pai:
            self.players[self.current_drawer].draw(self.deck.pop())
            print(self.players[self.current_drawer].name)
            self.players[self.current_drawer].print_hand()
            self.liang_query()

    def liang_query(self):
        # format is "suit cnt" or "SJo 2" or "BJo 2"
        print("Liang?")
        response = input().split()
        if len(response) != 2:
            return
        if response[1] != "1" and response[1] != "2":
            return
        if (response[0] == "SJo" or response[0] == "BJo") and response[1] == "2":
            new_trump_suit = "wu zhu"
            new_trump_suit_cnt = 3
        if response[0] in Card.suit_map:
            new_trump_suit = response[0]
            new_trump_suit_cnt = int(response[1])
        if new_trump_suit_cnt > self.trump_suit_cnt:
            print("Set trump suit to: " + self.new_trump_suit)
            self.trump_suit = new_trump_suit
            self.trump_suit_cnt = new_trump_suit_cnt
        

    # compare two cards
    def cmp_cards(a, b):
        1
    def play_turn(self):
        1

    def play_round(self):
        self.deal()

    def get_current_player_input(self):
        #format is card rank+card suit (lowercase) or BJo all separated by spaces if multiple
        print("Type the hand you want to play")
        response = input().split()
        return response

    def 

    def turn_helper(self, start):
        hand_size=len(self.players[0].gethand())


print('asdf')
