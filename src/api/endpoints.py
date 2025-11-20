# ==============================================================================
# src/api/endpoints.py
# Contiene la lógica para la API RESTful (Semana 4).
# ==============================================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import os
import sys

# --- Configuración de la Ruta de Importación ---
# Se agrega la carpeta 'src' a la ruta de Python para encontrar los módulos.
ruta_src = os.path.join(os.path.dirname(__file__), '..')
if ruta_src not in sys.path:
    sys.path.append(ruta_src)

# --- Importaciones del Proyecto ---
# (Importamos las funciones que ya creamos en semanas anteriores)
from core.pure_functions import media_movil, normalizar
from analysis.anomaly_detection import z_score_anomalies

# --- Modelos de Datos (para que FastAPI sepa qué esperar) ---
class TimeSeriesData(BaseModel):
    """Define cómo deben lucir los datos que el usuario nos envía."""
    valores: List[float]
    parametros: Optional[Dict] = {}

class AnalysisResponse(BaseModel):
    """Define cómo lucirá nuestra respuesta."""
    resultado: List | Dict
    parametros_usados: Optional[Dict] = {}

# ==============================================================================
# Creación de la Aplicación API
# (Este es el objeto 'app' que el error no encontraba)
# ==============================================================================
app = FastAPI(
    title="API Funcional de Series Temporales",
    description="Proyecto 2 - Procesamiento de Series Temporales con Enfoque Funcional",
    version="1.0.0"
)

@app.get("/")
def leer_raiz():
    """Endpoint principal para verificar que la API funciona."""
    return {"mensaje": "Bienvenido a la API de Análisis de Series Temporales"}

@app.post("/transformar/media_movil", response_model=AnalysisResponse)
async def api_media_movil(request: TimeSeriesData):
    """
    (Paso 5.1)
    Endpoint para calcular la media móvil.
    """
    try:
        # Se extraen los parámetros (si no existen, se usa 5)
        tamano_ventana = request.parametros.get('tamano_ventana', 5)
        
        # Se llama a nuestra función pura
        resultado = media_movil(request.valores, tamano_ventana)
        
        return AnalysisResponse(
            resultado=resultado,
            parametros_usados={'tamano_ventana': tamano_ventana}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/analizar/anomalias", response_model=AnalysisResponse)
async def api_detectar_anomalias(request: TimeSeriesData):
    """
    (Paso 5.1)
    Endpoint para detectar anomalías usando Z-score.
    """
    try:
        umbral = request.parametros.get('threshold', 3.0)
        
        # Se llama a nuestra función pura
        anomalias = z_score_anomalias(request.valores, umbral)
        
        # Se formatea el resultado para que sea más claro
        resultado_formateado = [{'indice': idx, 'valor': val} for idx, val in anomalias]
        
        return AnalysisResponse(
            resultado=resultado_formateado,
            parametros_usados={'metodo': 'zscore', 'threshold': umbral}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))