# Ejercicio 9
# Muestre las siguientes opciones 1. Agregar a lista de Python, 2. Agregar a lista de SQL,
# 3. Agregar a lista Power BI y al final mostrar las 3 listas
# Nota: Solo se ejecuta un vez

python = []
sql = []
powerBI = []
listas = [python,sql,powerBI]
elemento = input("\nIngrese un elemento: ")
print("\n1. Agregar a lista de Python")
print("2. Agregar a lista de SQL")
print("3. Agregar a lista de Power BI")
opcion = int(input("Opción: "))

if opcion == 1:
    listas[0].append(elemento)
elif opcion == 2:
    listas[1].append(elemento)
elif opcion == 3:
    listas[2].append(elemento)
else:
    print("La opcion no es valida\n")

print(f"\nLista de Python: {listas[0]}")
print(f"Lista de SQL: {listas[1]}")
print(f"Lista de Power BI: {listas[2]}")