import requests
import sqlite3

def obtenerDatos():
    # Conexión a la API y obtención de los datos
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    response = requests.get(url)
    data = response.json()

    # Extracción de los datos relevantes de la API
    fecha = data["fecha"]
    compra = data["compra"]
    venta = data["venta"]

    # Conexión a la base de datos
    conexion = sqlite3.connect("basedatos.db")
    cursor = conexion.cursor()

    # Creación de la tabla si no existe
    cursor.execute("""
        CREATE TABLE tipo_cambio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    """)

    # Inserción de los datos en la base de datos
    cursor.execute("""
        INSERT INTO tipo_cambio (fecha, compra, venta) VALUES (?, ?, ?)
    """, (fecha, compra, venta))

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

    print("Datos guardados en la BD")

obtenerDatos()