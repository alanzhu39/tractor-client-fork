import single_player.player_input_methods as pim

def play_round(self):
    self.deal()

    # play out the turns
    # pass in trump info as a dictionary
    info = self.play_turn(self.zhuang_jia_id)
    while len(self.players[0].get_hand()) > 0:

        # assumes that play_turn return an info dictionary
        trick_winner = info['trick_winner']
        info = self.play_turn(trick_winner)

    # reveal di pai and add to attacker's points if necessary
    attacker_multiplier = 2 * info['num_cards']
    if (info['trick_winner'] == self.zhuang_jia_id) or (info['trick_winner'] == (self.zhuang_jia_id + 2) % 4):
        attacker_multiplier = 0

    di_pai_points = 0
    print("Di pai: ", end='')
    for card in self.discards:
        di_pai_points += card.point_value
        print(card, end=' ')
    print('')

    if attacker_multiplier > 0:
        print("Attackers won the last trick, adding %d * %d = %d points."
              % (attacker_multiplier, di_pai_points, attacker_multiplier * di_pai_points))
        self.attacker_points += attacker_multiplier * di_pai_points

    return self.attacker_points


def deal(self):
    self.deck.shuffle()
    current_drawer = self.zhuang_jia_id
    while len(self.deck) > self.num_di_pai:
        self.players[current_drawer].draw(self.deck.pop())
        print(self.players[current_drawer].name)
        self.players[current_drawer].print_hand()
        # self.liang_query(current_drawer)
        current_drawer = (current_drawer + 1) % 4
    # no liang -> flip di pai
    if self.trump_suit == "none":
        self.flip_di_pai
    # zhuang jia chooses 8 cards for di pai
    self.choose_di_pai()


def flip_di_pai(self):
    """
    Flips cards from di pai until the trump rank or joker is hit, and sets the trump suit accordingly
    Otherwise makes the largest card the trump rank
    :param self: round instance
    """
    print("No liang, flipping di pai...")
    largest_rank_suit = "none"
    largest_rank = 1
    rank_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12,
                 'K': 13, 'A': 14}
    for card in self.deck.cards:
        print(card)
        if card.is_big_joker or card.is_small_joker:
            self.trump_suit = "none"
            print("The game is now WuZhu")
            return
        elif card.rank == self.trump_rank:
            self.trump_suit = card.suit
            print("The trump suit is now %s" % card.suit)
            return
        else:
            if rank_dict[card.rank] > largest_rank:
                largest_rank_suit = card.suit
    self.trump_suit = largest_rank_suit
    print("The trump suit is now %s" % self.trump_suit)
    return


def choose_di_pai(self):
    zhuang_jia_player = self.players[self.zhuang_jia_id]
    for card in self.deck.cards:
        zhuang_jia_player.draw(card)
    print(zhuang_jia_player.get_name() + ". Your hand after di pai:")
    zhuang_jia_player.print_hand()
    print("The trump suit is " + self.trump_suit)
    while len(self.discards) != 8:
        print("Enter 8 indexes you want to discard:")
        discard_indexes = pim.get_player_input()
        if not pim.is_valid_input(zhuang_jia_player, discard_indexes) or not len(discard_indexes) == 8:
            continue
        else:
            break
    # ADDS DISCARDS TO SELF.DISCARDS, DELETES CARDS FROM PLAYER HAND
    for each_index in discard_indexes:
        self.discards.append(zhuang_jia_player.get_hand()[each_index])
    self.del_indexes(zhuang_jia_player, discard_indexes)
