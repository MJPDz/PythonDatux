# Ejercicio 1

Numeros = [1,5,7,6,3,10,45,22,78,100]
Personas = [
    {"Nombre":"Pedro", "Edad": 21},
    {"Nombre":"Renzo", "Edad": 18},
    {"Nombre":"Alex", "Edad": 16},
    {"Nombre":"Paul", "Edad": 14},
    {"Nombre":"Guillermo", "Edad": 20},
    {"Nombre":"Ana", "Edad": 17},
    {"Nombre":"Luisa", "Edad": 15},
    {"Nombre":"Rodrigo", "Edad": 23},
    {"Nombre":"Valeria", "Edad": 19},
    {"Nombre":"Geraldine", "Edad": 10}
]

def dibujarCuadrado(lado):
    print()
    for i in range(lado):
        for j in range(lado):
            print("*", end=" ")
        print()
    print()

def multiplos2(numeros):
    print()
    for numero in numeros:
        if numero%2==0:
            print(f"-> {numero} es multiplo de 2")
    print()

def mayoresEdad(personas):
    print()
    mayores = []
    for persona in personas:
        if persona["Edad"] >= 18:
            mayores.append(persona)
    if mayores is not None:
        print("Mayores de edad: ")
        for persona in mayores:
            nombre = persona["Nombre"]
            edad = persona["Edad"]
            print(f"-> {nombre}, {edad} años")
    print()

def realizarOpcion(opc):
    match opc:
        case 1:
            while True:
                lado = int(input("Ingrese la longitud del cuadrado: "))
                if lado > 0:
                    dibujarCuadrado(lado)
                    break
        case 2: multiplos2(Numeros)
        case 3: mayoresEdad(Personas)

def mostrarMenu():
    while True:
        print("\n\t.:MENÚ DE OPCIONES:.")
        print("\n1. Dibujar cuadrado")
        print("2. Multiplos de 2")
        print("3. Mayores de edad")
        print("4. Salir")
        while True:
            opc = int(input("Opción: "))
            if 0<opc<5:
                break
        if opc==4:
            print()
            break
        else:
            realizarOpcion(opc)

mostrarMenu()