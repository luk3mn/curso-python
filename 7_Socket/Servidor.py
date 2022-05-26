# 1. importamos todas (*) as funções da biblioteca “socket”,
# isso será preciso para que possamos criar objetos do tipo “socket”.
from socket import *

# 2.
servidor = "127.0.0.1" # o servidor aqui é a própria máquina, também é representado pelo endereço “127.0.0.1”(localhost)
porta = 43210   # foi utilizada uma porta representada por um número inteiro entre 0 e 65535, visto que normalmente as
#                 portas entre 0 e 1023 são portas utilizadas, por padrão, para atribuições de serviços conhecidos por
#                 meio do sistema opera

# 3. criamos o nosso objeto socket “obj_socket”, por meio da função “socket()”, que exige dois parâmetros:
#    o primeiro definirá a família responsável por identificar os pacotes (AF_INET e AF_UNIX)
#    o segundo parâmetro refere-se ao transporte desse pacote (SOCK_STREAM pata o TCP e SOCK_DGRAM para o UDP)
obj_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET -> iremos utilizar a identificação do emissor/receptor do(s)
#                                            pacote(s) via DNS ou número IP (
obj_socket.bind((servidor, porta)) # fazemos a associação no nosso objeto socket com o nosso servidor e porta
obj_socket.listen(2)  # a função “listen()”, define o máximo de clientes que o servidor irá atender simultaneamente
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept()  # aguardamos a chamada de um cliente (por meio da função accept())
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))  # aguarda a solicitação que pode ser transmitida em pacotes de 1024 bytes
        print("Recebemos: ", msg_recebida)  # exibimos a mensagem recebida
        msg_enviada = b'Olah Cliente'   # geramos uma mensagem para enviar no formato de “bytes”, po isso o “b”+String
        con.send(msg_enviada)   # enviamos por meio do método “send()”
        break
    con.close() # fechamos a conexão e voltamos a aguardar uma nova conexão