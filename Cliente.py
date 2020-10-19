import socket
from GeradorArquivo import FileGenerator
from threading import Thread
import time


# ip = input('digite o ip de conexao: ')
# print(type(ip))
# port = 7000


class Envio(Thread):
    def __init__(self,adress,port,message):
        Thread.__init__(self)
        self.adress=adress
        self.port=port
        self.message=message
    
    def run(self):
        addr = ((self.adress,self.port)) #define a tupla de endereco
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET parametro para informar a familia do protocolo, SOCK_STREAM indica que eh TCP/IP
        client_socket.connect(addr) #realiza a conexao
        mensagem = self.message
        ini=time.time()
        print(ini)
        print("-------MENSAGEM:",mensagem)
        client_socket.send(mensagem.encode()) #envia mensagem
        print(client_socket.recv(1024).decode())
        fim=time.time()
        print(fim)
        print ('RTT:',fim-ini)
        client_socket.close() #fecha conexao

cont=0

ip = '127.0.0.1'
tam  = int(input("Tamanho dos arquivos: "))
qtd = int(input("Qtd de arquivos enviados: "))
taxa = int(input("Taxa de envio: "))
FileGenerator(tam)

arquivo = open("archive.txt", "r")
message = str(arquivo.readlines()).strip('[]')


while cont < qtd:
    obj=Envio(ip,7000,message)
    obj.start()
    time.sleep(taxa)
    cont+=1
