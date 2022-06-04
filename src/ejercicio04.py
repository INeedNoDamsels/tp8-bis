# Manuel Bernabei @INeedNoDamsels
# UNRN - Intro. Ingeniería en Computación

"""
Unidad 3 - Diagramas de flujo de datos
TP 8 Bis - Ejercicio 4
"""

extra   = 0
extra_b = 0
digitos = []
nombres = ["decenas de mil", "unidades de mil", "centenas", "decenas", "unidades"]
numero  = int(input("Ingrese un número entero (entre 999 y 99999): "))
assert 999 <= numero <= 99999, "Error, rango inválido."

for i in str(numero):
    digitos.append(i)

if len(digitos) == 5:
    extra = 2
elif len(digitos) == 4:
    extra   = 1
    extra_b = 1
else:
    extra_b = 2

if len(digitos) >= 3:
    if (digitos[0] == digitos[2 + extra]) and (digitos[1] == digitos[1 + extra]):
        print(f"¡{numero} es capicúa!")
    else:
        print(f"¡{numero} no es capicúa!")

for j in range(len(digitos)):
    print(f"{digitos[j]} {nombres[j + extra_b]}")
