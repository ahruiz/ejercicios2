#Codigo para calcular la calificacion en base a los aciertos

print("*" * 80)
print("Codigo para calificacion de examen de acuerdo al # de aciertos.....")

numPreg = input("ingresa el numero de preguntas en el examen: ")
numAciertos = input("ingresa el numero de ACIERTOS          : ")
numFallas = input("ingresa cuantas respondiste MAL          : ")

if not numPreg.isdigit() or not numAciertos.isdigit() or not numFallas.isdigit():
    print("Favor de introducir numeros enteros.....")
    exit()
else:
    numPreg = int(numPreg)
    numAciertos = int(numAciertos)
    numFallas = int(numFallas)

totPreg = numAciertos + numFallas
    

if totPreg > numPreg or totPreg < numPreg:
    print("El num de ACIERTOS mas el num de FALLAS no coincide con el num de preguntas")
    exit()


calif = round((numAciertos / numPreg) * 100,2)

print(f"La calificacion de acuerdo a tus datos es de: {calif}")