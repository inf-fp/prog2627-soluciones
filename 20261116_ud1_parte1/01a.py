# Alternativa A

n = int(input("Número de filas (1-9): "))

for i in range(1, n + 1):
    fila = ""
    for j in range(1, i + 1):
        fila += str(j)
    print(fila)
