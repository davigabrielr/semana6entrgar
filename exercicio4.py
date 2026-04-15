
contador = 0
soma = 0

while contador < 15:
    idade = int(input("Digite a idade do estudante: "))
    soma = soma + idade
    contador = contador + 1

media = soma / 15

print("Média da turma:", media)

if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
