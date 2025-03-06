import os
arquivo = open('C:/Users/grana/OneDrive/Documentos/Codes/Semestre 2/teste py/aaa.txt', 'r')
print("Nome do arquivo:", arquivo.name)
print("Modo do arquivo", arquivo.mode)
print("Arquivo fechado?", arquivo.closed)

conteudo = arquivo.readlines()
print("Tipo do conteúdo:", type(conteudo))
print("Tipo de conteúdo:", type(linha))
print(repr(linha))
arquivo.close()
