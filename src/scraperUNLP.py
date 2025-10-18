from bs4 import BeautifulSoup
import requests
import pandas as pd

def obtener_carreras_unlp():
    url = "https://unlp.edu.ar/ensenanza/carreras_de_grado/carreras-de-grado-unlp-10909-15909/"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("❌ No se pudo acceder a la página.")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    datos = []

    # Buscamos todos los <ul> de la página
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            a_tag = li.find("a")
            if a_tag:
                carrera = a_tag.get_text(strip=True)
                link = a_tag.get("href")
                datos.append({
                    "Universidad": "UNLP",
                    "Facultad": None,  # Podés intentar inferirla si hay otra etiqueta cerca
                    "Carrera": carrera,
                    "Link Carrera": link
                })

    if datos:
        df = pd.DataFrame(datos)
        df.to_csv("data/carreras_unlp.csv", index=False)
        print(f"✅ Se encontraron {len(datos)} carreras y se guardaron en 'data/carreras_unlp.csv'")
    else:
        print("⚠️ No se encontraron carreras.")
    
    return datos
