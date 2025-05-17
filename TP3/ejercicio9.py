mag = float(input("Magnitud del terremoto: "))
if mag < 3:
    print("Muy leve")
elif mag < 4:
    print("Leve")
elif mag < 5:
    print("Moderado")
elif mag < 6:
    print("Fuerte")
elif mag < 7:
    print("Muy Fuerte")
else:
    print("Extremo")