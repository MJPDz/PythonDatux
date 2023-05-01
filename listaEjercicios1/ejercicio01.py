# EJERCICIO 1
# Realizar un programa que ingrese sus datos personales e imprimirlos.

print("\nDATOS PERSONALES")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

mensaje = f'''
   .:Datos de la persona:.
-> Nombre: {nombre}
-> Apellido: {apellido}
-> Edad: {edad}
'''

print(mensaje)