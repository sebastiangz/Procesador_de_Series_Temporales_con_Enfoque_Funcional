# ==============================================================================
# Tarea: Programación Funcional en Python
# Nombre: Abimael Villamar
# Script de Demostración del Avance 4 (Proyecto Final)
# ==============================================================================

import sys
import os
from functools import partial
from typing import List, Dict, Any

# Se agrega la carpeta 'src' a la ruta de Python para encontrar los módulos.
ruta_src = os.path.join(os.getcwd(), 'src')
if ruta_src not in sys.path:
    sys.path.append(ruta_src)

# --- Importaciones del Proyecto ---
from core.lazy_streams import cargar_calendario, leer_ventas_lazy
from core.pure_functions import media_movil, normalizar, sliding_window
from core.transformers import TimeSeriesPipeline

from analysis.pattern_matching import detect_seasonality
from analysis.anomaly_detection import z_score_anomalies

# (Importamos las funciones de visualización)
from visualization.dashboard import crear_dashboard, exportar_dashboard_html

# --- Definición de Rutas a los Datos Reales de Kaggle ---
RUTA_CALENDARIO = 'data/calendar.csv'
RUTA_VENTAS = 'data/sales_train_validation.csv'

# ==============================================================================
# FUNCIÓN PRINCIPAL DE LA DEMO
# ==============================================================================

def ejecutar_demo_completa():
    """
    Función principal que ejecuta la demostración del Avance 4.
    """
    print("=" * 60)
    print("DEMO DEL AVANCE 4: PROYECTO FINAL (Kaggle M5)")
    print("=" * 60)

    # --- 1. Carga de Datos (Lazy Evaluation) ---
    
    print("\n[Paso 1: Cargando datos de Kaggle...]")
    mapa_calendario = cargar_calendario(RUTA_CALENDARIO)
    if not mapa_calendario:
        print("No se pudo cargar el calendario. Terminando demo.")
        return
        
    generador_ventas = leer_ventas_lazy(RUTA_VENTAS, chunksize=1)
    
    print("Leyendo (con 'yield') el primer producto del archivo de ventas...")
    
    try:
        primer_chunk = next(generador_ventas) 
        primera_fila_producto = primer_chunk.iloc[0]
        id_producto = primera_fila_producto.get('id', 'ID Desconocido')
        
        serie_temporal_producto = []
        lista_de_dias_indices = [] # Ej: 'd_1', 'd_2', ...
        
        for dia_id, valor_venta in primera_fila_producto.items():
            # --- AQUÍ ESTABA EL ERROR ---
            # Se corrigió 'dia.startswith' por 'dia_id.startswith'
            if dia_id.startswith('d_'):
                serie_temporal_producto.append(float(valor_venta))
                lista_de_dias_indices.append(dia_id)
        
        print(f"Éxito. Analizando la serie para el producto: {id_producto}")

    except Exception as e:
        print(f"Error al pre-procesar la fila: {e}")
        return

    # --- 2. Detección de Anomalías (Semana 3) ---

    print("\n[Paso 2: Detección de Anomalías (Z-Score)]")
    anomalias = z_score_anomalies(serie_temporal_producto, threshold=3.0)
    if anomalias:
        print(f"--- Resultado: Se encontraron {len(anomalias)} anomalías. ---")
    else:
        print("--- Resultado: No se encontraron anomalías significativas. ---")

    # --- 3. Creación del Dashboard (Semana 4) ---
    
    print("\n[Paso 3: Creando Dashboard Interactivo...]")
    
    # Se obtienen las fechas legibles (ej: '2011-01-29') del calendario
    lista_de_fechas = [mapa_calendario.get(dia_id, {}).get('date', dia_id) for dia_id in lista_de_dias_indices]
    
    # Se llama a la función de visualización
    figura_dashboard = crear_dashboard(
        datos=serie_temporal_producto,
        anomalias=anomalias,
        dias=lista_de_fechas
    )
    
    # Se exporta el gráfico a un archivo HTML
    exportar_dashboard_html(figura_dashboard, nombre_archivo="reporte_ventas_final.html")

    print("\n" + "=" * 60)
    print("DEMO FINAL COMPLETADA")
    print("=" * 60)

# ==============================================================================
# LÍNEA DE EJECUCIÓN
# ==============================================================================
if __name__ == "__main__":
    ejecutar_demo_completa()