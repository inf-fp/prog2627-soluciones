def digito_mas_frecuente(n: int) -> int:
    texto = str(n)
    mejor = "0"
    max_veces = 0

    # Recorre 0,1,2,3,4,5,6,7,8,9 (todas las cifras posibles)
    for digito in "0123456789":
        veces = texto.count(digito)
        if veces > max_veces:  # estricto: en empate se queda el menor
            max_veces = veces
            mejor = digito
    
    return int(mejor)



# Programa principal
print(digito_mas_frecuente(122333))
print(digito_mas_frecuente(1122))
print(digito_mas_frecuente(9988776))
print(digito_mas_frecuente(1000))
