from Module import *

option = options()
while option != 0:
    if option == 1:
        register("db.json")
    elif option == 2:
        code = input("Informe a categoria:")
        show("db.json", cat_code=code)
    elif option == 3:
        code = input("Informe o código do produto: ")
        show("db.json", code=code)
    elif option == 4:
        code = input("Informe o código do produto: ")
        update("db.json", code)
    elif option == 5:
        code = input("Informe o código do produto: ")
        delete("db.json", code)
    else:
        print("Opção inválida")
    option = options()