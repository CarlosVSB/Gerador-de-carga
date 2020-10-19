import socket
from threading import Thread
import time
import mysql.connector as mysql
import pickle
import os

class bd(Thread):
    def __init__(self,CSocket,Adress):
        Thread.__init__(self)
        self.Sock=CSocket
        self.Ad=Adress
        print('Iniciada conexão com cliente',Adress)

    def run(self):
        data = b''
        while True:
            recebe = self.Sock.recv(1024)
            data += recebe
            try:
                loads = pickle.loads(data)
                break
            except:
                pass

        loads = pickle.loads(data)
        query = """insert into arquivos(arq) values (%s);"""
        tupla = (loads,)
        cursor.execute(query,tupla)
        conexao.commit()
        self.Sock.send("daijobu".encode())

conexao = mysql.connect(host = 'localhost', user='root', passwd='0000')
cursor = conexao.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS Workload')
cursor.execute('USE Workload')
cursor.execute("""CREATE TABLE IF NOT EXISTS `arquivos`
                (
                `arq` blob NOT NULL
                )""")

host = ''
port = 7000
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reiniciliza o socket
server.bind(addr) #define a porta e quais ips podem se conectar com o servidor
cont=0
os.system('nohup ./memoryLog.sh &')
while cont<3:
    server.listen(1)
    print ('aguardando conexao')
    clientsock, clientAddress = server.accept()
    print('conectado')
    newthread = bd(clientsock,clientAddress)
    newthread.start()

server.close()