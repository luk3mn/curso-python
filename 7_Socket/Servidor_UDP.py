from socket import *
servidor = "127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_DGRAM) # 'DGRAM' determina que está sendo utilizado o protocolo UDP
obj_socket.bind((servidor, porta)) # Associa a porta e o servidor especificado
print("Servidor pronto....")

while True:
  dados, origem = obj_socket.recvfrom(65535) # aguarda os dados do cliente, com o tamanho limitado a 65535
  print("Origem..........: ", origem) # Exibe a origem
  print("Dados recebidos.: ", dados.decode()) # Exibe os dados, e o decode exibe os bytes no formato string
  resposta=input("Digite a resposta: ")
  obj_socket.sendto(resposta.encode(), origem) # 'encode' que converte de string para bytes e 'origem' é para onde vamos enviar a mensagem
obj_socket.close()