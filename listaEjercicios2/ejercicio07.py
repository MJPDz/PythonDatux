# Ejercicio 7

texto = '''Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un 
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos 
y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 
años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando 
esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas Letraset, 
las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, 
como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'''

def contarPalabras(texto):
    palabras = texto.split()
    return len(palabras)

def contarAparicionesPalabra(texto, palabra):
    apariciones = texto.count(palabra)
    return apariciones

def reemplazarPalabra(texto, palabra_a_reemplazar, nueva_palabra):
    texto_modificado = texto.replace(palabra_a_reemplazar, nueva_palabra)
    return texto_modificado

texto_modificado = reemplazarPalabra(texto, 'texto', 'DATUX')

def mostrarResultado():
    print(f"\nCantidad de palabras en el texto: {contarPalabras(texto)}")
    print(f"\nCantidad de veces que aparece la palabra 'texto' en el texto: {contarAparicionesPalabra(texto, 'texto')}")
    print(f"\nTexto modificado: \n{texto_modificado}\n")

mostrarResultado()