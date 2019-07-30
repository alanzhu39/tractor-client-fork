'''
Keep track of:
player's hand
'''
import operator
class Player():
    def __init__(self, name, trump_suit = 'spades', zhuang_jia = False, attacker = False, hand = []):
        self.name = name
        self.zhuang_jia = zhuang_jia
        self.hand = hand
        self.trump_suit = trump_suit
        self.attacker = attacker

    def __str__(self):
        return self.name, self.zhuangjia, self.hand

    def get_name(self):
        return self.name

    def get_trump_suit(self):
        return self.trump_suit

    def get_trump_card(self):
        return self.trump_card

    def get_zhuang_jia(self):
        return self.zhuang_jia

    def get_hand(self):
        return self.hand

    def get_attacker(self):
        return self.attacker

    def set_name(self, name):
        self.name = name

    def set_trump_suit(self, trump_suit):
        self.trump_suit = trump_suit

    def set_trump_card(self, trump_card):
        self.trump_card = trump_card

    def set_zhuang_jia(self, zhuang_jia):
        self.zhuang_jia = zhuang_jia

    def set_hand(self, hand):
        self.hand = hand

    def set_attacker(self, attacker):
        self.attacker = attacker

    def get_hand_size(self):
        return len(hand)

    def print_hand(self):
        for card in self.hand:
            print (card,end=' ')
        print('')

    def draw(self, card):
        #draws a card and checks to see if the player wants to declare trump suit
        for i in range(len(self.hand)):
            if compare(card, self.hand[i], self.trump_suit, self.trump_card) >= 0:
                self.hand.insert(i,card)
                break
        self.hand.append(card)

    def play(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        else:
            return "Card not in hand"

    def sort(self, trump_card, trump_suit):
        new_hand = []
        for card in self.hand:
            for i in range(len(new_hand)):
                if compare(card, new_hand[i], self.trump_suit, self.trump_card) >= 0:
                    new_hand.insert(i, card)
                    break
        self.hand = new_hand[:]

    def compare(self, card1, card2, trump_suit, trump_card):
        if card1 == card2:
            return 0
        if card1.is_big_joker:
            return 1
        if card2.is_big_joker:
            return -1
        if card1.is_small_joker:
            return 1
        if card2.is_small_joker:
            return -1
        if card1.rank == trump_card and card1.suit == trump_suit:
            return 1
        if card2.rank == trump_card and card2.suit == trump_suit:
            return -1
        if card1.rank == trump_card and card2.rank == trump_card:
            return 0
        if card1.rank == trump_card:
            return 1
        if card2.rank == trump_card:
            return -1

        suit_dict = {'clubs': 1, 'diamonds': 2, 'hearts': 3, 'spades': 4}
        suit_dict[trump_suit] = 5
        rank_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        rank_dict[trump_card] = 15
        if suit_dict[card1.suit] > suit_dict[card2.suit]:
            return 1
        elif suit_dict[card1.suit] < suit_dict[card2.suit]:
            return -1
        else:
            if rank_dict[card1.rank] > rank_dict[card2.rank]:
                return 1
            else:
                return -1





