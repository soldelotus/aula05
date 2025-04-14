pergunta = "S"
while pergunta == "S":

    nota1 = float(input("Digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Valor inválido, digite novamente a primeira nota: "))


    nota2 = float(input("Digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Valor inválido, digite novamente a segunda nota: "))
    break

media = (nota1 + nota2) /2
print(f"A média é {media}")
pergunta = input("Deseja realizar um novo cálculo? Escreva S ou N: ")



