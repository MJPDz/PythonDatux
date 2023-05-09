# Ejercicio 2

class Producto_:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre}: {self.precio}"


class Catalogo_:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)
            