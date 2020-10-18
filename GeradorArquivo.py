import os
def arquivo(tam):
    arquivo = open("archive.txt", "a")
    file = os.path.getsize ('archive.txt')
    while(True):
        if (file+8 <= tam):
            arquivo = open("archive.txt", "a")
            arquivo.write("a\n")
            file = os.path.getsize ('archive.txt')
        else:
            break

arquivo(100)