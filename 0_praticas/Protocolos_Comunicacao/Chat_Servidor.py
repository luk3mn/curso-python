from Func_Chat import *
from socket import *

# importando as configurações
servidor, porta, obj_socket = configuracao()

obj_socket.bind((servidor, porta)) # associando o servidor e a porta ao objeto socket
obj_socket.listen(2) # máximo de clientes que o servidor pode atender
print("Aguardando a resposta do cliente...")

while True: # o laço mantém o servidor executando até que seja desligado
  # aguarda a chamada de um cliente
  con, cliente = obj_socket.accept()
  print("Conectado com: ", cliente)
  while True:
    # limita o tamanho da mensagem em pacotes de 1024 Bytes
    msg_recebida = str(con.recv(1024))
    print("RECEBIDA: ", msg_recebida)

    # pergunta o conteúdo da mensagem
    # msg_enviada = bytes(input("MENSAGEM: "))
    # msg_enviada = bytes(input("MENSAGEM: "), 'utf-8')
    msg_enviada = b'Olah Cliente'
    con.send(msg_enviada) # envia a mensagem
    break
  con.close() # fecha a conexao atual