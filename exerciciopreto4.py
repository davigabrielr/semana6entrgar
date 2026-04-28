#que negocio dificil meu deus 
    while True:
        try:
            idade = int(input("Digite a idade (0 a 150): "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("Idade inválida. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def ler_salario():
    while True:
        try:
            salario = float(input("Digite o salário (maior que 0): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido. Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def ler_sexo():
    while True:
        sexo = input("Digite o sexo ('f' para feminino, 'm' para masculino): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Sexo inválido. Tente novamente.")

def ler_estado_civil():
    while True:
        estado_civil = input("Digite o estado civil ('s' solteiro, 'c' casado, 'v' viúvo, 'd' divorciado): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Estado civil inválido. Tente novamente.")

# Programa principal
print("Cadastro de trabalhador da plantação de oliveiras")
idade = ler_idade()
salario = ler_salario()
sexo = ler_sexo()
estado_civil = ler_estado_civil()

print("\nDados cadastrados com sucesso:")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
