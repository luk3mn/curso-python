import json
import os
from datetime import date

# função para perguntar as opções ao usuário
def options():
  return int(input("[1] Cadastrar produto\n"
                   "[2] Listar produtos por categorias\n"
                   "[3] Pesquisar produto\n"
                   "[4] Atualizar produto\n"
                   "[5] Remover produto\n"
                   "[0] Encerrar\n"
                   "Escolha uma opção: "))


# carrega o arquivo para a leitura
def read_file(file):
  if os.path.exists(file): # se o aquivo ja existe -> adiciona seus dados no dicionario
    with open(file, "r") as json_file:
      dicionary = json.load(json_file)
  else: # senão -> cria um novo dicionário
    dicionary = {}
  return dicionary

# cria um novo arquivo passando os dados do dicionario para ele
def save_file(dicionary, file):
  with open(file, "w") as json_file:
    json.dump(dicionary, json_file)

# registra os dados do produto em um dicionario de dados
def register(file):
  # carrega os dados do arquivo para o dicionario de dados
  dicionary = read_file(file)
  sysDate = date.today() # pega a hora atual
  [description, prod_code, cat_code, price, category, quantity] = [
    input("Informe os dados do produto\nDescrição do produto:"),
    input("Código do produto: "),
    input("Código da categoria: "),
    input("Preço: "),
    input("Categoria: "),
    input("Quantidade: ")
  ]

  # registra dos dados de entrada no dicionario de dados
  dicionary[prod_code]=[description, cat_code, float(price), category, str(sysDate), int(quantity)]
  # salva os dados do dicionario do arquivo json
  save_file(dicionary, file)


def show(file, code=None, cat_code=None):
  dicionary = read_file(file) # será passado o nome e endereço do arquivo  
  for key, values in dicionary.items():
    if code == key:
      print("Cód. Produto...: ", key)
      print("Descrição......: ", values[0])
      print("Cód. Categoria.: ", values[1])
      print("Preço..........: ", "R$",values[2])
      print("Categoria......: ", values[3])
      print("Cadastrado em..: ", values[4])
      print("Quantidade.....: ", values[5])
    if cat_code == values[1]:
      print("Produto: {}\nCategoria: {}\n".format(values[0], values[3]))

def update(file, code):
  dicionary = read_file(file)
  for key, values in dicionary.items():
    if code == key:
      print(values)


def delete(file, code):
  dicionary = read_file(file)
  for key, values in dicionary.items():
    if code == key:
      print(values)