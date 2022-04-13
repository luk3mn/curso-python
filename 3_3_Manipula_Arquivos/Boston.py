# Análise exploratória dos dados
with open("economic-indicators.csv", "r") as boston:
    for dado in boston.readlines()[1:-1]:
        lista = dado.split(",")
        print(lista)

########################################################
# DEVEREMOS BUSCAR AS RESPOSTAS ÀS SEGUINTES QUESTÕES: #
########################################################
# Qual o total de voos internacionais que partiram do aeroporto de Logan no ano de 2014?
with open("economic-indicators.csv", "r") as boston:
    total = 0
    for data in boston.readlines():
        lista = data.split(",")
        if lista[0] == '2014':
            total = total + int(lista[3])
    print("\nTotal de voos em 2014: ", total)


# Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?
with open("economic-indicators.csv", "r") as boston:
    maximo = 0
    for dado in boston.readlines()[1:-1]:
        lista = dado.split(",")
        if int(lista[2]) > int(maximo):
            maximo = lista[2]
            mes = lista[1]
            ano = lista[0]
    print("\nMaior trânsito de passageiros")
    print("Mês: {}, Ano: {}, Passageiros: {}".format(mes, ano, maximo))


# Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for especificado pelo usuário?
ano = input("\nInforme o ano: ")
with open('economic-indicators.csv', 'r') as boston:
    total_passageiros = 0;
    for dado in boston.readlines()[1:-1]:
        lista = dado.split(",")
        if lista[0] == ano:
            total_passageiros += int(lista[2])
    print("Total de passageiros no ano de {}: {}".format(ano, total_passageiros))


# Qual o mês que possui a maior média da diária de um hotel, com base no ano especificado pelo usuário?
media_maxima, ano = [0.0, input("\nInforme o ano: ")]
with open('economic-indicators.csv', 'r') as boston:
    for dado in boston.readlines()[1:-1]:
        lista = dado.split(",")
        if lista[0] == ano:
            if float(lista[5]) > media_maxima:
                media_maxima = float(lista[5])
                mes = lista[1]
    print("Mês: {}, Maior média diárias de um hotel: {}".format(mes, media_maxima))

# CONTINUAR EM: Um caminho para a portabilidade
