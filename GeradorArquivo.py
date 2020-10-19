import os
def FileGenerator(tam):
    arquivo = open("archive5.txt", "w")
    fileSize = os.path.getsize ('archive5.txt')
    while(True):
        if (fileSize+8 <= tam):
            arquivo = open("archive5.txt", "a")
            arquivo.write("a")
            fileSize = os.path.getsize ('archive5.txt')
        else:
            break

FileGenerator(1000000)