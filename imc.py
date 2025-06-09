#codigo para calcular el indice de masa corporal(IMC)
from colorama import Fore

print("*" * 80)
print("Codigo para calculo de IMC segun el peso y la estatura....")

peso = float(input("Introduce tu peso en Kgs           : "))
estatura = float(input("Introduce tu estatura en metros: "))

if estatura > 2.2:
    estatura = estatura / 100
    imc = round(peso / (estatura * estatura),2)
else:
    imc = round(peso / (estatura * estatura),2)

print(" IMC menor a 16: DESNUTRICION")
print(" IMC 17 a 20   : BAJO PESO")
print(" IMC 21 a 25   : NORMAL")
print(" IMC 26 a 30   : SOBREPESO")
print(" IMC 31 a 35   : OBESIDAD")
print(" IMC 36 a 40   : OBESIDAD MARCADA")
print(" IMC mayor a 49: OBESIDAD MORBIDA")

print(f"**********************************{Fore.YELLOW} Tu IMC es:  {imc} {Fore.WHITE} ")
print("*" * 80)