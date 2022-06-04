# Manuel Bernabei @INeedNoDamsels
# UNRN - Intro. Ingeniería en Computación

"""
Unidad 3 - Diagramas de flujo de datos
TP 8 Bis - Ejercicio 2
"""
import random

X = []
posicion  = 0
elementos = random.randint(8, 40)

print(f"Ingrese {elementos} números enteros:")
for i in range(elementos):
    numero = int(input(" >> "))
    X.append(numero)

    if numero < 0:
        posicion = i

if posicion > 0:
    print(f"La posición del último número negativo ingresado es: {posicion}")
else:
    print("No se ingresaron números negativos.")
