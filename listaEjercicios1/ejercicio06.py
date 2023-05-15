#Ejercicio 6
# Realice un programa que calcule la suma de los números hasta el valor ingresado.
# Ejemplo: si se ingresa 5 se tendrá ue calcular 1+2+3+4+5

print("\n\t.:SUMA DE NUMEROS::.")
numero = int(input("Ingrese un número: "))
suma = int(numero*(numero+1)/2)
print(f"La suma del 1 al {numero} es: {suma}\n")