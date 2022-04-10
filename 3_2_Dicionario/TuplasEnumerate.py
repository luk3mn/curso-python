import email


usuarios={} # cria o dicionário
resp="S" # controla o loop
emails=[] # cria a lista de emails

# repete enqunto a resposta for "S"
while resp=="S":
  # adiciona na lista de emails a entrada de novos emails
  emails.append(input("Digite um email: ").upper())
  # decide se continua ou encerra o loop
  resp=input("Digite <S> para continuar: ").upper()

# enumera cada elemento da lista e add em uma nova lista "tupla"
tupla=list(enumerate(emails))
# percorre e recupera os valores da tupla
for chave in range(0,len(tupla)):
  print("Email: ", tupla[chave][1])

  # add como [chave] a tupla e como [valor] as entradas com "nome" e "nível"
  usuarios[tupla[chave]]=[input("Digite o nome: "),input("Digite o nível: ")]

# imprime as saídas
for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])