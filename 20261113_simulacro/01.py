def aproximar_pi(terminos: int) -> float:
    suma = 0
    for i in range(terminos):
        suma += (-1) ** i / (2 * i + 1)
    return round(4 * suma, 6)

# Programa principal
print("Con 1 términos:", aproximar_pi(1))
print("Con 10 términos:", aproximar_pi(10))
print("Con 100 términos:", aproximar_pi(100))
print("Con 1000 términos:", aproximar_pi(1000))
