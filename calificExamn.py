#Codigo para calcular la calificacion en base a los aciertos

print("*" * 80) # linea de separacion en pantalla
print("Codigo para calificacion de examen de acuerdo al # de aciertos.....")   #explicacion

numPreg = input("ingresa el numero de preguntas en el examen: ")
numAciertos = input("ingresa el numero de ACIERTOS          : ") # pedimos al usuario introducir datos
numFallas = input("ingresa cuantas respondiste MAL          : ")

if not numPreg.isdigit() or not numAciertos.isdigit() or not numFallas.isdigit():
    print("Favor de introducir numeros enteros.....")    # comprobamos que los datos ingresados sean corrects
    exit()   #salimos del prog sin son incorrects
else:
    numPreg = int(numPreg)
    numAciertos = int(numAciertos)  #conversion de datos a enteros
    numFallas = int(numFallas)

totPreg = numAciertos + numFallas   # determinamos el tot de preguntas
    

if totPreg > numPreg or totPreg < numPreg:
    print("El num de ACIERTOS mas el num de FALLAS no coincide con el num de preguntas")
    exit()   #comprobamos que las cantidades coincidan


calif = round((numAciertos / numPreg) * 100,2) # calculamos el prom y lo redondeamos a dos decimales 

print(f"La calificacion de acuerdo a tus datos es de: {calif}") #mostramos el resultado

print("*" * 80) # linea de separacion en pantalla
