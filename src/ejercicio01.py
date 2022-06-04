# Manuel Bernabei @INeedNoDamsels
# UNRN - Intro. Ingeniería en Computación

"""
Unidad 3 - Diagramas de flujo de datos
TP 8 Bis - Ejercicio 1
"""
import random

pos = 0 # cantidad nros. pos
neg = 0 # cantidad nros. neg
cer     = 0 # cantidad cer
V = []
N = random.randint(1, 9) # cantidad elementos del vector V

for i in range(N):
    V.append(random.randint(-9, 9))

print(V)

for i in range(N):
    if V[i] < 0:
        neg += 1
    elif V[i] > 0:
        pos += 1
    else:
        cer += 1
print(f"Positivos: {pos}\nNegativos: {neg}\nCeros    : {cer}")
