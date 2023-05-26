import pandas as pd

def cargar_archivo_excel(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    return df

def filtrar_archivo(dataframe, columna, valor):
    df_filtrado = dataframe[dataframe[columna] == valor]
    return df_filtrado

ruta_archivo_excel = "D:/Prueba.xlsx"
dataframe = cargar_archivo_excel(ruta_archivo_excel)

columna_filtro = "Categoría"
valor_filtro = "Frutas"

df_filtrado = filtrar_archivo(dataframe, columna_filtro, valor_filtro)
print(df_filtrado)
