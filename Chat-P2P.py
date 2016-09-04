import socket
import thread
import threading

def ServidorRecebe(con, cliente):    
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg

    print 'Finalizando conexao do cliente', cliente
    con.close()
    thread.exit()

def ServidorEnvia():
    while True:
        msgSND = raw_input()
        con.send (msgSND)
    
    thread.exit()

def ClienteEnvia (tcp, ):
    while True:
        msgSND = raw_input()
        tcp.send (msgSND)
    thread.exit()



HOST = 'localhost'              # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = (HOST, PORT)

menu = raw_input ("0.Servidor\n1.Cliente\n")
while menu != '0' or menu != '1':
    if menu == '0':
        tcp.bind(connection)
        tcp.listen(1)
        while True:
            con, cliente = tcp.accept()
            print 'Conectado por', cliente
          
            thread.start_new_thread(ServidorRecebe, tuple([con, cliente]))
            thread.start_new_thread(ServidorEnvia, ())
        
        tcp.close()

    elif menu == '1':
        tcp.connect(connection)
        t = threading.Thread (target=ClienteEnvia, args=(tcp, ))
        t.daemon = True
        t.start()

        while True:
            msg = tcp.recv(1024)
            if not msg: break
            print msg

    else:
        menu = raw_input ("0.Servidor\n1.Cliente\n")
