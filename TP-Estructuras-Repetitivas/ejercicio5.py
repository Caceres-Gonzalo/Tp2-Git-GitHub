# Juego para adivinar un número aleatorio entre 0 y 9

import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0 a 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"adivinaste en {intentos} intento(s).")
        break
