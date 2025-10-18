from scraperUNLP import obtener_carreras_unlp
from scraperUTN import obtener_carreras_utn
from process import combinar_datos

# Obtener datos de ambas universidades
df_unlp = obtener_carreras_unlp()
df_utn = obtener_carreras_utn()

#Combinar y guardar los datos
df_universidades = combinar_datos()


