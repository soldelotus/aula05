tentativas = 1
pin = 123456
mensagem="Senha Bloqueada"

while tentativas <= 3:
    senha = int(input("Digite sua senha: "))
    if senha == pin:
        mensagem = "Bem-vindo"
        break
    tentativas += 1
print(mensagem)




