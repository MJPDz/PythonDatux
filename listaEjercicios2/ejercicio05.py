# Ejercicio 5

import os

def listar_elementos(path):
    for elemento in os.listdir(path):
        elemento_path = os.path.join(path, elemento)
        if os.path.isdir(elemento_path):
            listar_elementos(elemento_path)
        else:
            print(os.path.basename(elemento_path))


listar_elementos("D:\Programming course\Python course\DATUX\WorkSpace\PythonDatux/listaEjercicios1")