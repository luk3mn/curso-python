from datetime import date


def escolha():
    return int(input("[1] Cadastrar usuário"
                     "\n[2] Pesquisar usuário"
                     "\n[3] Atualisar usuario"
                     "\n[4] Remover usuário"
                     "\n[0] Encerrar"
                     "\nESCOLHA UMA OPÇÃO: "))


def cadastrar(dicionario):
    chave = input("Código do usuário: ")
    data = date.today()
    dicionario[chave] = [input("Nome: "),
                         chave,
                         input("E-mail: "),
                         input("Usuário: "),
                         input("Senha: "),
                         input("Data de nascimento: "),
                         str(data)]
    persistir_dados(dicionario)


def pesquisar():
    codigo = input("Codigo de usuário: ")
    with open("database/db.csv", "r") as arquivo_csv:
        for linha in arquivo_csv.readlines():
            lista = linha.split(";")
            if lista[0] == codigo:
                print("Código.........: ", lista[0])
                print("Nome...........: ", lista[1])
                print("E-mail.........: ", lista[2])
                print("Usuário........: ", lista[3])
                print("Nascimento.....: ", lista[5])
                print("Cadastrado em..: ", lista[6])


def persistir_dados(dicionario):
    with open("database/db.csv", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ";" + str(valor[0]) + ";" + str(valor[2]) + ";" + str(valor[3]) + ";" + str(
                valor[4]) + ";" + str(valor[5]) + ";" + str(valor[6]) + "\n")


# CORRIGIR O ERRO OCORRENDO EM 'for linha in arquivo_csv.readlines():'
def remover():
    codigo, validacao = [input("Código do usuário: "), input("Tem certeza disso [S/N]: ").upper()]
    if validacao == "S":
        with open("database/db.csv", "a") as arquivo_csv:
            for linha in arquivo_csv.readlines():
                lista = linha.split(";")
                if codigo == lista[0]:
                    # linha.replace(" ")
                    print(lista)
