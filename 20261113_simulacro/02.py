"""Ejercicio 2. Comprobador de contraseñas.

Pide contraseñas al usuario y muestra su nivel de seguridad ("débil", "media"
o "fuerte") hasta que introduce una contraseña fuerte o escribe "salir".
"""

LONGITUD_MINIMA = 8

def tiene_mayuscula(password: str) -> bool:
    for c in password:
        if c.isupper():
            return True
    return False


def tiene_digito(password: str) -> bool:
    for c in password:
        if c.isdigit():
            return True
    return False


def tiene_simbolo(password: str) -> bool:
    for c in password:
        if c in "!@#$%&*?":
            return True
    return False


def nivel_seguridad(password: str) -> str:
    if password == "":
        raise ValueError("La contraseña está vacía")

    puntos = 0
    if len(password) >= LONGITUD_MINIMA:
        puntos += 1
    if tiene_mayuscula(password):
        puntos += 1
    if tiene_digito(password):
        puntos += 1
    if tiene_simbolo(password):
        puntos += 1

    if puntos <= 1:
        return "débil"
    if puntos <= 3:
        return "media"
    return "fuerte"



# Programa principal
intentos = 0
while True:
    password = input("Contraseña: ")
    if password == "salir":
        print("Sin contraseña válida")
        break

    intentos += 1
    try:
        nivel = nivel_seguridad(password)
    except ValueError:
        print("La contraseña no puede estar vacía")
        continue

    print("La seguridad de la contraseña es", nivel)
    if nivel == "fuerte":
        print("Se han necesitado", intentos, "intentos")
        break

