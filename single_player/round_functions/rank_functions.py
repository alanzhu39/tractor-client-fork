def card_value(self, card):
    """
    Returns a relative value of the card.
    Lowest card in a suit is 1, second lowest is 2, etc... highest (usually A) is 12 because one rank is trump
    All cards of trump suit and not in the top 12 will have 100 added to signify trump
    ex: trump_rank == 4, trump_suit == spades
    2d: 1 3d: 2 5d: 3 ... 10d: 8 Jd: 9 Qd: 10 Kd: 11 Ad: 12
    2s: 101 3s: 102 5s: 103 10s: 108 Js: 109 Qs: 110 Ks: 111 As: 112 4d: 113 4c: 113 4s: 114 SJo: 115 BJo: 116

    ex: trump_rank == 4, trump_suit == "none" (wuzhu)
    2d: 1 3d: 2 5d: 3 ... Ad: 12
    4c: 114 4d: 114 4h: 114 4s: 114 SJo: 115 BJo: 116
    :param self: the Round instance
    :param card: found in deck.py file
    :return: int
    """
    trump_rank = self.trump_rank
    trump_suit = self.trump_suit
    if card.is_big_joker:
        return 116
    elif card.is_small_joker:
        return 115
    card_suit = card.get_suit()
    card_rank = card.get_rank()
    if card_rank == trump_rank:
        if card_suit == trump_suit or trump_suit == "none":
            return 114
        else:
            return 113
    rank_dict = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11,
                 'K': 12, 'A': 13}
    temp_card_value = rank_dict[card_rank]
    if temp_card_value > rank_dict[trump_rank]:
        temp_card_value -= 1
    if self.is_trump(card):
        temp_card_value += 100
    return temp_card_value