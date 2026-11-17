# Alternativa B

n = int(input("Número de filas (1-9): "))

for i in range(n):
    for j in range(i + 1):
        print(j + 1, end="")
    print()
