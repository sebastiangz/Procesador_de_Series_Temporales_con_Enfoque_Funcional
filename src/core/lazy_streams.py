# ==============================================================================
# src/core/lazy_streams.py
# Contiene la lógica para la lectura eficiente de datos (Lazy Evaluation).
# ==============================================================================

from typing import Iterator, Dict, Any
import pandas as pd
import os
import csv

def cargar_calendario(ruta_archivo: str) -> Dict[str, Dict[str, Any]]:
    """
    Carga el archivo 'calendar.csv' (que es pequeño) en un diccionario
    para usarlo como un "mapa" de consulta rápida (ej. 'd_1' -> 'Saturday').
    """
    mapa_calendario = {}
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo de calendario en {ruta_archivo}")
        return mapa_calendario
        
    try:
        with open(ruta_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # La clave 'd' (ej: d_1, d_2) es nuestro identificador único
                mapa_calendario[fila['d']] = fila
        print("Mapa del calendario cargado en memoria.")
        return mapa_calendario
    except Exception as e:
        print(f"Error al leer el calendario: {e}")
        return {}

def leer_ventas_lazy(ruta_archivo: str, chunksize: int = 1000) -> Iterator[pd.DataFrame]:
    """
    (Paso 2.2)
    Lee el archivo CSV de ventas (que es muy grande) en trozos (chunks)
    para un procesamiento 'lazy' (perezoso).
    
    En lugar de cargar todo el archivo, entrega un 'chunk' (un pedazo)
    del DataFrame a la vez.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo de ventas en {ruta_archivo}")
        yield from ()
        return

    print(f"Iniciando lectura 'lazy' (en chunks) de {ruta_archivo}...")
    
    # Usamos 'pd.read_csv' con 'chunksize' para crear un generador.
    try:
        with pd.read_csv(ruta_archivo, chunksize=chunksize) as lector:
            for chunk_df in lector:
                # 'yield' entrega el trozo de datos y pausa la función.
                yield chunk_df
    except Exception as e:
        print(f"Error durante la lectura del CSV: {e}")
        yield from ()