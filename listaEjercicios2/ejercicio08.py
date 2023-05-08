# Ejerccio 8

def generarListaPrimos(step):
    listaPrimos = []
    for num in range(2, 100001, step):
        # si un número no tiene divisores entre 2 y su raíz cuadrada, 
        # entonces no tendrá divisores mayores a su raíz cuadrada
        if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
            listaPrimos.append(num)
    return listaPrimos

listaPrimos = generarListaPrimos(1)
for i,primo in enumerate(listaPrimos):
    if i%20 == 0:
        print("\n")
    print(primo, end=", ")