import socket
localIP = '127.0.0.1'
localport = 20001

buffersize = 1024

msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

UDPSERVERSOCKET = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UDPSERVERSOCKET.bind((localIP,localport))

print("UDP server listening...")

while True:
    byteAddressPair = UDPSERVERSOCKET.recvfrom(buffersize)
    message = byteAddressPair[0]
    address = byteAddressPair[1]

    clientmsg = "Message from cline{}".format(message)
    cilentIP = "Client IP address:{}".format(address)
    print(clientmsg)
    print(cilentIP)
    UDPSERVERSOCKET.sendto(bytesToSend,address)

