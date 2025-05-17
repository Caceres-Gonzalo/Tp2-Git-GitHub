# Sumar los enteros entre dos valores pero exculyendolos

a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
inicio = min(a, b) + 1
fin = max(a, b)
suma = sum(range(inicio, fin))
print(f"La suma de los números entre {a} y {b} es: {suma}")
