# Dicioário
# - nunca teremos dois objetos com a mesma chave no dicionario
#

# Criando um dicionário de dados
usuarios={}

#
usuarios={
  "chave":["dado1","dado2","dado3"],
  "Chaves":["Chaves Silve","17/06/2017","Recep_01"],
  "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
}
# Estrutura do dicionário
# Chaves -> Login (chave)
# [...] -> dados (valor)

# print("\n",usuarios)

# Caso o coloque dois objetos com a mesma chave,
# o segundo objeto irá sobreescrever o primeiro

pessoa={}
pessoa={
  "123":["Lucas","Masculino","24","Rua A"]
}

# adicionando item no dicionario
pessoa["124"]=["Renan","Masculino","20","Rua B"]


print("\n",pessoa)
print("##############========#########")
print("Dados: ",pessoa.get("123"))


# CONTINUAR
# TUPLAS -> Pág.5 do conteúdo digital