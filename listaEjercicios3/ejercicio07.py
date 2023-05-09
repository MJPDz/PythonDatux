# Ejercicio 7

class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años y mide {self.altura} cm"