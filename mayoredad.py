#codigo para generar cartelera de cine segun la edad

print("*" * 80) # linea de separacion
print("Mostrar cartelera de cine segun la edad.....") #explicacion del codigo

cartelara = {"LA SIRENITA": "A", "EL EXORCISTA": "R", "PINOCHO": "A", "50 SOMBRAS DE GRAY": "R"}
#diccionario con cartelera y clasificacion

edad = int(input("Introduce tu edad para mostrarte la cartelera: ")) # se pide al usuario capturar su edad

# cartmenores = [key for key, value in cartelara.items() if value == "A"]
# cartmayores = [key for key, value in cartelara.items() if value == "R"] + cartmenores

# if edad >= 18:
#     print(f"nuestra cartelera es: {cartmayores}")
# else:
#     print(f"Nuestra cartelera es: {cartmenores} son clasificacion A:para toda la familia")
#ESTAS DOS SENTENCIAS ANTERIORES ARROJAN EL FORMATO DE DICCIONARIO en el print

if edad < 18:
    for clave, valor in cartelara.items():
        if valor == "A": 
            print(clave) #imprime solo las carteleras con clasificacion A
else:
    for clave,valor in cartelara.items():
        print(clave) #imprime todos los valores
#ESTAS SENTENCIAS print... ARROJAN LOS DATOS SIN EL FORMATO DE DICCIONARIO

print("*" * 80)