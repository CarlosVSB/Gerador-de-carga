import socket
from threading import Thread
import time
import sqlite3 as sqlite
import pickle
import os


class bd(Thread):
    def __init__(self, CSocket, Adress):
        Thread.__init__(self)
        self.Sock = CSocket
        self.Ad = Adress
        print('Iniciada conexão com cliente', Adress)

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
        print("TIPO: ",type(loads))
        #query = '''insert into arquivos(arq) values {};'''.format(loads)
        #tupla = (loads,)
        conexao = sqlite.connect('Workload.db')
        conexao.execute("""INSERT INTO arquivos (arq) VALUES (?) """, (memoryview(loads.encode()), ))
        conexao.commit()
        conexao.close()
        self.Sock.send("daijobu".encode())


conexao = sqlite.connect('Workload.db')
cursor = conexao.cursor()
conexao.execute('''CREATE TABLE IF NOT EXISTS arquivos
                (
                arq BLOB NOT NULL
                );''')
conexao.close()

host = ''
port = 7000
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria o socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)  # reiniciliza o socket
# define a porta e quais ips podem se conectar com o servidor
server.bind(addr)
cont = 0
os.system('nohup ./memoryLog.sh &')
while cont < 3:
    server.listen(1)
    print('aguardando conexao')
    clientsock, clientAddress = server.accept()
    print('conectado')
    newthread = bd(clientsock, clientAddress)
    newthread.start()

server.close()
