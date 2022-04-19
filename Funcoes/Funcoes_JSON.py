import json
import os


def chamarMenu():
    escolha = int(input("Digite: "
                        "\n<1> para registrar ativo"
                        "\n<2> para exibir ativos armazenados: "))
    return escolha


def ler_arquivo(arquivo):
    if os.path.exists(arquivo):  # se o arquivo existir [True], então, preencha o dicionário com o conteúdo do arquivo
        with open(arquivo, "r") as arq_json:
            # dicionario = {} -> ANTES, AGORA DEVE COMEÇAR PREENCHENDO COM O QUE EXISTE NO ARQUIVO JSON
            dicionario = json.load(arq_json)    # CARREGA NO MODELO "LEITURA" TUDO QUE ESTÁ NO ARQUIVO JSON
    else:   # caso contrário (se o arquivo não existir [False]), crie o dicionário “inventario” vazio
        dicionario = {}
    return dicionario


def gravar_arquivo(dicionario, arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)


def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario, arquivo)
    return "JSON gerado!!!!"


def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])
