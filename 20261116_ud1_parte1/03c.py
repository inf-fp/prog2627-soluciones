def digito_mas_frecuente(n: int) -> int:
    numero = str(n)
    cifra_max = -1
    contador_max = 0

    # Recorre cifra a cifra del número convertido a str
    for cifra in numero:
        contador = 0

        # De la cifra selecciona, revisa cuántas coincidencias hay
        # Por lo menos, siempre hay 1 (ella misma)
        for a in numero:
            if a == cifra:
                contador += 1

        # Si es la cifra que más se repite, se seleccióna la cifra como la más frecuente
        if contador > contador_max:
            contador_max = contador
            cifra_max = int(cifra)

        # Si la cifra se repite tanto como otra anterior, se verifica cuál es la de menor valor
        if contador == contador_max:
            cifra_max = min(cifra_max, int(cifra))
                
    return int(cifra_max)



# Programa principal
print(digito_mas_frecuente(122333))
print(digito_mas_frecuente(1122))
print(digito_mas_frecuente(9988776))
print(digito_mas_frecuente(1000))
