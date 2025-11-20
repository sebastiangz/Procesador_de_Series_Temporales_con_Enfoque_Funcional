# ==============================================================================
# src/analysis/pattern_matching.py
# Contiene la lógica para la detección de patrones (Semana 3).
# ==============================================================================

from typing import List, Tuple, Dict, Optional
from functools import reduce
import numpy as np

# Importamos las funciones que creamos en la Semana 1 y 2.
from core.pure_functions import sliding_window, diferenciacion


def detect_peaks_and_valleys(data: List[float], threshold: float = 0.01) -> Dict[str, List[int]]:
    """
    (Paso 3.2)
    Detecta picos y valles en la serie temporal.
    Esto es una forma de 'pattern matching' (coincidencia de patrones).
    """
    if len(data) < 3:
        # Se necesitan al menos 3 puntos para encontrar un pico o valle.
        return {'peaks': [], 'valleys': []}
     
    peaks = []
    valleys = []
     
    # Se itera desde el segundo hasta el penúltimo elemento.
    for i in range(1, len(data) - 1):
        
        # Un patrón de pico: el punto es más alto que sus dos vecinos.
        if data[i] > data[i-1] and data[i] > data[i+1]:
            # El 'threshold' (umbral) evita detectar picos muy pequeños.
            if abs(data[i] - data[i-1]) > threshold or abs(data[i] - data[i+1]) > threshold:
                peaks.append(i)
         
        # Un patrón de valle: el punto es más bajo que sus dos vecinos.
        elif data[i] < data[i-1] and data[i] < data[i+1]:
            if abs(data[i-1] - data[i]) > threshold or abs(data[i+1] - data[i]) > threshold:
                valleys.append(i)
     
    return {'peaks': peaks, 'valleys': valleys}

def detect_trend(data: List[float], window_size: int = 10) -> List[str]:
    """
    (Paso 3.2)
    Detecta la tendencia (subida, bajada, o plana) en ventanas de la serie.
    Retorna una lista de las tendencias encontradas.
    """
    
    # Se usa la función que creamos en la Semana 2.
    windows = sliding_window(data, window_size)
     
    def classify_trend(window: List[float]) -> str:
        """Función interna para clasificar la tendencia de una sola ventana."""
        n = len(window)
        if n < 2:
            return 'plana'
         
        # Se calcula la pendiente usando una regresión lineal simple.
        x = list(range(n))
        x_mean = sum(x) / n
        y_mean = sum(window) / n
         
        numerator = sum((x[i] - x_mean) * (window[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))
         
        if denominator == 0:
            return 'plana'
         
        slope = numerator / denominator
         
        # Se clasifica la tendencia basado en la pendiente.
        if slope > 0.01:
            return 'subida'
        elif slope < -0.01:
            return 'bajada'
        else:
            return 'plana'
    
    # Se usa 'map' para aplicar la clasificación a cada ventana.
    return list(map(classify_trend, windows))

def detect_seasonality(data: List[float], max_period: int = 50) -> Optional[int]:
    """
    (Paso 3.2)
    Detecta el período de estacionalidad (ej. 7 para semanal)
    usando autocorrelación. Es una función pura.
    """
    if len(data) < max_period * 2:
        return None 
     
    def autocorrelation(lag: int) -> float:
        """Función interna pura para calcular la autocorrelación."""
        n = len(data) - lag
        if n <= 0: return 0.0
         
        mean = sum(data) / len(data)
        numerator = sum((data[i] - mean) * (data[i + lag] - mean) for i in range(n))
        denominator = sum((x - mean) ** 2 for x in data)
      
         
        return numerator / denominator if denominator > 0 else 0.0
     
    # Se calculan las autocorrelaciones para diferentes 'lags' (períodos).
    lags = range(2, min(max_period, len(data) // 2))
    autocorrs = [(lag, autocorrelation(lag)) for lag in lags]
     
    if not autocorrs:
        return None
     
    # Se busca el 'lag' (período) con la correlación más alta.
    best_lag, best_corr = max(autocorrs, key=lambda x: x[1])
     
    # Se retorna el período solo si la correlación es fuerte (mayor a 0.5).
    return best_lag if best_corr > 0.5 else None
