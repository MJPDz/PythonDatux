# Ejercicio 4

import sys

def imprimir_argumentos(*args):
    for arg in args:
        print(arg)

imprimir_argumentos(*sys.argv[1:])