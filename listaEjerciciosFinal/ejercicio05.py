import sqlite3

def leerDatos():
    # Conexión a la base de datos
    conexion = sqlite3.connect("basedatos.db")
    cursor = conexion.cursor()

    # Obtener todos los datos de la tabla tipo_cambio
    cursor.execute("SELECT * FROM tipo_cambio")
    datos = cursor.fetchall()

    # Iterar sobre los datos y mostrarlos
    for dato in datos:
        id, fecha, compra, venta = dato
        print(f"ID: {id}\nFecha: {fecha}\nCompra: {compra}\nVenta: {venta}")

    # Cerrar la conexión
    conexion.close()

leerDatos()