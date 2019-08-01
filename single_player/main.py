"""
add players
start the rounds
keep track of scores
"""
from player import *
from round import *

# below is a test
players = [Player("Adam", "2"), Player("Andrew", "2"), Player("Alan", "2"), Player("Raymond", "2")]
players[0].set_is_zhuang_jia(True)

r = Round(players)
r.play_round()