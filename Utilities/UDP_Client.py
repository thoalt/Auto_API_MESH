import socket
import json

msgFromClientDict = {
 "action": "discovery",
 "clientMac": "00:0E:C6:59:A1:A6",
 "authenString": "$1$D2...40.$APHR6xyBOu/L6QQWK06UT1",
 "requestId": 2408
}
msgFromClient = json.dumps(msgFromClientDict)
bytesToSend = str.encode(msgFromClient)

serverAddrPort = ("255.255.255.255", 9000)
bufferSize = 1024

# Create UDP Socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET,
                                type=socket.SOCK_DGRAM,
                                proto=socket.IPPROTO_UDP)

# Enable Broadcasting mode
UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddrPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msgReceived = json.loads(msgFromServer[0])
msgDict = json.dumps(msgReceived, indent=4)

print("**************Msg From Server **********")
print(msgFromServer)
print(msgReceived)
print(msgDict)