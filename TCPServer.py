from socket import *

listening_address = ("localhost", 9999)
listening_socket = socket(AF_INET, SOCK_STREAM)
listening_socket.bind(listening_address)
listening_socket.listen(1)
print "Ready to receive sentences"

connection_socket, addr = listening_socket.accept()
while 1:
    downcased_sentence = connection_socket.recv(2048)
    if downcased_sentence == "quit":
        connection_socket.close()
        connection_socket, addr = listening_socket.accept()
        continue
    upcasedSentence = downcased_sentence.upper()
    connection_socket.send(upcasedSentence)
