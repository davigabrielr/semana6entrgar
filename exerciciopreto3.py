print("Loja das Oliveiras – Tabela de preços")

preco_unitario = 1.99

for quantidade in range(1, 51):
    total = quantidade * preco_unitario
    print(f"{quantidade} muda(s) – R$ {total:.2f}")
