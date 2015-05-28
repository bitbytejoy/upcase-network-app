from socket import *
import sys

serverAddress = ("localhost", 9999)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverAddress)

while 1:
    sentence = raw_input("Lower case sentence (quit to exit): ")
    clientSocket.send(sentence)
    if sentence == "quit":
        clientSocket.close()
        sys.exit(0)
    upcasedSentence = clientSocket.recv(2048)
    print upcasedSentence
