#codigo para sumar y mostrar la suma de 2 nums ingresados x el usr

print("-" * 80)
print("codigo para sumar dos numeros proporcionados por el usuario")

num1= input("ingresa el primer numero : ")
num2= input("ingresa el segundo numero: ")

if not num1.isdigit() or not num2.isdigit():
    print("Teclea numeros enteros.....")
    exit()

suma = num1 + num2

print(f"La suma de los numeros proporcionados es: {suma}")
print("-" * 80)