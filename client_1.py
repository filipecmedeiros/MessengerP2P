import socket
import thread

HOST = 'localhost'              # Endereco IP do Servidor
PORT = 4001            # Porta que o Servidor esta

def conectar(con, cliente):
    
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg

    print 'Finalizando conexao do cliente', cliente
    con.close()
    thread.exit()

def enviar():
    while True:
        msgSND = raw_input()
        con.send (msgSND)
    
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print 'Conectado por', cliente

    thread.start_new_thread(conectar, tuple([con, cliente]))
    thread.start_new_thread(enviar, ())


tcp.close()
