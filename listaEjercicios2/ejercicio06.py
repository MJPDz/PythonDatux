# Ejercicio 6

def main():
    print("\n\t.::VALIDACIÓN DE EVENTO::.\n")
    # Pedir al usuario que ingrese información sobre el evento
    nombre = obtener_nombre()
    fecha = obtener_fecha()
    asistentes = obtener_asistentes()

    # Validar la información del evento
    if nombre != '' and fecha != '' and es_fecha_valida(fecha) and es_cantidad_valida(asistentes):
        print('El evento es válido')
    else:
        print('El evento no es válido')


def obtener_nombre():
    nombre = input('Ingrese el nombre del evento: ')
    return nombre


def obtener_fecha():
    fecha = input('Ingrese la fecha del evento (en formato DD/MM/AAAA): ')
    return fecha


def obtener_asistentes():
    asistentes = input('Ingrese la cantidad de asistentes esperados: ')
    return asistentes


def es_fecha_valida(fecha):
    fecha_valida = True
    fecha_lista = fecha.split('/')
    if len(fecha_lista) != 3:
        fecha_valida = False
    else:
        dia, mes, anio = fecha_lista
        if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
            fecha_valida = False
        else:
            dia, mes, anio = int(dia), int(mes), int(anio)
            if mes < 1 or mes > 12:
                fecha_valida = False
            elif dia < 1 or dia > dias_en_mes(mes, anio):
                fecha_valida = False
    if not fecha_valida:
        print('La fecha ingresada no es válida')
    return fecha_valida


def dias_en_mes(mes, anio):
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    elif mes in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def es_cantidad_valida(asistentes):
    if asistentes.isdigit() and int(asistentes) >= 0:
        return True
    else:
        print('La cantidad de asistentes ingresada no es válida')
        return False

main()