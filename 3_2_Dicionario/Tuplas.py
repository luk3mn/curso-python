# TEORIA:
# Lista envolvem 
# dados entre colchetes; 
# dicionário entre entre chaves; 
# tuplas entre parênteses

#

# dicionário de dados
usuarios = {}

# tupla
emails = ["xpto@xyz.com", "xkcd@phd.com"]

tupla = list(enumerate(emails))

# atribui valores
for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome "), input("Digite o nivel ")]

# lista os dicionários
for chave, dado in usuarios.items():
    print("Usuário.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])