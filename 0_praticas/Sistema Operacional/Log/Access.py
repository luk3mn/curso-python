from datetime import datetime
import platform
import getpass
import random
import json
import os


# carrega os dados de usuário para um dicionario de dados
def carrega_dados_usuario(arquivo):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as arq_usuario:
      dicionario = json.load(arq_usuario)
  else:
    dicionario = {}
  return dicionario


#
# def gravar_dados_usuario(dicionario, arquivo):
#   with open(arquivo, "w") as arq_usuario:
#     json.dump(dicionario, arq_usuario)


# carrega todos os dados de log exitente no arquivo de log
def carregar_dados_log(arquivo):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as arq_log:
      dicionario = json.load(arq_log)
  else:
    dicionario = {}
  return dicionario


# grava no arquivo json os dados de log
def gravar_dados_log(dicionario, arquivo):
  with open(arquivo, "w") as arq_log:
      json.dump(dicionario, arq_log)


# Mecanismo de login
def login(arquivo):
  
  # trás os dados do usuário do json para o dicionario de dados
  dicionario = carrega_dados_usuario(arquivo)

  [usuario, senha] = [input("Informe seu login de acesso\nUsuário: "),
                    getpass.getpass("Senha: ")]
  
  for chave, valor in dicionario.items():
    if senha == chave and usuario == valor[0]:
      # print("Usuário: ", valor[0], "Senha: ", chave)
      return True, usuario


# Mecanismo que add no dic
def access_log(access, usuario, arquivo):
  if access:
    dicionario = carregar_dados_log(arquivo)
    
    [nome_maq, so, versao, usuario_so, data_hora] = [
      platform.node(), platform.system(),
      platform.version(), getpass.getuser(),
      datetime.now()
    ]
    
    # gera um id aleatório para cada acesso
    _id = ''
    for x in range(0,3):
      _id = _id + str(random.randrange(10,99))

    # TAREFA: ATRIBUIR OUTRA CHAVE {EXP: USUÁRIO+VALOR_ALEATÓRIO}
    dicionario[usuario+_id] = [nome_maq, so, usuario_so, versao, str(data_hora)]

    # chama a função que grava o log no json
    gravar_dados_log(dicionario, arquivo)
    print(dicionario)