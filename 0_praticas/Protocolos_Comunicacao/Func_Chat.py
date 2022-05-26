from socket import *

def configuracao():
  servidor = "127.0.0.1"
  porta = 43210
  obj_socket = socket(AF_INET, SOCK_STREAM)
  return servidor, porta, obj_socket