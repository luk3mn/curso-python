import socket   # Importando a biblioteca socket
resp = "S"  # Criando uma variável para controlar o nosso laço, que virá na sequência
while resp == "S":  # enquanto digitar a letra “s”, o código continuará perguntando uma url e exibindo o seu IP
    url = input("Digite uma url: ")  # variável “url” que simplesmente irá armazenar o domínio que está tentando localizar o IP
    ip = socket.gethostbyname(url)  # gethostbyname() é um método pertencente à classe socket, que recebe uma URL e retorna o IP.
    print("O IP referente à url informada é: ", ip) # Por fim, exibimos o IP na tela para o usuário
    resp = input("Digite <S> para continuar: ").upper()