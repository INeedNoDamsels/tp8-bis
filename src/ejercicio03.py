# Manuel Bernabei @INeedNoDamsels
# UNRN - Intro. Ingeniería en Computación

"""
Unidad 3 - Diagramas de flujo de datos
TP 8 Bis - Ejercicio 3
"""

A = []
V = 0
suma_total = 0
suma_pares = 0
suma_impar = 0
promedio   = 0
negativos  = 0 # cantidad de números negativos
pnegativos = 0 # porcentaje de números negativos

print("Ingrese 10 números enteros (entre -15 y 50)")
for i in range(10):
    V = int(input(" >> "))
    assert -15 <= V <= 50, "Error, valor fuera de rango."

    if V < 0:
        negativos += 1

    A.append(V)

for j in range(10):
    suma_total += A[j]

    if j % 2 != 0: # Toma esta posición "par" ya que el programa comienza a contar desde 0.
        suma_pares += A[j]
    else:
        suma_impar += A[j]

promedio   = float(suma_total / 10)
pnegativos = (negativos * 100) / 10

print(f"\nVector {A}\nPromedio: {promedio}.  Negativos: % {pnegativos} \
\nSuma pares: {suma_pares}, impares: {suma_impar}. Total: {suma_total}")
