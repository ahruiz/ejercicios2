#codigo para mostrar la palabra mas larga de un texto
from colorama import Fore

print("_" * 80)
print("Codigo para mostrar la palabra mas larga de un texto dado por el usuario....")

mitexto = input(Fore.YELLOW + "Ingresa el texto:" + Fore.WHITE)

diccDeMitxt = mitexto.split() #se genera el diccionario

palMasL = max(diccDeMitxt, key=len)
longPalMasL= len(palMasL) 
print("_" * 80)
print(f"La palabra mas larga es: {Fore.YELLOW} {palMasL} {Fore.YELLOW} con una logitud de {longPalMasL} letras")
print("_" * 80)