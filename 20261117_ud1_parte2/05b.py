import random

lanzamientos = int(input("¿Cuántas veces se lanza el dado? "))

cara1 = cara2 = cara3 = cara4 = cara5 = cara6 = 0
mas_frecuente = 1
maximo = 0

for _ in range(lanzamientos):
    cara = random.randint(1, 6)
    if cara == 1:
        cara1 += 1
        veces = cara1
    elif cara == 2:
        cara2 += 1
        veces = cara2
    elif cara == 3:
        cara3 += 1
        veces = cara3
    elif cara == 4:
        cara4 += 1
        veces = cara4
    elif cara == 5:
        cara5 += 1
        veces = cara5
    else:
        cara6 += 1
        veces = cara6

    # Solo la cara recién lanzada puede cambiar la más frecuente.
    # En empate gana la cara menor.
    if veces > maximo or (veces == maximo and cara < mas_frecuente):
        mas_frecuente = cara
        maximo = veces

print(f"Cara 1: {cara1} veces")
print(f"Cara 2: {cara2} veces")
print(f"Cara 3: {cara3} veces")
print(f"Cara 4: {cara4} veces")
print(f"Cara 5: {cara5} veces")
print(f"Cara 6: {cara6} veces")
print(f"La cara más frecuente es el {mas_frecuente}")
