from ftplib import * # importação de todas as funções do módulo ftplib
ftp_ativo = False # variável booleana representando uma conecção passiva com valor 'False'
ftp = FTP('ftp.ibiblio.org') # objeto que representa a conexão FTP com o endereço do servidor FTP
print(ftp.getwelcome()) # vai representar uma mensagem padrão retornada pelo servidor
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")
ftp.login(usuario, senha) # responsavel por estabelecer a conexão com o servidor, caso não for informado usuario ou senha, então o acesso será anônimo
print("Diretorio atual de trabalho: ", ftp.pwd())
ftp.cwd('pub')
print("Diretorio corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit() # encerramos a conexão