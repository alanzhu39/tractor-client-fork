import socket
from _thread import *
import sys
from single_player.round_copy import *
from single_player.player import *
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


sheng_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
rank_ids = [0, 0, 0, 0]

zj_id = 0
players = [Player("Adam", sheng_order[0]), Player("Andrew", sheng_order[0]),
           Player("Alan", sheng_order[0]), Player("Raymond", sheng_order[0])]
players[zj_id].set_is_zhuang_jia(True)

r = testRound(players)



def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = int(arr[0])
                pos[id] = reply

                if id == 0: nid = 1
                if id == 1: nid = 0

                reply = pos[nid][:]
                print("Sending: " + reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))