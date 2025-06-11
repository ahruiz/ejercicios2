#codigo para contar las letras de un texto dado por el usuario

print("_" * 80) # linea separadora en pantalla
print("Codigo para contar las letras de un texto dado por el usuario")  #explicacion del codigo

texto = input("Ingrese una palabra o un texto: ") # se solicita al usr ingresar la palabra o texto

espEnBco = texto.count(" ")   #contamos los espacios en blanco
longDelTxt= len(texto)        #sacamos la longitud del testo con espacios en bco

longSinEsp= longDelTxt - espEnBco #calculamos la long sin espacios en bco

print(f"La longitud del texto que insertaste es de: {longSinEsp} caracteres mas {espEnBco} espacios en blanco")
print("_" * 80) # mostramos los datos y agregamos linea separadora de datos