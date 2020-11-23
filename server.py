import signal
import socket
import sys


def signal_handle(sig, frame):
    print("CTRL+C detected, exiting...")
    sys.exit(0)

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind(("127.0.0.1", 8000))
    s.listen(1)
    print("[+] Listening on {}:{}".format("127.0.0.1", "8000"))

    conn, addr = s.accept()
    print(f"[+] Connection from {addr}")

    while True:
        command = input("SHELL> ")
        if 'exit' in command:
            conn.send('exit\r\n'.encode())
            conn.close()
            break
        else:
            #conn.send((command + '\r\n').encode())
            conn.send(f'{command}\r\n'.encode())
            print(conn.recv(1024))

signal.signal(signal.SIGINT, signal_handle)
listen()
