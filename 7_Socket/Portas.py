import socket

# Com a execução desse código, teremos o retorno das portas que estamos disponibilizando.
print(socket.getservbyname("domain"))   # domínio (por padrão 53), usado para resolver a conversão entre DNS e IP
print(socket.getservbyname("http"))     # HTTP (por padrão 80), usado para navegar nas páginas WEB
print(socket.getservbyname("ftp"))      # FTP (por padrão 21), usado para transferência de arquivos