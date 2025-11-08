# 📈 Proyecto 2: Procesador de Series Temporales con Enfoque Funcional

## 📋 Descripción del Proyecto

Sistema funcional que procesa y analiza la serie temporal de ventas del restaurante "Las Hamacas del Mayor". El sistema implementa transformaciones, filtrados y agregaciones (basado en el dataset M5 de Kaggle) manteniendo los principios de funciones puras e inmutabilidad.

**Universidad de Colima - Ingeniería en Computación Inteligente**
**Materia**: Programación Funcional
**Profesor**: Gonzalez Zepeda Sebastian
**Semestre**: Agosto 2025 - Enero 2026

---

## 🎯 Objetivos

- Implementar **funciones puras** para la transformación de series temporales.
- Aplicar **lazy evaluation** (evaluación perezosa) con generadores para el manejo eficiente de grandes datasets (M5).
- Usar **composición de funciones** para crear pipelines de análisis.
- Aplicar **funciones de orden superior** (`map`, `filter`, `reduce`) en el análisis temporal.
- Utilizar **recursión** para algoritmos de procesamiento.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.11+
- **Paradigma**: Programación Funcional
- **Librerías (requirements.txt)**:
  - `pandas` (Para la lectura inicial del CSV)
  - `numpy` (Para cálculos numéricos)
  - `statsmodels` (Para análisis estadístico)
  - `matplotlib` (Para visualización)
  - `fastapi` (Para la API final)
  - `plotly` (Para el dashboard final)
  - `rx` (Para programación reactiva, si se alcanza)

---

## 📦 Instalación

```bash
# 1. Clonar el repositorio
git clone [https://github.com/sebastiangz/Procesador_de_Series_Temporales_con_Enfoque_Funcional.git](https://github.com/sebastiangz/Procesador_de_Series_Temporales_con_Enfoque_Funcional.git)
cd Procesador_de_Series_Temporales_con_Enfoque_Funcional

# 2. Crear y activar el entorno virtual
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 3. Instalar las dependencias
pip install -r requirements.txt
```

## 🚀 Uso del Sistema (Avance 2)

# demo_avance2.py

from src.core.lazy_streams import leer_ventas_csv
from src.core.pure_functions import media_movil, normalizar
from src.core.transformers import TimeSeriesPipeline
from functools import partial

# 1. Cargar datos de forma 'lazy' (eficiente)
# (Usamos un archivo de ejemplo para la demo)
generador_ventas = leer_ventas_csv('data/ventas_restaurante.csv')
        
# 2. Extraer solo la columna de interés
serie_temporal = [venta['total_ventas'] for venta in generador_ventas]

# 3. Crear un pipeline funcional de transformaciones
# (Esto combina Semana 1 y Semana 2)
pipeline = (TimeSeriesPipeline(serie_temporal)
           .add_transformation(normalizar, method='zscore') # Transf. Semana 2
           .add_transformation(lambda data_tupla: data_tupla[0]) # Se extrae el dato
           .add_transformation(media_movil, tamano_ventana=3) # Operación Semana 1
           )
        
# 4. Ejecutar el pipeline
resultado_final = pipeline.execute()

print(f"Datos procesados (Normalizados + Media Móvil): {resultado_final}")

## 📂 Estructura del Proyecto

/timeseries_processor/
├── data/
│   └── ventas_restaurante.csv
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── pure_functions.py    # (Avance 1 y 2: media_movil, normalize)
│   │   ├── transformers.py      # (Avance 2: compose, pipe, TimeSeriesPipeline)
│   │   └── lazy_streams.py      # (Avance 1: leer_ventas_csv)
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── ... (Próximamente Avance 3)
│   └── ...
├── venv/
├── demo_avance1.py              # Demo de la semana pasada
├── demo_avance2.py              # Demo de esta semana
└── requirements.txt

## 📈 Pipeline de Desarrollo (Avance 2)

Semana 1: Funciones Básicas de Manipulación (Completado) ✅

Estructura del proyecto y lectura de datos (lazy_streams.py).

Operaciones básicas: media_movil, diferenciacion (pure_functions.py).

Semana 2: Filtros y Transformaciones Complejas (Completado) ✅

Implementación de transformaciones de escala (normalize en pure_functions.py).

Implementación de composición de funciones (pipe, compose, TimeSeriesPipeline en transformers.py).

Optimización con lazy evaluation (demostrado en la lectura).

Semana 3: Detección de Anomalías y Patrones (En progreso)

Semana 4: Dashboard y API Funcional


## 💼 Componente de Emprendimiento
Aplicación Real: Sistema de análisis y predicción de ventas para el restaurante "Las Hamacas del Mayor".

Propuesta de Valor:
1. Optimización de inventario para reducir el desperdicio de alimentos.
2. Detección automática de anomalías en las ventas (ej. caídas por problemas operativos).
3. Planificación de personal basada en la predicción de demanda por día de la semana.

## 📚 Referencias Académicas
Sprangers, O., De Rijke, M., & Vlachos, M. (2024). Efficient and Accurate Forecasting in Large-scale Settings.
Relevancia: Justifica el uso de agregaciones (que veremos en Semana 3) para analizar ventas en diferentes niveles y encontrar tendencias.
Ledesma, J., Garcia, M. (2025). Real-Time Advertising Data Unification Using Spark and S3.
Relevancia: Respalda el uso de un pipeline funcional para transformar y filtrar grandes volúmenes de datos, similar a cómo procesaremos el historial de ventas.
Wagner, M. & Neumann, D. (2020). Identifying and Responding to Outlier Demand in Revenue Management.
Relevancia: Fundamenta el objetivo de nuestra Semana 3 para la detección de anomalías, aplicando técnicas funcionales para identificar días con ventas inusuales.

## 👥 Equipo
Nombre: 
1. Abimael Villamar
2. Jesus Fuentes
3. Aaron Diaz 

GitHub: [@Abimael2012](https://github.com/Abimael2012)

## 📄 Licencia
Proyecto académico - Universidad de Colima © 2025
