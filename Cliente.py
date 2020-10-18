import socket
from threading import Thread
import time


# ip = input('digite o ip de conexao: ')
# print(type(ip))
# port = 7000


class Envio(Thread):
    def __init__(self,adress,port):
        Thread.__init__(self)
        self.adress=adress
        self.port=port
    
    def run(self):
        addr = ((self.adress,self.port)) #define a tupla de endereco
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
        client_socket.connect(addr) #realiza a conexao
        mensagem = 'mensagem'
        ini=time.time()
        print(ini)
        client_socket.send(mensagem.encode()) #envia mensagem
        print(client_socket.recv(1024).decode())
        fim=time.time()
        print(fim)
        print ('RTT:',fim-ini)
        client_socket.close() #fecha conexao

cont=0

while cont < 3:
    obj=Envio("192.168.18.22",7000)
    obj.start()
    time.sleep(1)
    cont+=1
