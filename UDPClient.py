from socket import *
import sys

serverName = "localhost"
serverPort = 9999

clientSocket = socket(AF_INET, SOCK_DGRAM)

while 1:
    sentence = raw_input("Lower cased sentence (quit to exit): ")
    if sentence == "quit":
        clientSocket.close()
        sys.exit(0)
    clientSocket.sendto(sentence, (serverName, serverPort))
    upcasedSentence, serverAddress = clientSocket.recvfrom(2048)
    print upcasedSentence
