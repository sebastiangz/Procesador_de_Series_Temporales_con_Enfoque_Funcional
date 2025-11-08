# 📈 Proyecto 2: Procesador de Series Temporales con Enfoque Funcional

## 📋 Descripción del Proyecto

Sistema que procesa y analiza la serie temporal de ventas del restaurante "Las Hamacas del Mayor" usando programación funcional. El sistema implementa transformaciones, filtrados y agregaciones (basado en el dataset M5 de Kaggle) manteniendo los principios de funciones puras e inmutabilidad.



**Universidad de Colima - Ingeniería en Computación Inteligente**  
**Materia**: Programación Funcional  
**Profesor**: Gonzalez Zepeda Sebastian  
**Semestre**: Agosto 2025 - Enero 2026

---

## 🎯 Objetivos

- Implementar **lazy evaluation** para procesamiento eficiente de streams de datos
- Aplicar **funciones de orden superior** en análisis temporal
- Desarrollar **pipelines funcionales** para transformación de series
- Practicar **composición de transformaciones** temporales
- Utilizar **pattern matching** para detección de anomalías
- Crear **funciones currying** para configuración de análisis
- Implementar **funciones puras** para la transformación de series temporales.
- Aplicar **lazy evaluation** (evaluación perezosa) con generadores para el manejo eficiente de grandes datasets (M5).
- Usar **composición de funciones** para construir pipelines de análisis.
- Aplicar **funciones de orden superior** (map, filter, reduce) en el análisis temporal.
- Desarrollar un módulo de **detección de anomalías** para identificar días con ventas inusuales (Próxima semana).

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3.11+
- **Paradigma**: Programación Funcional
- **Librerías**:
  - `pandas` - Manipulación de series temporales
  - `numpy` - Operaciones numéricas
  - `toolz` - Utilidades funcionales
  - `more-itertools` - Iteradores avanzados
  - `plotly` - Visualización interactiva
  - `statsmodels` - Modelos estadísticos

---

## 📦 Instalación

```bash
# Clonar el repositorio
git clone
[https://github.com/sebastiangz/Procesador_de_Series_Temporales_con_Enfoque_Funcional.git](https://github.com/sebastiangz/Procesador_de_Series_Temporales_con_Enfoque_Funcional.git)
cd Procesador_de_Series_Temporales_con_Enfoque_Funcional

# Crear entorno virtual
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

### requirements.txt
```
pandas>=2.0.0
numpy>=1.24.0
toolz>=0.12.0
more-itertools>=10.0.0
plotly>=5.17.0
statsmodels>=0.14.0
scipy>=1.11.0
```

---

## 🚀 Uso del Sistema (Avance 2)

```El siguiente script (demo_avance2.py) demuestra el uso de los generadores y el pipeline de transformaciones (Semana 1 y 2).

Python

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
```

---

## 📂 Estructura del Proyecto (Avance 2)

```
Esta es la estructura de archivos implementada hasta la Semana 2.

/timeseries_processor/
├── data/
│   └── ventas_restaurante.csv   # Archivo con el historial de ventas
├── src/
│   └── core/
│       ├── _init_.py          # Inicializador del paquete
│       ├── pure_functions.py    # (Avance 1 y 2: media_movil, normalize)
│       ├── transformers.py      # (Avance 2: compose, pipe, TimeSeriesPipeline)
│       └── lazy_streams.py      # (Avance 1: leer_ventas_csv)
├── venv/
├── demo_avance1.py              # Script demo de la Semana 1
└── requirements.txt

---

## 🔑 Características Principales

### 1. Lazy Evaluation para Streams
```python
from itertools import islice
from toolz import compose, pipe

def create_data_stream(source):
    """Generator para procesamiento lazy"""
    for chunk in source:
        yield process_chunk(chunk)

# Procesamiento bajo demanda
stream = create_data_stream(large_dataset)
first_100 = list(islice(stream, 100))
```

### 2. Pipeline de Transformaciones
```python
from functools import partial

# Transformaciones composables
pipeline = compose(
    partial(moving_average, window=7),
    partial(remove_outliers, std=3),
    normalize_data,
    detect_seasonality
)

result = pipeline(timeseries_data)
```

### 3. Detección de Patrones
```python
from toolz import sliding_window

def detect_pattern(pattern, threshold=0.9):
    """Detecta patrones en series temporales"""
    def matcher(series):
        windows = sliding_window(len(pattern), series)
        return [
            (i, correlation(window, pattern))
            for i, window in enumerate(windows)
            if correlation(window, pattern) >= threshold
        ]
    return matcher
```

---

## 📊 Funcionalidades Implementadas

### Procesamiento de Datos
- ✅ Carga desde múltiples formatos (CSV, JSON, Parquet)
- ✅ Resampling temporal (upsampling/downsampling)
- ✅ Interpolación de valores faltantes
- ✅ Normalización y estandarización

### Análisis
- ✅ Descomposición estacional (STL, X-13)
- ✅ Detección de tendencias
- ✅ Identificación de anomalías
- ✅ Análisis de autocorrelación

### Forecasting
- ✅ Moving Average
- ✅ Exponential Smoothing
- ✅ ARIMA funcional
- ✅ Validación cruzada temporal

### Visualización
- ✅ Gráficos interactivos
- ✅ Dashboard de análisis
- ✅ Exportación de reportes

---

## 🧪 Testing

```bash
# Ejecutar tests
pytest tests/ -v

# Tests con cobertura
pytest --cov=src tests/

# Tests de performance
pytest tests/ -k "performance"
```

---

## 📈 Pipeline de Desarrollo

### Semana 1: Funciones Básicas de Manipulación (Completado)
- Estructuras de datos inmutables para series
- Funciones básicas de transformación
- Lazy evaluation inicial
- Estructura del proyecto y lectura de datos (lazy_streams.py).

Operaciones básicas: media_movil, diferenciacion (pure_functions.py).

### Semana 2: Filtros y Transformaciones Complejas (Completado) 
- Descomposición estacional funcional
- Detección de anomalías
- Métricas de calidad
- Implementación de transformaciones de escala (normalize en pure_functions.py).

Implementación de composición de funciones (pipe, TimeSeriesPipeline en transformers.py).

### Semana 3: Detección de Anomalías y Patrones (En progreso)
- Modelos predictivos funcionales
- Validación temporal
- Dashboard interactivo

---

## 💼 Componente de Emprendimiento

**Aplicación Real**: Sistema de análisis y predicción de ventas para el restaurante "Las Hamacas del Mayor".

**Propuesta de Valor**:
- Predicción de demanda con 90%+ de precisión
- Detección automática de tendencias de mercado
- Alertas tempranas de anomalías en ventas
- Optimización de inventario basada en forecasting
- Optimización de inventario para reducir el desperdicio de alimentos.
- Detección automática de anomalías en las ventas (ej. caídas por problemas operativos).
- Planificación de personal basada en la predicción de demanda por día de la semana.


**Modelo de Negocio**: SaaS con pricing por volumen de datos procesados

---

## 📚 Referencias

- Hyndman, R.J., & Athanasopoulos, G. (2021). *Forecasting: principles and practice*
- **Pandas Time Series**: https://pandas.pydata.org/docs/user_guide/timeseries.html
- **Statsmodels**: https://www.statsmodels.org/
- **Toolz**: https://toolz.readthedocs.io/
- Sprangers, O., De Rijke, M., & Vlachos, M. (2024). Efficient and Accurate Forecasting in Large-scale Settings.
- Relevancia: Justifica el uso de agregaciones para analizar ventas en diferentes niveles y encontrar tendencias.
- Ledesma, J., Garcia, M. (2025). Real-Time Advertising Data Unification Using Spark and S3.
- Relevancia: Respalda el uso de un pipeline funcional para transformar y filtrar grandes volúmenes de datos, similar a cómo procesaremos el historial de ventas.
- Wagner, M. & Neumann, D. (2020). Identifying and Responding to Outlier Demand in Revenue Management.
- Relevancia: Fundamenta el objetivo de nuestra Semana 3 para la detección de anomalías, aplicando técnicas funcionales para identificar días con ventas inusuales.

---

## 🏆 Criterios de Evaluación

- **Lazy Evaluation (25%)**: Eficiencia en memoria, procesamiento bajo demanda
- **Composición Funcional (30%)**: Pipeline elegante, transformaciones composables
- **Análisis Temporal (25%)**: Precisión en forecasting, detección de patrones
- **Testing y Performance (20%)**: Cobertura, benchmarks

---

## 👥 Autor

**Nombre**: Abimael Villamar 
**Nombre**: Jesus Fuentes
**Nombre**: Aaron Diaz
**Email**: [adiaz82@ucol.mx]  
**GitHub**: [@aarondiazurena25](https://github.com/tu-usuario)

---

## 📄 Licencia

Proyecto académico - Universidad de Colima © 2025
