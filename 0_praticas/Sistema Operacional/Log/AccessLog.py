from Access import *
from datetime import datetime

usuarios = {"1998": ["lukemn", "19-04-2022"], "2030": ["renl", "18-04-2022"]}
dados_log = {}

logado, usuario = login("usuarios.json")
if logado == True:
  print("Logado!")
  access_log(logado, usuario, arquivo="sys_access.json")
else:
  print("Incorreto")