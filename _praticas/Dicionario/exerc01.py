# tupla
emails = ["xpto@xyz.com", "xkcd@phd.com"]
print(emails)
print(emails[1],"\n")

tupla = list(enumerate(emails))
print(tupla)

for chave in range(0, len(tupla)):
  print(tupla[chave][1])

# dicionário de dados
print("\n\nPráticas de dicionários")
usuarios = {
    "chaves": ["Chaves do 8", "24/12/2017", "Recep_01"],
    "quico": ["Quico das Flores", "20/12/2017", "Raiox_03"]
}

for item in usuarios.items():
  # tupla = list(enumerate(item))
  print(item)

tupla = list(enumerate(usuarios))
print("\n",tupla)
print(usuarios.get('quico')[2])

print("\n\nTESTE EXEMPLO PRÁTICO")
alunos = {
  "121": ["Renan", "121", "25", "Masculino", "Engenharia", str(6.7), "Reprovado"],
  "122": ["Miya", "122", "23", "Feminino", "Psicologia", str(10.0), "Aprovado"],
  "123": ["Lucas", "123", "24", "Masculino", "TADS", str(8.7), "Aprovado"]
}
print(alunos)

# chave = 121
chave = int(input("código do estudante: "))
print("\nIterando o dicionario...")
for aluno in alunos.items():
    if (chave == int(aluno[0])):
      print(aluno[0])

# for item in alunos.items():
#   if chave == str(item[0]):
#     chave_existe = True
#   else:
#     chave_existe = False