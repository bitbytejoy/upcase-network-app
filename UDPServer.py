from socket import *

serverPort = 9999

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "Ready to receive sentences"

while 1:
    downcasedSentence, clientAddress = serverSocket.recvfrom(2048)
    upcasedSentence = downcasedSentence.upper()
    serverSocket.sendto(upcasedSentence, clientAddress)
