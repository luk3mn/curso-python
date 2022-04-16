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

  keys=list()
  for key, values in dicionary.items():
    keys.append(int(key))
  new_key = max(keys)+1
  print(new_key)

  sysDate = date.today() # pega a hora atual
  [description, cat_code, price, category, quantity] = [
    input("Informe os dados do produto\nDescrição do produto:"),
    input("Código da categoria: "),
    input("Preço: "),
    input("Categoria: "),
    input("Quantidade: ")
  ]

  # registra dos dados de entrada no dicionario de dados
  dicionary[new_key]=[description, cat_code, float(price), category, str(sysDate), int(quantity)]
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

def options_update():
  option = input("O que deseja alterar"
                    "\n[1] Descrição"
                    "\n[2] Categoria"
                    "\n[3] Preço"
                    "\n[4} Quantidade"
                    "\n[0] Cancelar"
                    "\nEscolha um opção: ")
  return option


def update(file, code):
  dicionary = read_file(file)
  for key, values in dicionary.items():
    if code == key:
      print(values)
      option = options_update()
      while(option != "0"):
        if option != "0":
          new_value = input("Novo valor: ")
        if option == "1":
          values[0]=new_value # atribui novo valor ao dicionario
        if option == "2":
          values[1]=new_value
          if new_value == "1":
            values[3]="Bebidas"
          if new_value == "2":
            values[3]="Laticínios"
          if new_value == "3":
            values[3]="Doces"
        if option == "3":
          values[2]=new_value
        if option == "4":
          values[5]=new_value
        print(values)
        option = options_update()
  # salva no arquivo json o novo valor
  save_file(dicionary, file)


def delete(file, code):
  dicionary = read_file(file)
  print(dicionary[code])
  confirm = input("Você tem certeza disso? [S/N]: ").upper()
  if (confirm == "S"):
    del dicionary[code]
    print("Removido com sucesso!")
  # salva a remoção no arquivo json
  save_file(dicionary, file)