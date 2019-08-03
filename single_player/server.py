from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep

class ClientChannel(Channel):
    def Network(self, data):
        print(data)
 
class TractorServer(Server):
 
    channelClass = ClientChannel()
 
    def Connected(self, channel, addr):
        print('asdfasdfasdf:', channel)

print("STARTING SERVER ON LOCALHOST")
tractorServe = TractorServer()
while True:
    tractorServe.Pump()
    sleep(0.0001)
