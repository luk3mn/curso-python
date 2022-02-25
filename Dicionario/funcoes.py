def perguntar():
    return input("O que deseja realizar? [0 - Encerra]\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário: \n").upper()


def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [input("Digite o nome: ").upper(),
                         input("Digite a última data de acesso: "),
                         input("Qual a última estação acessada: ").upper()]


def pesquisar(dicionario):
    login = input("Informe o login: ").upper()
    lista = dicionario.get(login);
    if lista:
        # print(dicionario.get(login))
        print("Nome...............: " + lista[0])
        print("Último acesso......: " + lista[1])
        print("Última estação.....: " + lista[2])
    else:
        print("\"Login\" não existe!")


def excluir(dicionario):
    login = input("Informe o login: ").upper()
    confirme = input("Tem certeza disso? [S/N]").upper()
    if confirme == "S":
        if dicionario.get(login):
            del dicionario[login]
            print("O usuário foi deletado!")
        else:
            print("Login não encontrado!")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto..............")
        print("Login:", chave)
        print("Dados: ", valor)