import socket
from _thread import *
import sys
from single_player.round_copy import *
from single_player.player import *
import single_player.connections as connections
import selectors
import types

sel = selectors.DefaultSelector()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("Waiting for a connection")

sheng_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_ids = [0, 0, 0, 0]

zj_id = 0
players = [Player("Adam", sheng_order[0]), Player("Andrew", sheng_order[0]),
           Player("Alan", sheng_order[0]), Player("Raymond", sheng_order[0])]
players[zj_id].set_is_zhuang_jia(True)

r = testRound(players)

def threaded_client(conn):
    global currentId, pos
    currentId = connections.get_length() - 1
    conn.send(str.encode(str(currentId)))
    reply = ''
    while currentId != r.get_current_player():
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                reply = r.get_data()
                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break
    '''
    print("Connection Closed")
    conn.close()
    '''

while connections.get_length() < 4:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    start_new_thread(threaded_client, (conn,))
    connections.add_conn(conn)

r.play_round()

'''
data = client_conns[0].recv(2048)
reply = data.decode('utf-8')
if reply == 'x':
    print("received x")
else:
    reply = "y"
client_conns[0].sendall(str.encode(reply))


def get_player_input(self):
    # just player indexes, check if integerse
    response = input().split()
    integer_list = [s for s in response if s.isdigit()]
    return list(map(int, integer_list))


def is_valid_input(self, player, response):
    if len(set(response)) != len(response):
        return False
    for each_index in response:
        if int(each_index) < 0 or int(each_index) >= len(player.get_hand()):
            return False
    return True
'''