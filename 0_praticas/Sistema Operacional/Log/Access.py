import platform
import getpass
import random
import json
import os
from datetime import datetime

# Mecanismo de login
def login(dicionario):
  
  [usuario, senha] = [input("Informe seu login de acesso\nUsuário: "),
                    getpass.getpass("Senha: ")]
  
  for chave, valor in dicionario.items():
    if senha == chave and usuario == valor[0]:
      # print("Usuário: ", valor[0], "Senha: ", chave)
      return True, usuario


# carrega todos os dados de log exitente no arquivo de log
def carregar_dados_log(arquivo):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as arq_log:
      dicionario = json.load(arq_log)
  else:
    dicionario = {}
  return dicionario


# 
def grava_dados_log(dicionario, arquivo):
  with open(arquivo, "w") as arq_log:
      json.dump(dicionario, arq_log)


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
    grava_dados_log(dicionario, arquivo)
    print(dicionario)