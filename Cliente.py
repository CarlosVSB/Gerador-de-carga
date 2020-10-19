import socket
from GeradorArquivo import FileGenerator
from threading import Thread
import time
import pickle

# ip = input('digite o ip de conexao: ')
# print(type(ip))
# port = 7000


class Envio(Thread):
    def __init__(self,adress,port,message,tempos):
        Thread.__init__(self)
        self.adress=adress
        self.port=port
        self.message=message
        self.tempos=tempos
    
    def run(self):
        addr = ((self.adress,self.port)) #define a tupla de endereco
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
        client_socket.connect(addr) #realiza a conexao
        mensagem = pickle.dumps(self.message)
        ini=time.time()
        client_socket.sendall(mensagem) #envia mensagem
        client_socket.recv(1024).decode()
        fim=time.time()
        #print (fim-ini)
        self.tempos.append(fim-ini)
        client_socket.close() #fecha conexao

cont=0

ip = '127.0.0.1'
qtd = 100
taxa = 1
#tam  = [200000,400000,600000,800000]
#FileGenerator(tam)

arquivo = open("archive1.txt", "r")
message = str(arquivo.readlines()).strip('[]')
tempos = []
while cont < qtd:

    obj=Envio(ip,7000,message,tempos)
    obj.start()
    time.sleep(taxa)
    cont+=1

print('SOMA: ',sum(tempos)/100)