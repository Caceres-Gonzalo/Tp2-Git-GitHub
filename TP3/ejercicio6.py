import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
prom = mean(numeros_aleatorios)
med = median(numeros_aleatorios)
mod = mode(numeros_aleatorios)

print("Media:", prom)
print("Mediana:", med)
print("Moda:", mod)

if prom > med and med > mod:
    print("Sesgo positivo")
elif prom < med and med < mod:
    print("Sesgo negativo")
else:
    print("Sin sesgo")