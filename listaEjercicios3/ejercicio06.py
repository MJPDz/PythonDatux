# Ejercicio 6

class Pelicula:
    def __init__(self,titulo,duracion,release) -> None:
        self.titulo=titulo
        self.duracion=duracion
        self.release=release
    def __str__(self) -> str:
        return f"{self.titulo} se estreno el {self.release} y dura {self.duracion} minutos"

class Catalogo:
    listaPeliculas=[]
    def __init__(self) -> None:
        self.name="Catalogo Peliculas"
        self.listaPeliculas=[]
    def agregar(self, x):  # p será un objeto Pelicula
        self.listaPeliculas.append(x)
    def mostrar(self):
        for iterador in self.listaPeliculas:
            print(iterador)  # Print toma por defecto str(p)
    
    def filtroDuracion(self,duracion=0):
        resultadoFiltro=[]
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.duracion>duracion:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro
    
    def filtroRelease(self, release):
        resultadoFiltro = []
        for iteradorPelicula in self.listaPeliculas:
            if iteradorPelicula.release == release:
                resultadoFiltro.append(iteradorPelicula)
        return resultadoFiltro
