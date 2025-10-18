# process.py
import pandas as pd
from pathlib import Path

def combinar_datos():
    """
    Combina los CSV de diferentes universidades en un único DataFrame
    y guarda el resultado en 'data/carreras_totales.csv'.
    """
    data_dir = Path("data")
    archivos = [data_dir / "carreras_unlp.csv", data_dir / "carreras_utn.csv"]
    
    dfs = []
    for archivo in archivos:
        if archivo.exists():
            print(f"📥 Leyendo {archivo.name}...")
            dfs.append(pd.read_csv(archivo))
        else:
            print(f"⚠️ Archivo no encontrado: {archivo.name}")
    
    if not dfs:
        print("❌ No hay archivos para combinar.")
        return
    
    df_total = pd.concat(dfs, ignore_index=True).drop_duplicates()
    output_path = data_dir / "carreras_totales.csv"
    df_total.to_csv(output_path, index=False, encoding="utf-8")
    
    print(f"✅ Datos combinados guardados en '{output_path}'")

if __name__ == "__main__":
    combinar_datos()
