from single_player.player import Player

def get_current_player_input():
    # format is card rank+card suit (lowercase) or BJo/Sjo all separated by spaces if multiple
    response = input().split()
    return response


def is_valid_card(card_string):
    if len(card_string) == 3:
        if card_string == 'BJo' or card_string == 'SJo':
            return True
        suit=card_string[2]
        if (suit=='c' or suit=='d' or suit=='h' or suit=='s') and card_string[:2]=='10':
            return True
    if len(card_string)==2:
        suit=card_string[1]
        if (suit=='c' or suit=='d' or suit=='h' or suit=='s') and card_string[0].isDigit():
            return True


def is_pair(response):
    if len(response) == 2 and response[0] == response[1]:
        return True


def is_single(response):
    if len(response) == 1:
        return True


def is_valid_input(response):
    for each_card in response:
        if not is_valid_card(each_card):
            return False
    return True

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

#RETURNS THE HANDTYPE AND CARDS PLAYED IN A TUPLE
def get_valid_input(player, startplayer, currentsuit, handtype):
    name = player.get_name()
    #IF PERSON IS FIRST TO ACT
    if startplayer.get_name()==name:
        inputvalid = False
        while not inputvalid:
            print(name + ": Please type what you want to play (format:'BJo','SJo','10c','7s','Qd',etc)")
            response = get_current_player_input()
            if not is_valid_input(response):
                continue


    #IF PERSON IS NOT FIRST TO ACT
    if startplayer.get_name()!=name:



