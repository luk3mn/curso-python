from ftplib import *
ftp = FTP('ftp.ibiblio.org') # cria a conexão FTP
print(ftp.getwelcome())
ftp.login() # estabelecer o login
ftp.cwd('/pub/linux/logos/pictures') # definir o diretorio
with open ('pai_do_linux.jpg', 'wb') as arq:
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write)
ftp.quit()