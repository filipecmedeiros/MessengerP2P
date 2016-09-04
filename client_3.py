import socket
import thread

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 4001            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

def enviar(i):
    while True:
        print "Thread", i
        msgSND = raw_input()
        tcp.send (msgSND)
    thread.exit()

def receber (j):
    while True:
        print "Thread ", j
        msg = tcp.recv(1024)
        if not msg: break
    print msg
    thread.exit()  

while True:
#    thread.start_new_thread(receber, tuple([1]))
#    thread.start_new_thread(enviar, tuple([2]))
 #Receber
    msg = tcp.recv(1024)
    if not msg: break
    print "Servidor: ", msg

#Enviar
#    msgSND = raw_input()
#    tcp.send (msgSND)

