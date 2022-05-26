from urllib import response
from Func_Chat import *
from socket import *

# importando as configurações
servidor, porta, obj_socket = configuracao()

# converte o conteúdo do input, de string para o formato bytes
obj_socket.connect((servidor, porta)) # realiza a conexão com o servidor

while True:
  # # aguarda a chamada de um cliente
  # con, cliente = obj_socket.accept()
  # print("Conectado com: ", cliente)
  
  # while True:
  msg = bytes(input("Digite algo: "), 'utf-8')
  obj_socket.send(msg)

  # limita o tamanho da resposta para 1024 bytes
  respossta = obj_socket.recv(1024)
  print("RECEBIDA: ", respossta)
  obj_socket.close() # fecha a conexão
