import os
from ftplib import *
ftp_ativo = False # configuramos nossa variável para uma conexão passiva
ftp = FTP(input("Digite o FTP que se deseja conectar: ")) # definimos  o  objeto  “ftp”,que   representará   nossa   conexão conforme  o  que  o  usuário  digitar
print(ftp.getwelcome()) # mensagem de boas-vindas
usuario = input("Digite o usuário: ") # solicita usuario
senha = input("Digite a senha: ") # solicita senha
ftp.login(usuario, senha)
print("Conexão bem sucedida. Diretório atual de trabalho: ", ftp.pwd())
menu = '1' # menu de interação
while menu == '1' or menu == '2' or menu == '3':
  menu = input("Escolha a opção desejada: "
               "\n<1> - para LIstar arquivos"
               "\n<2> - para definir um diretório"
               "\n<3> - para baixar um arquivo: ")
  if menu == '1': # se 1 -> iremos  exibir  uma listagem do diretório atual
    print(ftp.dir())
  elif menu == '2': # se 2 -> iremos mudar de diretório  de  acordo  com  o  que o  usuário  digitar
    ftp.cwd(input("Digite o diretório que deseja entrar: "))
    print("Diretório corrente é: ", ftp.pwd())
  elif menu == '3': # se 3 -> iremos perguntar o que ele deseja baixar
    tipo=input("Digite <B> para arquivo binário ou qualquer outra para arquivo ASCII: ").upper()
    if tipo == "B": # se binário -> deverá digitar a letra “b”
      with open(input("Digite o nome do arquivo do destino: "), 'wb') as arq:
        ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
    else: # se (qualquer letra != B) -> 
      with open(input("Digite o nome do arquivo de destino: "), 'w') as arq:
        def escreverLinha(data):
          arq.write(data)
          arq.write(os.linesep)
        ftp.retrlines('RETR ' + input("Arquivo de origem: "), escreverLinha)
    print("Arquivo baixado com sucesso!")
    ftp.quit()
