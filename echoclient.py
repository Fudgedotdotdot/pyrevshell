import socket
import pathlib

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 16000))

    sockFile = s.makefile(mode='wr')
    while True:
        sockFile.writeline('hello')

connect()
