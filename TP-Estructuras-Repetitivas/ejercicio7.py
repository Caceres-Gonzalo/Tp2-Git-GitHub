# Sumar todos los números entre 0 y un número positivo ingresado


limite = int(input("Ingrese un número entero positivo: "))
suma = sum(range(limite + 1))
print(f"La suma desde 0 hasta {limite} es: {suma}")
