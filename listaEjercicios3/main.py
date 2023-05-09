from ejercicio02 import Catalogo_,Producto_
from opciones.menu import menu
from ejercicio04 import Producto
import os
from ejercicio06 import *
from ejercicio07 import Persona
import sys

def ejercicio02():
    catalogo = Catalogo_()
    catalogo.agregar_producto(Producto_('Llanta', 50))
    catalogo.agregar_producto(Producto_('Batería', 100))
    catalogo.agregar_producto(Producto_('Aceite', 20))
    catalogo.mostrar_productos()

def ejercicio03():
    menu()

def ejercicio04():
    p = Producto('producto1', 'PERU-0001-2023')
    print(p.__str__())

def ejercicio05():
    try:
        p = Producto('producto1', 'PERU-00012023')
        print(p)
    except ValueError:
        print('Error: formato de código incorrecto')
        print('Ruta del directorio de trabajo:', os.getcwd())
    finally:
        print('Proceso terminado')

def ejercicio06():
    peli1=Pelicula("ant man",120,2020)
    peli2=Pelicula("mario b",80,2023)

    c1=Catalogo()
    c1.agregar(peli1)
    c1.agregar(peli2)
    c1.mostrar()

    print("Peliculas con duracion mayor a 100:")
    for i in c1.filtroDuracion(100):
        print(i)

    print("Peliculas estrenadas en 2020:")
    for i in c1.filtroRelease(2020):
        print(i)

def ejercicio07():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    altura = float(input("Ingrese la altura de la persona en cm: "))

    persona = Persona(nombre, edad, altura)
    print(persona)

def realizarOpcion(opc):
    match opc:
        case 1: sys.exit()
        case 2: ejercicio02()
        case 3: ejercicio03()
        case 4: ejercicio04()
        case 5: ejercicio05()
        case 6: ejercicio06()
        case 7: ejercicio07()

def mostrarMenu():
    while True:
        print("\n\t.:EJERCICOS 3 DATUX:.")
        print("\n1. Main.py")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Salir")
        while True:
            opc = int(input("Opción: "))
            if 0<opc<9:
                break
        if opc==8:
            print("\nSaliendo...\n")
            break
        else:
            print()
            realizarOpcion(opc)

if __name__ == '__main__':
    # Aquí va el código que se ejecutará si el archivo main.py se ejecuta como script principal
    mostrarMenu()