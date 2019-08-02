import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print(data)
 
class TractorServer(PodSixNet.Server.Server):
 
    channelClass = ClientChannel
 
    def Connected(self, channel, addr):
        print('new connection:', channel)
 
print("STARTING SERVER ON LOCALHOST")
tractorServe = TractorServer()
while True:
    tractorServe.Pump()
    sleep(0.01)
