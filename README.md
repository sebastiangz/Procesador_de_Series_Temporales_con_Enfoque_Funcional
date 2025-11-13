# 📈 Proyecto 2: Procesador de Series Temporales con Enfoque Funcional

## 📋 Descripción del Proyecto

Sistema funcional para procesar, analizar y predecir series temporales utilizando técnicas de programación funcional, incluyendo transformaciones, filtrado de ruido, detección de tendencias y forecasting.

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
git clone https://github.com/tu-usuario/series-temporales-funcional.git
cd series-temporales-funcional

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

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

## 🚀 Uso del Sistema

```python
from src.timeseries import load_series, create_pipeline

# Cargar serie temporal
data = load_series('datos/ventas.csv', date_column='fecha')

# Crear pipeline funcional
pipeline = create_pipeline(
    remove_outliers(threshold=3),
    smooth_ma(window=7),
    detect_trend(),
    seasonal_decompose(),
    forecast(periods=30)
)

# Procesar serie
result = pipeline(data)

# Visualizar
plot_results(result, output='analisis.html')
```

---

## 📂 Estructura del Proyecto

```
series-temporales-funcional/
├── src/
│   ├── __init__.py
│   ├── timeseries.py       # Funciones core de series temporales
│   ├── transforms.py       # Transformaciones funcionales
│   ├── filters.py          # Filtros y suavizado
│   ├── analysis.py         # Análisis estadístico
│   ├── forecasting.py      # Modelos de predicción
│   └── visualization.py    # Gráficos y visualización
├── data/
│   ├── raw/                # Datos crudos
│   └── processed/          # Datos procesados
├── tests/
│   ├── test_transforms.py
│   ├── test_filters.py
│   └── test_forecasting.py
├── notebooks/
│   ├── exploracion.ipynb
│   └── ejemplos.ipynb
├── docs/
│   ├── api.md
│   └── ejemplos.md
├── requirements.txt
├── README.md
└── .gitignore
```

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

### Semana 1: Fundamentos (30 Oct - 5 Nov)
- Estructuras de datos inmutables para series
- Funciones básicas de transformación
- Lazy evaluation inicial

### Semana 2: Análisis Avanzado (6 Nov - 12 Nov)
- Descomposición estacional funcional
- Detección de anomalías
- Métricas de calidad

### Semana 3: Forecasting (13 Nov - 19 Nov)
- Modelos predictivos funcionales
- Validación temporal
- Dashboard interactivo

---

## 💼 Componente de Emprendimiento

**Aplicación Real**: Sistema de análisis y predicción de ventas para e-commerce

**Propuesta de Valor**:
- Predicción de demanda con 90%+ de precisión
- Detección automática de tendencias de mercado
- Alertas tempranas de anomalías en ventas
- Optimización de inventario basada en forecasting

**Modelo de Negocio**: SaaS con pricing por volumen de datos procesados

---

## 📚 Referencias

- Hyndman, R.J., & Athanasopoulos, G. (2021). *Forecasting: principles and practice*
- **Pandas Time Series**: https://pandas.pydata.org/docs/user_guide/timeseries.html
- **Statsmodels**: https://www.statsmodels.org/
- **Toolz**: https://toolz.readthedocs.io/

---

## 🏆 Criterios de Evaluación

- **Lazy Evaluation (25%)**: Eficiencia en memoria, procesamiento bajo demanda
- **Composición Funcional (30%)**: Pipeline elegante, transformaciones composables
- **Análisis Temporal (25%)**: Precisión en forecasting, detección de patrones
- **Testing y Performance (20%)**: Cobertura, benchmarks

---

## 👥 Autor

**Nombre**: Abimael Villamar 
**Email**: [tu-email@ucol.mx]  
**GitHub**: [@tu-usuario](https://github.com/tu-usuario)
**Nombre**: Jesus Fuentes
**Email**: [Jfuentes15@ucol.mx](mailto:jfuentes15@ucol.mx)
**GitHub**: [@ChuyFuentes](https://github.com/ChuyFuentesDev)
aarondiazurena25-svg
**Nombre**: Aaron Diaz
**Email**: [adiaz82@ucol.mx](mailto:adiaz82@ucol.mx)
**GitHub**: [@aarondiazurena25-svg](https://github.com/aarondiazurena25-svgDev)
---

## 📄 Licencia

Proyecto académico - Universidad de Colima © 2025
