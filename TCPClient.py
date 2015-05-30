from socket import *
import sys

server_address = ("localhost", 9999)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

while 1:
    sentence = raw_input("Lower case sentence (quit to exit): ")
    client_socket.send(sentence)
    if sentence == "quit":
        client_socket.close()
        sys.exit(0)
    upcased_sentence = client_socket.recv(2048)
    print upcased_sentence
