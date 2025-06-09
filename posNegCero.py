#codigo para restar 2 (2do - 1ro)nums ingresados x el usr

print("-" * 80)
print("codigo para restar dos numeros, el 2do del 1ro, proporcionados por el usuario")

num1= input("ingresa el primer numero : ")
num2= input("ingresa el segundo numero: ")

if not num1.isdigit() or not num2.isdigit():
    print("Teclea numeros enteros.....")
    exit()
else:
    num1 = int(num1)
    num2 = int(num2)

resta = num2 - num1

print(f"La resta de los numeros proporcionados es: {resta}")
print("-" * 80)