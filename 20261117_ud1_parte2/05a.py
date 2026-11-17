import random

lanzamientos = int(input("¿Cuántas veces se lanza el dado? "))

cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0

# Lanzamientos de dado y conteo
for l in range(lanzamientos):
    cara = random.randint(1, 6) # Simular lanzamiento de dado de 6 caras
    if cara == 1:
        cara1 += 1
    elif cara == 2:
        cara2 += 1
    elif cara == 3:
        cara3 += 1
    elif cara == 4:
        cara4 += 1
    elif cara == 5:
        cara5 += 1
    else:
        cara6 += 1

print(f"Cara 1: {cara1} veces")
print(f"Cara 2: {cara2} veces")
print(f"Cara 3: {cara3} veces")
print(f"Cara 4: {cara4} veces")
print(f"Cara 5: {cara5} veces")
print(f"Cara 6: {cara6} veces")

# Comparaciones estrictas: en caso de empate se queda la cara menor
mas_frecuente = 1 # Suponemos que la cara 1 es la más frecuente
maximo = cara1 # Guardamos el número de veces que salío la cara 1

# Comprobaos cara a cara si es más frecuente que la guardada
if cara2 > maximo:
    mas_frecuente = 2
    maximo = cara2
if cara3 > maximo:
    mas_frecuente = 3
    maximo = cara3
if cara4 > maximo:
    mas_frecuente = 4
    maximo = cara4
if cara5 > maximo:
    mas_frecuente = 5
    maximo = cara5
if cara6 > maximo:
    mas_frecuente = 6
    maximo = cara6

print(f"La cara más frecuente es el {mas_frecuente}")
