def dividir(a, b):
    return a / b

def menu():
    opcion = ''
    while opcion != '2':
        print('Seleccione una opción:')
        print('1. Dividir dos números')
        print('2. Salir')

        opcion = input('Opción: ')

        if opcion == '1':
            num1 = float(input('Ingrese el primer número: '))
            num2 = float(input('Ingrese el segundo número: '))

            resultado = dividir(num1, num2)

            print(f'El resultado de la división es: {resultado}\n')
        elif opcion == '2':
            print('Adiós!\n')
        else:
            print('Opción no válida\n')
