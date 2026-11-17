def digito_mas_frecuente(n: int) -> int:
    df = 0 # Dígito más frecuente
    max_veces = 0 # Número máximo de apariciones

    # Recorre 0,1,2,3,4,5,6,7,8,9 (todas las cifras posibles)
    for digito in range(10): 
        veces = 0
        resto = n
        while resto > 0:
            if resto % 10 == digito:
                veces += 1
            resto //= 10
        if veces > max_veces:  # estricto: en empate se queda el menor
            max_veces = veces
            df = digito
    return df



# Programa principal
print(digito_mas_frecuente(122333))
print(digito_mas_frecuente(1122))
print(digito_mas_frecuente(9988776))
print(digito_mas_frecuente(1000))
