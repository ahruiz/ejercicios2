#codigo p/generar num aleatoria e intento de adivinar
import random    #funcion para crear nums aleatoriamente

print("-" * 80) # linea de separacion en pantalla
print("Se genera num aleatorio OCULTO y el usuario intenta adivinarlo")    # explicacion de la funcion del codigo

numAleat = random.randint(1,10)   # se genera un num aleatorio escondido

miNum = int(input("ingresa el numero que crees que se genero: ")) #pedimos al usuario que adivine

if miNum == numAleat:
    print(f"Este es el numero escondido: {numAleat}") #mostramos el numero y la felicitacion
    print("¡¡¡FELICIDADES!!! Has ganado un cupon, acertaste el numero oculto")
else:
    print(f"Este es el numero escondido: {numAleat}") #mostramos el numero e invitamos a participar de nuevo
    print("MALA SUERTE.....intentalo de nuevo")

print("-" * 80) # linea de separacion en pantalla