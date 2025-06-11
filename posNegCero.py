#codigo para restar 2 (2do - 1ro)nums y detereminar si es +, - o cero

print("-" * 80) #linea de separacion en pantalla
print("codigo para restar dos numeros, el 2do del 1ro, proporcionados por el usuario") # Explicacion

num1= input("ingresa el primer numero : ") 
num2= input("ingresa el segundo numero: ") # se pide al usuario ingresar los numeros

if not num1.isdigit() or not num2.isdigit():
    print("Teclea numeros enteros.....") # comprobamos que lo datos ingresados sean correctos
    exit() #terminamos el proceso sin son erroneos
else:
    num1 = int(num1)
    num2 = int(num2) # si son correctos los convertimos a enteros

resta = num2 - num1 #realizamos la operacion

if resta > 0:
    print(f"El resultado es: {resta} positivo")
elif resta < 0:
    print(f"El resultado es: {resta} negativo") # se muestran los resultados: +, - o cero
else:
    print(f"El resultado es: {resta} cero")

print("-" * 80) #linea de separacion en pantalla