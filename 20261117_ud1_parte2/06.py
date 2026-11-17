a = int(input("Introduce a: "))
b = int(input("Introduce b: "))

if a > b:
    print("No se pueden crear las tablas de multiplicar")
else:
    # Recorremos el rango a-b
    for n in range(a, b + 1):
        print(f"Tabla del {n}")

        # Mostramos la tabla de multiplicar
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

        # Si no es la última tabla, se introduce línea en blanco 
        if n != b:
            print()