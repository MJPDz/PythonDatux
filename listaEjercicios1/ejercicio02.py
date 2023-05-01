# EJERCICIO 2
# Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado.

print("\t.:CALCULO DE AREAS:.")
print("-> CIRCULO")
radio = float(input("Ingrese el radio del circulo: "))
pi = 3.1416
area = pi*(radio*radio)
print(f"Area del cirulo: {area}\n")

print("-> TRIANGULO")
base = float(input("Ingese la base del triangulo: "))
altura = float(input("Ingrese la altura de triangulo: "))
area = (base*altura)/2
print(f"Area del triangulo: {area}\n")

print("-> CUADRADO")
lado = float(input("Ingrese el lado de cuadrado: "))
area = lado*lado
print(f"Area del cuadrado: {area}\n")