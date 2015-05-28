from socket import *

listeningAddress = ("localhost", 9999)
listeningSocket = socket(AF_INET, SOCK_STREAM)
listeningSocket.bind(listeningAddress)
listeningSocket.listen(1)
print "Ready to receive sentences"

connectionSocket, addr = listeningSocket.accept()
while 1:
    downcasedSentence = connectionSocket.recv(2048)
    if downcasedSentence == "quit":
        connectionSocket.close()
        connectionSocket, addr = listeningSocket.accept()
        continue
    upcasedSentence = downcasedSentence.upper()
    connectionSocket.send(upcasedSentence)
