frase = input("Escribí una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    print(frase + "!")
else:
    print(frase)