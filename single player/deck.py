'''
structure for cards
structure for deck
note: trumps ignored
'''
class Card(object):
    '''
    rank = string
    suit = string
    is_trump = boolean
    is_big_joker = boolean
    is_small_joker = boolean
    '''
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['\u2663', '\u2666', '\u2665', '\u2660']
    def __init__(self, rank, suit, is_big_joker = False, is_small_joker = False):
        self.rank = rank
        self.suit = suit
        self.is_big_joker = is_big_joker
        self.is_small_joker = is_small_joker
        self.is_joker = is_big_joker or is_small_joker
        # implement below when trump suit decided
        #self.is_trump = is_trump
        #assert not(not self.is_trump and self.is_joker)

    def __str__(self):
        if self.is_big_joker:
            return 'BJo'
        if self.is_small_joker:
            return 'SJo'
        return self.rank + self.suit
    
    def __eq__(self, other):
        if self.is_big_joker and other.is_big_joker:
            return True
        if self.is_small_joker and other.is_small_joker:
            return True
        if self.rank == other.rank and self.suit == other.suit:
            return True
        return False
    '''
    Perhaps not necessary? Find a check in while playing
    def __lt__(self, other):
        # check equality 
        if self == other:
            return False
        # check joker cases
        if self.is_big_joker:
            return False
        if self.is_small_joker:
            return other.is_big_joker
        if other.is_joker:
            return True
        # check trump
        if self.is_trump:
            return other.is_trump and self.rank
        # check current suit???
    '''    
        
class Deck(object):
    def __init__(self):
        self.ids = []
        self.cards = []
        for i in range(108):
            self.ids.append(i)
        for r in Card.ranks:
            for s in Card.suits:
                self.cards.append(Card(r, s))
                self.cards.append(Card(r, s))
        self.cards.append(Card('', '', False, True))
        self.cards.append(Card('', '', False, True))
        self.cards.append(Card('', '', True, False))
        self.cards.append(Card('', '', True, False))
        
    def printCardNames(self):
        for s in self.cards:
            print(s)
        
# deck = Deck()
# deck.printCardNames()
