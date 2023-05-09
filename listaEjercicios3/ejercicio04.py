# Ejercicio 4

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        pais, lote, anio = self.codigo.split('-')
        return f"Producto: {self.nombre}, país de origen: {pais}, número de lote: {lote}"
