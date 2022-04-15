# CADASTRO DE USUÁRIO
from Functions import *

usuario = {}
opcao = escolha()

while opcao != 0:
    if opcao == 1:
        cadastrar(usuario)
    elif opcao == 2:
        pesquisar()
    elif opcao == 3:
        print("Opção 3")
    elif opcao == 4:
        remover()
    elif opcao == 0:
        print("Encerrando...")
    else:
        print("Opção inválida")
    opcao = escolha()

# print(type(str(usuario)))