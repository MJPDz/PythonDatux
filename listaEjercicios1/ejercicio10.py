# Ejercicio 10
# Defina una lista de DNI's y otra lista de datos que tenga lista anidadas en donde si la
# posición del DNI es x la información se encuentra en la posición x de la lista de datos,
# pedir datos para validar si el usuario tiene permitido ingresar, validar que exista en
# la lista de DNI, que su edad sea mayor a 18 años y que sea datux en el curso de python
# Ejemplo: ['name',edad,'distrito','datux','curso:sql']

dnis = ['111', '222', '333', '444']
datos = [
    ['Juan', 25, 'Lima', 'datux', 'curso:python'], # Ingresa
    ['María', 30, 'Arequipa', 'otro', 'curso:python'], # No ingresa
    ['Pedro', 20, 'Cusco', 'datux', 'curso:sql'], # Ingresa
    ['Ana', 19, 'Lima', 'otro', 'curso:java'] # No ingresa
]

dni = input("Ingrese su DNI: ")

if dni in dnis:
    posicion = dnis.index(dni)
    nombre, edad, distrito, datux, curso = datos[posicion]
    if edad >= 18 and datux == "datux":
        print("Tiene permitido ingresar.")
        print(f"Bienvenido(a) {nombre}, usted tiene {edad} años y vive en {distrito}.")
    else:
        print("No tiene permitido ingresar.")
else:
    print("No tiene permitido ingresar.")