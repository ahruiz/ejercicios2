#codigo para contar las letras de un texto dado por el usuario

print("_" * 80)
print("Codigo para contar las letras de un texto dado por el usuario")

texto = input("Ingrese una palabra o un texto: ")

espEnBco = texto.count(" ")
longDelTxt= len(texto)

longSinEsp= longDelTxt - espEnBco

print(f"La longitud del texto que insertaste es de: {longSinEsp} y {espEnBco} espacios en blanco")
print("_" * 80)