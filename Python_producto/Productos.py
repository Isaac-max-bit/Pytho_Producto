import pandas as pd

archivo = "Productos.cvs.xlsx"

df = pd.read_excel(archivo, engine='openpyxl')

print(df.head(10))  # Muestra las primeras 10 filas
print(df.tail(10))  # Muestra las últimas 10 filas
