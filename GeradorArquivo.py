import os
def FileGenerator(tam):
    arquivo = open("archive.txt", "a")
    fileSize = os.path.getsize ('archive.txt')
    while(True):
        if (fileSize+8 <= tam):
            arquivo = open("archive.txt", "a")
            arquivo.write("a")
            fileSize = os.path.getsize ('archive.txt')
        else:
            break