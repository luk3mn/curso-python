import json
from Access import *
import platform
from datetime import datetime

usuarios = {"1998": ["lukemn", "19-04-2022"], "2030": ["renl", "18-04-2022"]}
dados_log = {}

logado = login(usuarios)
if logado == True:
  print("Logado!")
  access_log(logado, arquivo="sys_access.json")
else:
  print("Incorreto")