usuarios = {}
print(usuarios)

# dicionario de dados
usuarios = {
    "chaves": ["Chaves do 8", "24/12/2017", "Recep_01"],
    "quico": ["Quico das Flores", "20/12/2017", "Raiox_03"]
}
print(usuarios)

# atribuinda um novo usuário ao dicionario de dados
usuarios["florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]
print(usuarios)

# pegando os resgistros do dicionario
print("\n####-----#####")
print(usuarios.get("quico"))