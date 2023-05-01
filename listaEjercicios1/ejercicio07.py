# Ejercicio 7
'''
Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos:
    - Si los dos números son iguales
    - Si los dos números son diferentes
    - Si el primero es mayor que el segundo
    - Si el segundo es mayor o igual que el primero
'''

print("\n\t.::COMPARACIÓN DE NÚMEROS::.")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 == num2:
    print("\nLos números son iguales")
else:
    print("\nLos números son diferentes")
    if num1 > num2:
        print("El primero es mayor que el segundo")
    elif num2 >= num1:
        print("El segundo es mayor o igual que el primero")
print()