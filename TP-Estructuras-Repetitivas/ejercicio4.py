# Sumar números ingresados hasta que el usuario ingrese 0

total = 0
while True:
    n = int(input("Ingrese un número (0 para terminar): "))
    if n == 0:
        break
    total += n
print(f"Suma total: {total}")
