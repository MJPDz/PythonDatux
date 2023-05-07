# Ejercicio 2

categorias = ["Programación","Base de Datos","Redes"]
estados = ["Libre","Prestado"]
libros = [
    {"Nombre":"Progra1", "Autor": "Datux1", "Categoría":categorias[0], "Estado":estados[0]},
    {"Nombre":"Progra2", "Autor": "Datux2", "Categoría":categorias[0], "Estado":estados[0]},
    {"Nombre":"Progra3", "Autor": "Datux3", "Categoría":categorias[0], "Estado":estados[0]},
    {"Nombre":"BD1", "Autor": "Datux4", "Categoría":categorias[1], "Estado":estados[0]},
    {"Nombre":"BD2", "Autor": "Datux5", "Categoría":categorias[1], "Estado":estados[0]},
    {"Nombre":"BD3", "Autor": "Datux6", "Categoría":categorias[1], "Estado":estados[0]},
    {"Nombre":"Redes1", "Autor": "Datux7", "Categoría":categorias[2], "Estado":estados[0]},
    {"Nombre":"Redes2", "Autor": "Datux8", "Categoría":categorias[2], "Estado":estados[0]},
    {"Nombre":"Redes3", "Autor": "Datux9", "Categoría":categorias[2], "Estado":estados[0]}
]
usuarios = [
    {"Nombre":"Pedro", "Edad": 21},
    {"Nombre":"Ana", "Edad": 17},
    {"Nombre":"Martin", "Edad": 23},
    {"Nombre":"Valeria", "Edad": 19},
    {"Nombre":"Geraldine", "Edad": 10}
]

def mostrarCategorias(categorias):
    print()
    for categoria in categorias:
        print(f"-> {categoria}")
    print()

def mostrarLibros(libros):
    print()
    for i,libro in enumerate(libros):
        nombre = libro["Nombre"]
        autor = libro["Autor"]
        print(f"-> Libro {i+1}")
        print(f"Nombre: {nombre}\nAutor: {autor}\n")
    print()

def cambiarEstado(libro,usuario):
    libro["Estado"] = estados[1]
    nombre = libro["Nombre"]
    autor = libro["Autor"]
    cat = libro["Categoría"]
    estado = libro["Estado"]

    print(f"\nLibro prestado a {usuario}")
    print(f"-> Nombre: {nombre}\n-> Autor: {autor}\n-> Categoría: {cat}\n-> Estado: {estado}")

def prestarLibro():
    print()
    band = False
    nombre = input("Ingrese el usuario: ")
    for usuario in usuarios:
        if usuario["Nombre"] == nombre:
            band = True
            break
    if band:
        band = False
        lib = input("Ingrese el Nombre del Libro: ")
        for libro in libros:
            if libro["Nombre"] == lib:
                 band = True
                 cambiarEstado(libro,nombre)
                 break
        if not band:
            print("No tenemos ese libro...")
    else:
        print("El usuario no está registrado...")

def mostrarUsuarios(usuarios):
    print()
    for usuario in usuarios:
        nombre = usuario["Nombre"]
        edad = usuario["Edad"]
        print(f"-> {nombre}, {edad} años")
    print()

def realizarOpcion(opc):
    match opc:
        case 1: mostrarCategorias(categorias)
        case 2: mostrarLibros(libros)
        case 3: prestarLibro()
        case 4: mostrarUsuarios(usuarios)

def mostrarMenu():
    while True:
        print("\n\t.:BIBLIOTECA DATUX:.")
        print("\n1. Mostrar Categorias")
        print("2. Mostrar Libros")
        print("3. Prestamo de Libro")
        print("4. Mostrar Usuarios")
        print("5. Salir")
        while True:
            opc = int(input("Opción: "))
            if 0<opc<6:
                break
        if opc==5:
            print("\nGracias por usar la Biblioteca!!!\n")
            break
        else:
            realizarOpcion(opc)

mostrarMenu()