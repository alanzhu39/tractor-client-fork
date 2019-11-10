class Hand(object):

    def __init__(self, cardlist, suit='all'):
        self.cardlist = cardlist
        self.suit = suit

    def __gt__(self, other_hand):
        """
        N
        determine if hand is greater than other hand in the context of the round
        """
        pass

    def get_num_points(self):
        total = 0
        for card in self.cardlist:
            if card.get_rank() == '5':
                total += 5
            elif card.get_rank() == '10' or card.get_rank() == 'K':
                total += 10
        return total
