ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite <S> para continuar: ").upper()

print("Exibindo ip´s: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

# print("Exibindo máquinas com o mesmo endereço: ")
# pesquisa=input("Digite os dois últimos octetos: ")
# for ip,nome in ips.items():
#     if(ip[1]==pesquisa):
#         print("Máquinas no mesmo endereço (redes diferentes)")
#         print(nome)

print("Exibir máquinas que compõem uma mesma rede")
pesquisa = input("Digite os dois primeiros octetos: ")
for rede,nome in ips.items():
  if rede[0] == pesquisa:
    # print("Máquinas na mesmo endereço (redes diferentes)")
    print(nome)