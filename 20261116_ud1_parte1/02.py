n = int(input("Introduce un número entero positivo: "))

candidato = n + 1

while True:
    es_primo = True

    # Si n=8 => candidato=9
    # Comprueba si es primo dividiendo 9 entre 2,3,4,5,6,7,8
    for divisor in range(2, candidato):
        if candidato % divisor == 0:
            es_primo = False
            break
    
    if es_primo:
        break
    candidato += 1

print(candidato)
