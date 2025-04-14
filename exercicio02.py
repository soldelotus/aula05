i = 1
soma = 0
tam = 10

while i <= tam:
    num = float(input("Digite um valor: "))
    soma = soma + num
    i = i + 1

media = soma/10
print(f"A média destes valores é: {media}")