import json
import os

def options():
  options = int(input("[1] Cadastrar produto\n"
                      "[2] Listar produtos por categorias\n"
                      "[3] Pesquisar produto\n"
                      "[4] Atualizar produto\n"
                      "[5] Remover produto\n"
                      "[0] Encerrar\n"
                      "Escolha uma opção: "))
  return options


def read_file(file):
  if os.path.exists(file): # se o aquivo ja existe -> adiciona seus dados no dicionario
    with open(file, "r") as json_file:
      dicionary = json.load(json_file)
  else: # senão -> cria um novo dicionário
    dicionary = {}
  return dicionary


def register():
  print("Cadastar produto")

# MELHORAR A EXIBIÇÃO
def show(file, code):
  dicionary = read_file(file) # será passado o nome e endereço do arquivo  
  for key, values in dicionary.items():
    if code == key:
      print(values)