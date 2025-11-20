# ==============================================================================
# src/analysis/anomaly_detection.py
# Contiene la lógica para la detección de anomalías (Semana 3).
# ==============================================================================


from typing import List, Tuple, Callable
# Numpy se usa para cálculos estadísticos como la media, mediana y desviación estándar.
import numpy as np


def z_score_anomalies(data: List[float], threshold: float = 3.0) -> List[Tuple[int, float]]:
    """
    (Paso 3.1)
    Detecta anomalías (valores atípicos) usando el método Z-score.
    Es una función pura que devuelve los índices y valores de las anomalías.
    """
    if len(data) < 2:
        return []
     
    # Se calculan la media y la desviación estándar de los datos.
    mean = np.mean(data)
    std = np.std(data)
     
    if std == 0:
        # Si la desviación es 0, todos los datos son iguales, no hay anomalías.
        return []
     
    # El Z-score mide cuántas desviaciones estándar está un punto lejos de la media.
    z_scores = [(x - mean) / std for x in data]
     
    # Se identifican como anomalías los puntos que superan el umbral (threshold).
    anomalies = [
        (i, data[i]) 
        for i, z in enumerate(z_scores) 
        if abs(z) > threshold
    ]
     
    return anomalies

def mad_anomalies(data: List[float], threshold: float = 3.5) -> List[Tuple[int, float]]:
    """
    (Paso 3.1)
    Detecta anomalías usando MAD (Desviación Absoluta Mediana).
    Este método es más robusto (menos sensible) a los outliers extremos.
    """
    if len(data) < 2:
        return []
     
    # Se calcula la mediana de los datos.
    median = np.median(data)
     
    # Se calculan las desviaciones absolutas respecto a la mediana.
    deviations = [abs(x - median) for x in data]
    mad = np.median(deviations)
     
    if mad == 0:
        mad = 1e-10  # Se evita la división por cero.
     
    # Se calcula el Z-score modificado usando la mediana (MAD).
    modified_z_scores = [0.6745 * (x - median) / mad for x in data]
     
    # Se identifican las anomalías que superan el umbral.
    anomalies = [
        (i, data[i])
        for i, z in enumerate(modified_z_scores)
        if abs(z) > threshold
    ]
     
    return anomalies

def ensemble_anomaly_detection(data: List[float], detectors: List[Callable], voting: str = 'majority') -> List[Tuple[int, float]]:
    """
    (Paso 3.1 - Función de Orden Superior)
    Combina múltiples detectores de anomalías para obtener un resultado más confiable.
    """
    
    # Se aplican todos los detectores (ej. z_score, mad_anomalies) a los datos.
    all_detections = [detector(data) for detector in detectors]
     
    # Se cuentan cuántos detectores marcaron cada índice como una anomalía.
    anomaly_counts = {}
    for detections in all_detections:
        for idx, value in detections:
            anomaly_counts[idx] = anomaly_counts.get(idx, 0) + 1
     
    # Se define cuántos votos se necesitan para ser una anomalía final.
    if voting == 'majority':
        threshold = len(detectors) // 2 + 1
    else: # 'unanimous'
        threshold = len(detectors)
     
    # Se filtran las anomalías que cumplen con el umbral de votación.
    final_anomalies = [
        (idx, data[idx])
        for idx, count in anomaly_counts.items()
        if count >= threshold
        
    ]
     
    return sorted(final_anomalies, key=lambda x: x[0])
