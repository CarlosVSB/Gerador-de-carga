import os
def arquivo(tam):
    arquivo = open("archive.txt", "a")
    file = os.path.getsize ('archive.txt')
    while(file <= tam):
        arquivo = open("archive.txt", "a")
        arquivo.write("a\n")
        file = os.path.getsize ('archive.txt')