
dia = 1
soma = 0

maior = 0
menor = 0

while dia <= 7:
    colheita = int(input("Digite a colheita: "))

    soma = soma + colheita

    if dia == 1:
        maior = colheita
        menor = colheita
    else:
        if colheita > maior:
            maior = colheita
        if colheita < menor:
            menor = colheita

    dia = dia + 1

print("Total da semana:", soma)
print("Maior colheita:", maior)
print("Menor colheita:", menor)
