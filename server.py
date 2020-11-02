import socket


def convert_unix_python(command):
    if 'ls' in command:
        return compile("""import pathlib\ncurrentDir = pathlib.Path('.')\nfor currentFile in currentDir.iterdir():\tprint(currentFile)""", 'command', 'exec')
    else:
        print('asdf')

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen(1)
    print("[+] Listening on {}:{}".format("127.0.0.1", "8000"))

    conn, addr = s.accept()
    print(f"[+] Connection from {addr}")

    while True:
        command = input("SHELL> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            py_cmd = convert_unix_python(command)
            print(py_cmd)
            conn.send(py_cmd.encode())
            print(conn.recv(1024))

listen()
