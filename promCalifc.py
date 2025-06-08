#codigo para calcular el promedio de las calificaciones capturadas por el usuario

print("_" * 80)
print("Captura tus calificaciones para obtener tu promedio....")

numCalific = int(input("Cuantas calificaciones quieres capturar: "))
calificaciones = []

for i in range(numCalific):
    miCalific = int(input(f"Captura tu calificacion {i + 1}: "))
    calificaciones.append(miCalific)

promedio = round(sum(calificaciones) / numCalific,2)
print(f"El promedio de las calificaciones capturadas es: {promedio}")
print("_" * 80)
