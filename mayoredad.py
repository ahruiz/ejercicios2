#codigo para generar cartelera de cine segun la edad

print("*" * 80)
print("Mostrar cartelera de cine segun la edad.....")

cartelara = {"LA SIRENITA": "A", "EL EXORCISTA": "R", "PINOCHO": "A", "50 SOMBRAS DE GRAY": "R"}

edad = int(input("Introduce tu edad para mostrarte la cartelera: "))

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
            print(clave) 
else:
    for clave,valor in cartelara.items():
        print(clave)
#ESTAS SENTENCIAS IF... ARROJAN LOS DATOS SIN EL FORMATO DE DICCIONARIO

print("*" * 80)