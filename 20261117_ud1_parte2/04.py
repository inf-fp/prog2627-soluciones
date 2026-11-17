cantidad = 0
suma = 0
mayor = 0
menor = 0

while True:
    texto = input("Introduce un número entero (0 para terminar): ")
    try:
        numero = int(texto)
    except ValueError:
        print("No es un valor válido")
        continue
    if numero == 0:
        break
    if cantidad == 0:  # el primer número inicializa mayor y menor
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    cantidad += 1
    suma += numero

if cantidad == 0:
    print("No se ha introducido un número entero")
else:
    print(f"Cantidad: {cantidad}")
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")
    print(f"Media: {round(suma / cantidad, 2)}")
