def clear():
    try:
        import os
        lines = os.get_terminal_size().lines
    except:
        lines = 123
    print("\n" * lines)


def perguntar():
    return input("Escolha uma opção: \n" +
                 "[A] - Adicionar estudante\n" +
                 "[P] - Pesquisar estudante\n" +
                 "[R] - Remover estudante\n" +
                 "[L] - Listar cursos: ").upper()


def adicionar(dicionario):
    clear()
    chave = int(input("código do estudante: "))
    for item in dicionario.items():
        if chave == int(item[0]):
            chave_existe = True
            break
        else:
            chave_existe = False

    if chave_existe:
        clear()
        print("==========================")
        print("Código de aluno ja existe!")
        print("==========================")
    else:
        nome, idade, sexo, curso, nota1, nota2 = [input("Nome: "), input("Idade: "),
                                                  input("Sexo: "), input("Curso: "),
                                                  input("Nota 1: "), input("Nota 2: ")]
        media = (float(nota1) + float(nota2)) / 2
        if media >= 8:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        dicionario[chave] = [nome, chave, idade, sexo, curso, str(media), situacao]


def pesquisar(dicionario):
    codigo = input("Código do aluno: ").upper()
    lista = dicionario.get(codigo)
    if lista:
        clear()
        print("Nome...........: " + lista[0])
        print("Código.........: " + lista[1])
        print("Idade..........: " + lista[2])
        print("Sexo...........: " + lista[3])
        print("Curso..........: " + lista[4])
        print("Média..........: " + lista[5])
        print("Situação.......: " + lista[6])
    else:
        print("\n==================")
        print("Código não existe!")
        print("==================")


def remover(dicionario):
    codigo, confirme = [input("Código do aluno: ").upper(),
                        input("Você tem certeza disso? [S/N]").upper()]
    if confirme == 'S':
        if dicionario.get(codigo):
            del dicionario[codigo]
            clear()
            print("==================")
            print("Registro excluído!")
            print("==================")
        else:
            clear()
            print("===========================")
            print("Código do aluno não existe!")
            print("===========================")


def listar_cursos(dicionario):
    clear()
    print("----------------")
    for item in dicionario.items():
        print("| ", item[1][4])
    print("----------------")
