"""
add players
start the rounds
keep track of scores
"""
from single_player.player import *
from single_player.round import *

# below is a test
zj_id = 0
players = [Player("Adam", "2"), Player("Andrew", "2"), Player("Alan", "2"), Player("Raymond", "2")]
players[zj_id].set_is_zhuang_jia(True)

r = Round(players)
pts = r.play_round()

# todo
if pts == 0:
    # increase trump rank of players[zj_id] and players[(zj_id+2)%4] by 3
    zj_id = (zj_id + 2) % 4
elif pts < 40:
    # increase trump rank of players[zj_id] and players[(zj_id+2)%4] by 2
    zj_id = (zj_id + 2) % 4
elif pts < 80:
    # increase trump rank of players[zj_id] and players[(zj_id+2)%4] by 1
    zj_id = (zj_id + 2) % 4
else:
    num_shengs = (pts - 80)//40
    # increase trump rank of players[(zj_id+1)%4] and players[(zj_id+3)%4] by num_shengs
    zj_id = (zj_id + 1) % 4
