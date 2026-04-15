
oliveiras = 37  
tentativa = int(input("Tente adivinhar o número de oliveiras (1 a 100): "))

while tentativa != oliveiras:
    if tentativa < oliveiras:
        print("Há mais oliveiras, tente um número maior")
    else:
        print("Há menos oliveiras, tente um número menor")

    tentativa = int(input("Tente novamente: "))

print("Parabéns! Você descobriu a quantidade de oliveiras!")
