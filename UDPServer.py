from socket import *

server_port = 9999

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print "Ready to receive sentences"

while 1:
    downcased_sentence, client_address = server_socket.recvfrom(2048)
    upcased_sentence = downcased_sentence.upper()
    server_socket.sendto(upcased_sentence, client_address)
