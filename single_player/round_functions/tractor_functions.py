class Tractor(object):
    def __init__(self, highest_card_value, length):
        self.high_card_value = highest_card_value
        self.length = length

    def __gt__(self, other):
        pass

    def get_highest_value(self):
        return self.high_card_value

    def get_tractor_length(self):
        return self.length

