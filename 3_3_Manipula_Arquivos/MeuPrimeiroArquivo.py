# arquivo = open("primeiro_arquivo.txt", "w")
# arquivo.write("Meu primeiro arquivo! Ai que festa!")
# arquivo.close()

# melhorando o código (Não precisa mais do close())
# with open("arquivo.txt", "w") as arquivo:
#     arquivo.write("Hakuna Matata!\nÉ lindo viver!\nHakuna Matata!\nSe vai entender!")

# realizando a leitura do arquivo.txt
with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# realizando a leitura de forma iterativa
with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)