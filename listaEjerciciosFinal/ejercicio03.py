import re

def validarCorreo(correo):
    formato = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(formato, correo):
        print(f"\nCorreo: {correo} \nResultado: El correo electrónico es válido.\n")
    else:
        print(f"\n{correo} \nResultado: El correo electrónico NO es válido.\n")

correo = "markojpd20@gmail.com"
validarCorreo(correo)