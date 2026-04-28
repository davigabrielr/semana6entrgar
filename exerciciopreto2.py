idade = int(input("Digite a idade da oliveira (em anos): "))

altura = idade * 30 / 100

print("Altura estimada:", altura, "metros")

if altura > 5:
    print("Oliveira adulta")
else:
    print("Oliveira em crescimento")
