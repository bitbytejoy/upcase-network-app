from socket import *
import sys

server_name = "localhost"
server_port = 9999

client_socket = socket(AF_INET, SOCK_DGRAM)

while 1:
    sentence = raw_input("Lower cased sentence (quit to exit): ")
    if sentence == "quit":
        client_socket.close()
        sys.exit(0)
    client_socket.sendto(sentence, (server_name, server_port))
    upcased_sentence, serverAddress = client_socket.recvfrom(2048)
    print upcased_sentence
