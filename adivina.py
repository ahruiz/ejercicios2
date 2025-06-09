#codigo p/generar num aleatoria e intento de adivinar
import random

print("-" * 80)
print("Se genera num aleatorio y el usuario intenta adivinarlo")

numAleat = random.randint(1,10)

miNum = int(input("ingresa el numero que crees que se genero: "))

if miNum == numAleat:
    print("¡¡¡FELICIDADES!!! Has ganado un cupon, acertaste el numero oculto")
else:
    print("MALA SUERTE.....intentalo de nuevo")