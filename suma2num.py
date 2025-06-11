#codigo para sumar y mostrar la suma de 2 nums ingresados x el usr

print("-" * 80) #linea de separacion en pantalla
print("codigo para sumar dos numeros proporcionados por el usuario") #Explicacion

num1= input("ingresa el primer numero : ")
num2= input("ingresa el segundo numero: ") #pedimos al usr capturar los numeros a sumar

if not num1.isdigit() or not num2.isdigit():
    print("Teclea numeros enteros.....")   # verificamos que los datos sean correctos
    exit()                                 # terminamos el proceso si no son correctos

suma = num1 + num2 # sumamos

print(f"La suma de los numeros proporcionados es: {suma}") # mostramos resultados

print("-" * 80) #linea de separacion en pantalla