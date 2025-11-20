# ==============================================================================
# src/visualization/dashboard.py
# Contiene la lógica para la visualización (Semana 4).
# ==============================================================================

from typing import List, Dict, Optional
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Importamos la función de media móvil que ya creamos.
from core.pure_functions import media_movil

def crear_dashboard(datos: List[float], anomalias: List[Dict] = None, dias: List[str] = None):
    """
    (Paso 5.2)
    Crea un dashboard interactivo simple usando Plotly.
    Genera un gráfico con la serie original, la media móvil y las anomalías.
    """
    
    # 1. Crear la figura (nuestro "lienzo")
    fig = go.Figure()

    # 2. Añadir la Serie Original (las ventas diarias)
    fig.add_trace(
        go.Scatter(
            x=dias, # Eje X: los días (fechas)
            y=datos, # Eje Y: las ventas
            mode='lines',
            name='Ventas Diarias (Original)',
            line=dict(color='blue', width=1)
        )
    )

    # 3. Añadir la Media Móvil (Semana 1)
    # Usamos la función pura que ya teníamos
    ma = media_movil(datos, 30) # Usamos una ventana de 30 días
    ma_dias = dias[30-1:] # Ajustamos los días para que coincidan con la media móvil
    
    fig.add_trace(
        go.Scatter(
            x=ma_dias,
            y=ma,
            mode='lines',
            name='Media Móvil (30 Días)',
            line=dict(color='red', width=2)
        )
    )

    # 4. Añadir las Anomalías (Semana 3)
    if anomalias:
        indices_anomalias = [a[0] for a in anomalias]
        valores_anomalias = [a[1] for a in anomalias]
        # Obtenemos las fechas de las anomalías
        dias_anomalias = [dias[i] for i in indices_anomalias if i < len(dias)]
        
        fig.add_trace(
            go.Scatter(
                x=dias_anomalias,
                y=valores_anomalias,
                mode='markers',
                name='Anomalías Detectadas',
                marker=dict(color='red', size=10, symbol='x')
            )
        )

    # 5. Configurar el Layout (Títulos y Diseño)
    fig.update_layout(
        title_text="Análisis de Series Temporales de Ventas (Dashboard)",
        xaxis_title="Fecha",
        yaxis_title="Cantidad de Ventas",
        hovermode="x unified" # Muestra todos los datos de un día al pasar el mouse
    )
    
    return fig

def exportar_dashboard_html(figura: go.Figure, nombre_archivo: str = "reporte_ventas.html"):
    """
    Exporta la figura de Plotly a un archivo HTML interactivo.
    """
    try:
        figura.write_html(nombre_archivo)
        print(f"\nÉxito: Dashboard exportado a '{nombre_archivo}'")
        print("Puedes abrir este archivo en tu navegador para ver el gráfico interactivo.")
    except Exception as e:
        print(f"Error al exportar el dashboard: {e}")