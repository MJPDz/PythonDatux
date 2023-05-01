#Ejercicio 6
# Realice un programa que calcule la suma de los números hasta el valor ingresado.
# Ejemplo: si se ingresa 5 se tendrá ue calcular 1+2+3+4+5

print("\n\t.:SUMA DE NUMEROS::.")
numero = int(input("Ingrese un número: "))
suma = 0
for i in range(1,numero+1):
    suma = suma + i
print(f"La suma de 1 a {numero} es: {suma}\n")