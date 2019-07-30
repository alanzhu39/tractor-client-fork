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
        assert set_zhuang_jia

    def deal(self):
        self.deck = Deck()
        deck.shuffle()
        self.current_drawer = zhuang_jia_id
        while len(deck) > num_di_pai:
            players[current_drawer].draw()
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
            self.trump_suit = "wu zhu"
            self.trump_suit_cnt = 2
        
        

    # compare two cards
    def cmp_cards(a, b):

    def play_turn(self):
        

    def play_round(self):
        Round.deal()
        
print('asdf')
