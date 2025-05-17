nombre = input("Tu nombre: ")
opcion = int(input("Elegí 1-Mayús 2-Minús 3-Título: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")