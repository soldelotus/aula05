senha = int(input("Digite sua senha do cartão: "))
tentativas = 1
pin = 123456

while pin != senha:
    senha = int(input("Senha incorreta! Digite novamente: "))
    tentativas += 1
    if tentativas >= 3:
        print("Tentativas excedidas, saindo do programa...")
        break

if pin == senha:
    print("Bem-vindo")




