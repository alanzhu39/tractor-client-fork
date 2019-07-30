class Deck(object):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['\u2663', '\u2666', '\u2665', '\u2660']
    def __init__(self):
        self.ids = []
        self.card_names = []
        for i in range(108):
            self.ids.append(i)
        for r in ranks:
            for s in suits:
                self.card_names.append(ranks[i]+suits[i])
deck = Deck()
for s in deck.card_names:
    print(s)
