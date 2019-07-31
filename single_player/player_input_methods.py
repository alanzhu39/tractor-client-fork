def get_current_player_input(self):
    # format is card rank+card suit (lowercase) or BJo/Sjo all separated by spaces if multiple
    print("Type the hand you want to play")
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

def get_valid_input(player, startplayer, currentsuit)

