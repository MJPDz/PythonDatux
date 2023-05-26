from datetime import datetime

def registrarEvento(nombreArchivo, nombreEvento):
    fechaActual = datetime.now()
    formatoFecha = fechaActual.strftime("%Y-%m-%d %H:%M:%S")
    nombreLog = f"{nombreArchivo}.log"

    # Registro del evento en el archivo
    registro = f"[{formatoFecha}] Evento: {nombreEvento}\n"

    with open(nombreLog, "a") as archivoLog:
        archivoLog.write(registro)

    print(f"Evento registrado en el archivo {nombreLog}.")

nombreArchivo = "info" # info.log
nombreEvento = "Inicio del programa"
registrarEvento(nombreArchivo, nombreEvento)
