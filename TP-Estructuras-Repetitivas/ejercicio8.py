# Contar pares, impares, negativos y positivos en 100 números

pares = impares = negativos = positivos = 0
for _ in range(100): 
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n < 0:
        negativos += 1
    elif n > 0:
        positivos += 1
print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")
