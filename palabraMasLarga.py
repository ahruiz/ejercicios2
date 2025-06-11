#codigo para mostrar la palabra mas larga de un texto
from colorama import Fore   # funcion para resaltar texto

print("_" * 80) #linea de separacion en pantalla
print("Codigo para mostrar la palabra mas larga de un texto dado por el usuario....") # explicacion

mitexto = input(Fore.YELLOW + "Ingresa el texto:" + Fore.WHITE) #pedimos al usr insertar un texto

diccDeMitxt = mitexto.split() #se genera el diccionario agregando cada palabra del texto

palMasL = max(diccDeMitxt, key=len) #determinamos cual es la palambra mas larga en funcion de su longitud
longPalMasL= len(palMasL) #sacamos la longitud de la palabra mas larga

print(f"La palabra mas larga es: {Fore.YELLOW} {palMasL} {Fore.YELLOW} con una logitud de {longPalMasL} letras")
#mostramos resultados en pantalla
print("_" * 80)  #linea de separacion en pantalla