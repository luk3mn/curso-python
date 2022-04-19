import getpass
import os
import json
import platform
from datetime import datetime

def login(dicionario):
  
  [usuario, senha] = [input("Informe seu login de acesso\nUsuário: "),
                    getpass.getpass("Senha: ")]
  
  for chave, valor in dicionario.items():
    if senha == chave and usuario == valor[0]:
      # print("Usuário: ", valor[0], "Senha: ", chave)
      return True


# carrega todos os dados de log exitente no arquivo de log
def carregar_dados_log(arquivo):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as arq_log:
      dicionario = json.load(arq_log)
  else:
    dicionario = {}
  return dicionario



def access_log(access, arquivo):
  if access:
    dicionario = carregar_dados_log(arquivo)
    
    [nome_maq, so, versao, usuario, data_hora] = [
      platform.node(), platform.system(),
      platform.version(), getpass.getuser(),
      datetime.now()
    ]

    # TAREFA: ATRIBUIR OUTRA CHAVE {EXP: USUÁRIO+VALOR_ALEATÓRIO}
    dicionario[usuario] = [nome_maq, so, versao, str(data_hora)]

    with open("sys_access.json", "w") as arq_log:
      json.dump(dicionario, arq_log)
    print(dicionario)

    # print("Nome do computador..................: ", nome_maq)
    # print("Nome do sistema operacional.........: ", so)
    # print("Versão do sistema Operacional.......: ", versao)
    # print("Nome de usuáiro.....................: ", usuario)
    # print("Data/Hora do Acesso.................: ", data_hora)