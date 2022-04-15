from Module import *

# dicionary = {
#     "120":["Refrigerante", 5.70, "Bebidas", "14/04/2022", 10, 25],
#     "121":["Leite", 6.40, "Laticínios", "14/04/2022", 15, 5],
#     "122":["Bolo", 3.35, "Doces", "14/04/2022", 4, 54]
# }

option = options()
while option != 0:
    if option == 1:
        register()
    elif option == 2:
        print("opção 2")
    elif option == 3:
        code = input("Informe o código do produto: ")
        show("db.json", code)
    elif option == 4:
        print("opção 4")
    elif option == 5:
        print("opção 5")
    else:
        print("Opção inválida")
    option = options()


# with open("db.json", "w") as json_file:
#   json.dump(dicionary, json_file)

# with open("db.json", "r") as json_file:
#   dicionary = json.load(json_file)
#   for chave, valor in dicionary.items():
#     print(chave + " | " + str(valor))