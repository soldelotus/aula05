i = 1
soma = 0

qtd = int(input("Digite a quantidade de alunos: "))

while i <= qtd:
    notas = float(input(f"Digite a nota do {i} aluno: "))
    soma += notas
    i += 1

media = soma/qtd

print(f"A média é {media}")