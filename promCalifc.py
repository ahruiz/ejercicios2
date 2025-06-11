#codigo para calcular el promedio de las calificaciones capturadas por el usuario

print("_" * 80) #linea de separacion en pantalla
print("Captura tus calificaciones para obtener tu promedio....")  #Explicacion

numCalific = int(input("Cuantas calificaciones quieres capturar: ")) #pedimos al usr cuantas calificaciones son
calificaciones = [] # e genera dicc/lista vacio(a)

for i in range(numCalific):
    miCalific = int(input(f"Captura tu calificacion {i + 1}: ")) # se genera ciclo en fiuncion del num de califs
    calificaciones.append(miCalific) #ingresamos cada calificacion al dicc o lista

promedio = round(sum(calificaciones) / numCalific,2) #determinamos el prom y lo redondeamos a 2 decimales
print(f"El promedio de las calificaciones capturadas es: {promedio}") #desplegamos resultados

print("_" * 80) #linea de separacion en pantalla
