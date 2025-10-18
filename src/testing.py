import pandas as pd

archivo_combinado = "data/carreras_todas.csv"
df_final = pd.read_csv(archivo_combinado)


print(df_final.head())     # Muestra las primeras 5 filas
print(df_final.shape)      # Muestra (filas, columnas)
print(df_final.columns)    # Muestra los nombres de las columnas
print(df_final["Universidad"].value_counts()) # Cantidad de valores por universidad<
