#codigo para calcular el indice de masa corporal(IMC)
from colorama import Fore   #funcion para resaltar texto

print("*" * 80) # linea de separacion
print("Codigo para calculo de IMC segun el peso y la estatura....") # explicacion del codigo

peso = float(input("Introduce tu peso en Kgs           : ")) # puede que alguien capture peso con decimales
estatura = float(input("Introduce tu estatura en metros: "))  # para que sea en metros tiene que usar decimales

if estatura > 2.2:       #es muy dificil que una persona mida mas de 2.2 mts
    estatura = estatura / 100
    imc = round(peso / (estatura * estatura),2)  # si por error se captura en cent...hacemos la conversion a metros
else:
    imc = round(peso / (estatura * estatura),2)

print(" IMC menor a 16: DESNUTRICION")
print(" IMC 17 a 20   : BAJO PESO")
print(" IMC 21 a 25   : NORMAL")
print(" IMC 26 a 30   : SOBREPESO")         #tabla de imc's
print(" IMC 31 a 35   : OBESIDAD")
print(" IMC 36 a 40   : OBESIDAD MARCADA")
print(" IMC mayor a 49: OBESIDAD MORBIDA")

print(f"**********************************{Fore.YELLOW} Tu IMC es:  {imc} {Fore.WHITE} ")
print("*" * 80) #linea seaparadora