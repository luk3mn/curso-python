# open("<caminho>","<arquivo>","<ação>")
# obs1: caso não seja indicado o caminho, o python considera o local do 
#       do código-fonte, ".py", para criar o arquivo ".txt"
#       exemplo: "c:\meus_aquivos\teste.txt"
# valor "r" -> significa que o arquivo será aberto somente para leitura
# valor "w" -> significa que o arquivo será aberto somente para escrita
with open("teste.txt", "w") as arquivo:
    # método de escrita no arquivo
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")
