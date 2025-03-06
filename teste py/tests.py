import os

caminho = r"C:/Users/grana/OneDrive/Documentos/Codes/Semestre 2/teste py/aaa.txt"

if os.path.exists(caminho):
    try:
        with open(caminho, "r") as arquivo:
            conteudo = arquivo.read()
            print("Arquivo aberto com sucesso!\n")
            print("Conteúdo do arquivo:")
            print(conteudo)
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o arquivo: {e}")
else:
    print("Arquivo não encontrado. Verifique o caminho.") 

