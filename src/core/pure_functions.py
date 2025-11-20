# ==============================================================================
# src/core/pure_functions.py
# Contiene las funciones puras para el análisis básico (Semana 1 y 2).
# ==============================================================================

from typing import List, Callable, Tuple, Optional
from functools import reduce
import numpy as np

# --- Funciones de Semana 1 (Día 5-6) ---
def media_movil(datos: List[float], tamano_ventana: int) -> List[float]:
    """
    (Paso 2.1)
    Calcula la media móvil de una serie de datos.
    Es una función pura: no modifica los datos de entrada.
    """
    if tamano_ventana <= 0 or tamano_ventana > len(datos):
        print(f"Advertencia: Tamaño de ventana {tamano_ventana} inválido.")
        return []
    
    return [
        sum(datos[i:i + tamano_ventana]) / tamano_ventana
        for i in range(len(datos) - tamano_ventana + 1)
    ]

def diferenciacion(datos: List[float], lag: int = 1) -> List[float]:
    """
    (Paso 2.1)
    Calcula la diferencia (cambio) entre elementos de una serie.
    Es una función pura.
    """
    if lag <= 0 or lag >= len(datos):
        print(f"Advertencia: Lag (retraso) {lag} inválido.")
        return []
    
    return [datos[i] - datos[i - lag] for i in range(lag, len(datos))]

# --- Funciones de Semana 2 (Día 3-4) ---

def normalizar(datos: List[float], metodo: str = 'minmax') -> Tuple[List[float], dict]:
    """
    (Paso 2.1)
    Normaliza una serie temporal (transformación de escala).
    Retorna los datos normalizados y los parámetros usados.
    """
    if not datos:
        return [], {}
     
    if metodo == 'minmax':
        min_val = min(datos)
        max_val = max(datos)
         
        if max_val == min_val:
            return [0.5] * len(datos), {'min': min_val, 'max': max_val}
         
        normalizados = [(x - min_val) / (max_val - min_val) for x in datos]
        parametros = {'min': min_val, 'max': max_val, 'method': 'minmax'}
         
    elif metodo == 'zscore':
        media = sum(datos) / len(datos)
        varianza = sum((x - media) ** 2 for x in datos) / len(datos)
        std = varianza ** 0.5
         
        if std == 0:
            return [0.0] * len(datos), {'mean': media, 'std': std}
         
        normalizados = [(x - media) / std for x in datos]
        parametros = {'mean': media, 'std': std, 'method': 'zscore'}
     
    else:
        raise ValueError(f"Método de normalización desconocido: {metodo}")
     
    return normalizados, parametros

# --- Funciones Adicionales del Pipeline (Paso 2.1) ---

def sliding_window(datos: List[float], tamano_ventana: int, step: int = 1) -> List[List[float]]:
    """
    (Paso 2.1)
    Crea ventanas deslizantes de una serie temporal.
    """
    if tamano_ventana <= 0 or tamano_ventana > len(datos):
        print(f"Advertencia: Tamaño de ventana {tamano_ventana} inválido.")
        return []
     
    return [
        datos[i:i + tamano_ventana]
        for i in range(0, len(datos) - tamano_ventana + 1, step)
    ]