# Importamos as funções da biblioteca socket
from socket import *

# criação das duas variáveis que reresentam o servidor e a porta
servidor = "127.0.0.1"  # localhost, se o servidor não for a máquina local, definir o IP do servidor externo utilizado
porta = 43210  # a porta deve ser a mesma em que inicializamos o servidor

# definição do conteúdo da variável “msg”, por meio de uma entrada do usuário (input) com a função “bytes()”
# OBS: o socket transmite somente dados do tipo byte
msg = bytes(input("Digite algo: "), 'utf-8')  # a função converte o conteúdo do input, de string para o formato bytes
obj_socket = socket(AF_INET, SOCK_STREAM)  # criação do objeto socket por meio da função “socket()”
obj_socket.connect((servidor, porta))  # conexão com o servidor, por meio da função “connect()”
obj_socket.send(msg)  # envia uma mensagem para o servidor, utilizando o método “send()”
resposta = obj_socket.recv(1024)  # a resposta recebe os dados enviado pelo servidor, com tamanho máximo de 1024 bytes
print("Recebemos: ", resposta)  # exibi a resposta
obj_socket.close()  # Fecha a conexão
