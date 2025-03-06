import os
linhas = ["Conteúdo da primeira linha.", "\nConteúdo da segunda linha."]

arquivo_escrita = open("owo.txt", "w")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

arquivo_escrita = open("owo.txt", "a")
arquivo_escrita.write("\nConteúdo adicional.")
arquivo_escrita.close()

print("Iterando sobre o arquivo")
with open("owo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", arquivo.name)