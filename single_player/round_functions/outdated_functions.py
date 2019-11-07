"""
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
"""