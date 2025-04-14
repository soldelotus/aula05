valor1 = float(input("Digite o 1º valor: "))
valor2 = float(input("Digite o 2º valor: "))

while valor2 == 0:
    valor2 = float(input("Digite um valor válido que seja diferente de 0: "))

divisao = valor1/valor2
print(f"A divisão entre os dois números é {divisao}")