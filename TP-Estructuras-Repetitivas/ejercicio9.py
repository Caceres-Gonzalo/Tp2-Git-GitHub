# Calcular la media de 100 numeros ingresados

suma = 0
cantidad = 100 
for _ in range(cantidad):
    n = int(input("Ingrese un número: "))
    suma += n
media = suma / cantidad
print(f"La media es: {media}")
