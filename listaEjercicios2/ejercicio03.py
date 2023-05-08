# Ejercicio 3

def mostrarPrograma():
    num1  = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese otro número: "))
    mayor = calcularMayor(num1,num2)
    if mayor is None:
        print("\nLos números son iguales...\n")
    else:
        print(f"\nEl mayor es: {mayor}\n")

def calcularMayor(num1, num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
    else:
        return None
    
mostrarPrograma()