import socket
import json
import Config.config as cfg

class UDP_Lib():

    def __init__(self):
        self.buffersize = 1024

    # def Create_Discovery_Payload(self, action=None, clientMac=None, reqID=None):
    #
    def Create_UDP_Client_Socket(self):
        # Create Socket UDP
        UDP_Client = socket.socket(family=socket.AF_INET,
                                type=socket.SOCK_DGRAM,
                                proto=socket.IPPROTO_UDP)

        # Enable Broadcasting mode
        UDP_Client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        return UDP_Client

    def Send_To(self,UDPClient=None, byteToSend=None,
                serverAddPort=None, buffsize=None):

        if UDPClient is None:
            Client = self.Create_UDP_Client_Socket()
        else:
            Client = UDPClient

        if serverAddPort is None:
            server = (cfg.SERVER_BROADCAST, cfg.PORT_BROADCAST)
        else:
            server = serverAddPort

        if buffsize is None:
            size = self.buffersize
        else:
            size = buffsize

        Client.sendto(byteToSend, server)
        msgReceived = json.loads(Client.recvfrom(size)[0])
        print("\n ****************** DISCOVERY RESPONSE *****************")
        print(json.dumps(msgReceived, indent=4))
        return msgReceived




