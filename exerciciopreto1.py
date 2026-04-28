reservatorio = 500
gasto = 30
ciclos = 0

while reservatorio > 0:
    reservatorio = reservatorio - gasto
    ciclos = ciclos + 1

print("Total de ciclos realizados:", ciclos)
