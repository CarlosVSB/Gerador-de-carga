import socket
from threading import Thread
import time


class bd(Thread):
    def __init__(self,CSocket,Adress):
        Thread.__init__(self)
        self.Sock=CSocket
        self.Ad=Adress
        print('Iniciada conexão com cliente',Adress)

    def run(self):
        recebe = self.Sock.recv(1024)
        time.sleep(2)
        self.Sock.send("daijobu".encode())

host = ''
port = 7000
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
server.bind(addr) #define a porta e quais ips podem se conectar com o servidor
cont=0
while cont<3:
    server.listen(1)
    print ('aguardando conexao')
    clientsock, clientAddress = server.accept()
    print('conectado')
    newthread = bd(clientsock,clientAddress)
    newthread.start()

server.close()