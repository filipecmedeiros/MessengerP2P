import socket
import thread

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)


def receber ():
    while True:
        msg = tcp.recv(1024)
        if not msg: break
        print msg

def enviar ():
    while True:
        msgSND = raw_input()
        tcp.send (msgSND)
    thread.exit()


while True:
    thread.start_new_thread (receber, ())
    thread.start_new_thread (enviar, ())
    tcp.close()
