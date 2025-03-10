import os

def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")

    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == "sair":
            break
        frases.append(entrada)

    with open("textinho.txt", "w") as arquivo:
        for frase in frases:
            arquivo.write(frase + "\n")

    print("Arquivo original criado. Agora vamos manipular os dados.")

    dados_modificados = []
    with open("textinho.txt", "r") as arquivo:
        for linha in arquivo:
            dados_modificados.append(linha.strip().upper())

    with open("textinho.txt", "w") as arquivo:
        for linha in dados_modificados:
            arquivo.write(linha + "\n")

    print("O arquivo foi sobrescrito com os dados modificados.")

if __name__ == "__main__":
    main()