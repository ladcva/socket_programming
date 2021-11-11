# server.py
import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

serversocket.bind((host, port))

serversocket.listen()

while True:
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    # message = 'Hi, nice to meet you' + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()