# scraperUTN.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

def obtener_carreras_utn(guardar_csv: bool = True):
    """
    Obtiene la lista de carreras de grado de la UTN FRLP desde su sitio oficial.
    
    Parámetros:
        guardar_csv (bool): Si es True, guarda los datos en 'data/carreras_utn.csv'.
    
    Retorna:
        pd.DataFrame: DataFrame con las columnas [Universidad, Facultad, Carrera, Link Carrera]
    """
    
    url = "https://www.frlp.utn.edu.ar/carreras-grado"
    universidad = "UTN FRLP"
    facultad = "FRLP"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"⚠️ Error al acceder a la página: {response.status_code}")
        return pd.DataFrame()

    soup = BeautifulSoup(response.text, "html.parser")
    lista_carreras = []

    for h3 in soup.find_all("h3"):
        a_tag = h3.find("a")
        if a_tag:
            nombre = a_tag.get_text(strip=True)
            enlace = a_tag.get("href")
            if enlace and not enlace.startswith("http"):
                enlace = "https://www.frlp.utn.edu.ar/" + enlace.lstrip("/")
            
            lista_carreras.append({
                "Universidad": universidad,
                "Facultad": facultad,
                "Carrera": nombre,
                "Link Carrera": enlace
            })

    df = pd.DataFrame(lista_carreras)

    if guardar_csv:
        Path("data").mkdir(exist_ok=True)
        df.to_csv("data/carreras_utn.csv", index=False, encoding="utf-8")
        print("✅ Datos de carreras guardados en 'data/carreras_utn.csv'")

    return df
