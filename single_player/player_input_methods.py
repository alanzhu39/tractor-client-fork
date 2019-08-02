from single_player.player import Player
from single_player.deck import Card

def get_current_player_input():
    # format is card rank+card suit (lowercase) or BJo/Sjo all separated by spaces if multiple
    response = input().split()
    return response


def is_pair(card1, card2):
    if card1 == card2:
        return True


def is_valid_input(player, response):
    for each_index in response:
        if int(each_index) < 0 or int(each_index) > len(player.get_hand()):
            return False
        if len(set(response)) != len(response):
            return False
        return True


def is_trump(card, trumpinfo):
    if card.is_joker:
        return True
    if card.suit == trumpinfo["suit"]:
        return True
    if card.rank == trumpinfo["rank"]:
        return True
    return False

#CHECK IF A MOVE IS LEGAL FOR FIRST MOVE PLAYER
'''
Check if player's hand contains at least the same number of cards in their own hand as they request to play
Check if all trumps first, then check same suit
Check if is pair or is single
'''
def is_valid_play_firstplayer(player, response):
    for each_input in response:
        if player.hand_contains(each_input) < response.count(each_input):
            return False

#CHECK IF A MOVE IS LEGAL FOR SECOND, THIRD, AND FOURTH PLAYER
'''
Check if player's hand contains at least the same number of card in their own hand as they request to play
Check if hand style must be of trump -> if hand style is of a certain suit
Make sure player's request contains minimum(# of trumps/certain suit, cards played)
If handtype is tractor/pair, look through hand to see if contains tractor/pair of same hand style
'''
def is_valid_play_nextplayer(player, response):
    1


def hand_contains_pair_in_suit(hand, suit, trumpinfo):
    for i in range(len(hand)-1):
        if suit == 'trump':
            if hand[i] == hand[i+1] and is_trump(hand[i], trumpinfo):
                return True
        else:
            if hand[i] == hand[u+1] and hand[i].suit == suit:
                return True
    return False

def num_cards_in_suit(hand, suit, trumpinfo):
    cnt = 0
    if suit == 'trump':
        for i in range(len(hand)):
            if is_trump(hand, trumpinfo):
                cnt +=1
    else:
        for i in range(len(hand)):
            if hand[i].suit == suit:
                cnt+1
    return cnt
#RETURNS THE HANDTYPE AND CARDS PLAYED IN A TUPLE
def get_valid_input(player, startplayer, trumpinfo, curSuit, curType, curNumCards):
    name = player.get_name()
    #IF PERSON IS FIRST TO ACT
    hand = player.get_hand()
    if startplayer.get_name() == name:
        while True:
            print(name + ": Please type what you want to play (format:'BJo','SJo','10c','7s','Qd',etc)")
            response = get_current_player_input()
            if not is_valid_input(response):
                continue
            break
        if len(response) == 2:
            card1 = hand[int(response[0])]
            card2 = hand[int(response[1])]
            if is_pair(card1, card2):
                if is_trump(card1, trumpinfo):
                    return True, [card1, card2], 'trump', 'pair'
                else:
                    return True, [card1, card2], card1.suit, 'pair'
        elif len(response) == 1:
            card1 = hand[int(response[0])]
            if is_trump(card1, trumpinfo):
                return True, [card1], 'trump', 'single'
            else:
                return True, [card1], card1.suit, 'single'
        else:
            return False, []



    #IF PERSON IS NOT FIRST TO ACT
    if startplayer.get_name()!= name:
        while True:
            print(name+": Please type the indeces of the cards you would like to play")
            response = get_current_player_input()
            if not is_valid_input(response):
                continue
            break
        if curNumCards == 2:
            if curType == 'pair' and len(response) == 2:
                card1 = hand[int(response[0])]
                card2 = hand[int(response[1])]
                responsehand = [card1, card2]
                if num_cards_in_suit(hand, curSuit, trumpinfo) >= 2:
                    if hand_contains_pair_in_suit(hand, curSuit, trumpinfo):
                        if hand_contains_pair_in_suit(responsehand, curSuit, trumpinfo):
                            return True, responsehand
                        else:
                            return False, []
                    else:
                        if num_cards_in_suit(responsehand, curSuit, trumpinfo) == 2:
                            return True, responsehand
                        else:
                            return False, []
                elif num_cards_in_suit(hand, curSuit, trumpinfo) == 1:
                    if num_cards_in_suit(responsehand, curSuit, trumpinfo) == 1:
                        return True, responsehand
                    else:
                        return False, []
                elif num_cards_in_suit(hand, curSuit, trumpinfo) == 0:
                    return True, responsehand

        if curNumCards == 1:
            if len(response) == 1:
                card1 = hand[int(response[0])]
                responsehand = [card1]
                if num_cards_in_suit(hand, curSuit, trumpinfo) == 1:
                    if num_cards_in_suit(responsehand, curSuit, trumpinfo) == 1:
                        return True, responsehand
                    else:
                        return False, []
                else:
                    return True, responsehand

                

