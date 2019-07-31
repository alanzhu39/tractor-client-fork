'''
add players
start the rounds
keep track of scores
'''
from single_player.player import *
from single_player.round import *

players = [Player("Adam"), Player("Andrew"), Player("Alan"), Player("Raymond")]
players[0].set_zhuang_jia(True)
for i in range(4):
    players[i].set_trump_rank('2')

round = Round(players)
round.play_round()
players[0].set_zhuang_jia(True)
