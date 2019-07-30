'''
add players
start the rounds
keep track of scores
'''
from player import *
from round import *

players = [Player("Adam"), Player("Andrew"), Player("Alan"), Player("Raymond")]
players[0].set_zhuang_jia(True)

round = Round(players)
round.play_round()
players[0].set_zhuang_jia(True)
