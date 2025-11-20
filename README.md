📈 Proyecto 2: Procesador de Series Temporales con Enfoque Funcional
==================================================================

📋 DESCRIPCIÓN DEL PROYECTO
----------------------------
Sistema funcional que procesa y analiza la serie temporal de ventas del restaurante "Las Hamacas del Mayor".
El sistema implementa transformaciones, filtrados y agregaciones (basado en el dataset M5 de Kaggle)
manteniendo los principios de funciones puras e inmutabilidad.

Universidad de Colima - Ingeniería en Computación Inteligente
Materia: Programación Funcional
Profesor: Gonzalez Zepeda Sebastian
Semestre: Agosto 2025 - Enero 2026

==================================================================

🎯 OBJETIVOS
-------------
- Implementar funciones puras para la transformación de series temporales.
- Aplicar lazy evaluation (evaluación perezosa) con generadores para el manejo eficiente de grandes datasets (M5).
- Usar composición de funciones para crear pipelines de análisis.
- Aplicar funciones de orden superior (map, filter, reduce) en el análisis temporal.
- Utilizar recursión para algoritmos de procesamiento.

==================================================================

🛠️ TECNOLOGÍAS UTILIZADAS
--------------------------
- Lenguaje: Python 3.11+
- Paradigma: Programación Funcional
- Librerías (requirements.txt):
  - pandas
  - numpy
  - statsmodels
  - matplotlib
  - fastapi
  - plotly
  - uvicorn
  - rx

==================================================================

📦 INSTALACIÓN
---------------
# 1. Clonar el repositorio
git clone https://github.com/sebastiangz/Procesador_de_Series_Temporales_con_Enfoque_Funcional.git
cd Procesador_de_Series_Temporales_con_Enfoque_Funcional

# 2. Crear y activar el entorno virtual
python -m venv venv
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Descargar los datos de Kaggle (M5)
# Colocar 'calendar.csv' y 'sales_train_validation.csv'
# dentro de la carpeta /data/

==================================================================

🚀 USO DEL SISTEMA (PROYECTO FINAL)
----------------------------------
El proyecto tiene dos modos de ejecución:

1. Demo Principal (Genera el Dashboard)
   Este script ejecuta el pipeline completo (carga, análisis, detección de anomalías)
   y genera un dashboard interactivo (reporte_ventas_final.html).

   # Asegúrate de que tu venv esté activado
   python demo_avance1.py
   
   # El script generará 'reporte_ventas_final.html'.
   # Ábrelo en tu navegador.

2. API Funcional
   Inicia un servidor web local con uvicorn que expone los análisis como endpoints.

   # En una terminal separada, activa el venv
   uvicorn src.api.endpoints:app --reload
   
   # Visita http://127.0.0.1:8000 en tu navegador.

==================================================================

📂 ESTRUCTURA DEL PROYECTO
---------------------------
/timeseries_processor/
├── data/
│   ├── calendar.csv             (Datos de Kaggle M5)
│   └── sales_train_validation.csv (Datos de Kaggle M5)
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py         (Semana 4: API con FastAPI)
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── anomaly_detection.py (Semana 3: Detección de anomalías)
│   │   └── pattern_matching.py  (Semana 3: Detección de patrones)
│   ├── core/
│   │   ├── __init__.py
│   │   ├── pure_functions.py    (Semana 1/2: Funciones puras)
│   │   ├── transformers.py      (Semana 2: Composición/Pipeline)
│   │   └── lazy_streams.py      (Semana 1: Lazy evaluation)
│   ├── reactive/
│   └── visualization/
│       ├── __init__.py
│       └── dashboard.py         (Semana 4: Dashboard con Plotly)
├── venv/
├── demo_avance1.py              (Script principal de demostración)
└── requirements.txt

==================================================================

📈 PIPELINE DE DESARROLLO (100% COMPLETADO)
--------------------------------------------
- Semana 1: Funciones Básicas de Manipulación (Completado) ✅
- Semana 2: Filtros y Transformaciones Complejas (Completado) ✅
- Semana 3: Detección de Anomalías y Patrones (Completado) ✅
- Semana 4: Dashboard y API Funcional (Completado) ✅

==================================================================

💼 COMPONENTE DE EMPRENDIMIENTO
--------------------------------
Aplicación Real: Sistema de análisis y predicción de ventas para el restaurante "Las Hamacas del Mayor".

Propuesta de Valor:
1. Optimización de inventario para reducir el desperdicio de alimentos.
2. Detección automática de anomalías en las ventas (ej. caídas por problemas operativos).
3. Planificación de personal basada en la predicción de demanda por día de la semana.

==================================================================

📚 REFERENCIAS ACADÉMICAS
--------------------------
1. Sprangers, O., De Rijke, M., & Vlachos, M. (2024). Efficient and Accurate Forecasting in Large-scale Settings.
2. Ledesma, J., Garcia, M. (2025). Real-Time Advertising Data Unification Using Spark and S3.
3. Wagner, M. & Neumann, D. (2020). Identifying and Responding to Outlier Demand in Revenue Management.

==================================================================

👥 EQUIPO
----------
- Nombre: Abimael Villamar
  GitHub: @Abimael2012 (https://github.com/Abimael2012)
- Nombre: Jesus Fuentes
- Nombre: Aaron Diaz

<<<<<<< HEAD
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
**Nombre**: Aaron Diaz
**Email**: [adiaz82@ucol.mx](mailto:adiaz82@ucol.mx)
**GitHub**: [@aarondiazurena25-svg](https://github.com/aarondiazurena25-svgDev)
---

## 📄 Licencia
=======
==================================================================
>>>>>>> d681c978d0e169f7fa9fb6547fa0d9c561ef44f9

📄 LICENCIA
------------
Proyecto académico - Universidad de Colima © 2025
