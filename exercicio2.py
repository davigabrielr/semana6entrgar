
mudas = int(input("quantidade de mudas: "))
fileiras = int(input("quantidade de fileiras:"))

divisao = mudas / fileiras
resto = mudas % fileiras

print("ficara ", round(divisao), 'em cada fileira')
if resto == 0:
    print("não sobra nada")
else:
    print("sobram", resto,"mudas.")
