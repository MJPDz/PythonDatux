# EJERCICIO 3
# Ingrese 3 valores y realice las operaciones de suma ,resta ,
# multiplicación, división y división entera.

print("\n\t.:OPERACIONES BASICAS:.")
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))

print("\n-> SUMA")
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} + {num3} = {num1+num3}")
print(f"{num2} + {num3} = {num2+num3}")
print(f"{num1} + {num2} + {num3} = {num1+num2+num3}")

print("\n-> RESTA")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} - {num3} = {num1-num3}")
print(f"{num2} - {num1} = {num2-num1}")
print(f"{num2} - {num3} = {num2-num3}")
print(f"{num3} - {num1} = {num3-num1}")
print(f"{num3} - {num2} = {num3-num2}")

print("\n-> MULTIPLICACIÓN")
print(f"{num1} x {num2} = {num1*num2}")
print(f"{num1} x {num3} = {num1*num3}")
print(f"{num2} x {num3} = {num2*num3}")
print(f"{num1} x {num2} x {num3} = {num1*num2*num3}")

print("\n-> DIVISION")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} / {num3} = {num1/num3}")
print(f"{num2} / {num1} = {num2/num1}")
print(f"{num2} / {num3} = {num2/num3}")
print(f"{num3} / {num1} = {num3/num1}")
print(f"{num3} / {num2} = {num3/num2}")

print("\n-> DIVISION ENTERA")
print(f"{num1} // {num2} = {num1//num2}")
print(f"{num1} // {num3} = {num1//num3}")
print(f"{num2} // {num1} = {num2//num1}")
print(f"{num2} // {num3} = {num2//num3}")
print(f"{num3} // {num1} = {num3//num1}")
print(f"{num3} // {num2} = {num3//num2}")