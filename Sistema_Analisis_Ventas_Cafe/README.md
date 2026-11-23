# ☕ Sistema de Análisis de Ventas de Café con Programación Funcional

## 📋 DESCRIPCIÓN DEL PROYECTO

El proyecto consiste en desarrollar un sistema de análisis de ventas de café utilizando Python y los principios de la programación funcional.

Para su desarrollo se utiliza la base de datos **Coffee Sales Dataset**, obtenida de Kaggle, la cual contiene 3,547 registros de ventas realizadas mediante una máquina expendedora de café. Esta información incluye fechas, horarios, tipos de café, métodos de pago e importes de las transacciones.

El sistema permite procesar estos datos para realizar consultas sobre las ventas, identificar los productos más vendidos, consultar horarios de venta y calcular los ingresos registrados.

Se implementan conceptos de programación funcional como funciones puras, estructuras de datos inmutables y funciones de orden superior (`map`, `filter` y `reduce`).

El proyecto se desarrolló de forma modular, permitiendo que cada integrante del equipo trabajara en una parte específica del sistema.

## 🎯 OBJETIVOS

**Objetivo general:**

Desarrollar un sistema en Python que permita procesar y analizar registros de ventas de café mediante la aplicación de los principios básicos de la programación funcional.

**Objetivos específicos:**

- Leer y organizar los registros del Coffee Sales Dataset utilizando Python.
- Implementar funciones puras que permitan procesar los datos sin modificar la información original.
- Aplicar funciones de orden superior (`map`, `filter` y `reduce`) para filtrar y realizar cálculos sobre las ventas.
- Utilizar estructuras de datos inmutables y composición de funciones.
- Analizar las ventas por fecha y horario, calcular ingresos e identificar los productos más vendidos.
- Desarrollar un menú sencillo que permita consultar los resultados del análisis.
- Dividir el proyecto en módulos independientes para facilitar su desarrollo.
- Realizar pruebas básicas para verificar el funcionamiento del programa.

## 👥 EQUIPO DE DESARROLLO

**Universidad:** Universidad de Colima

**Carrera:** Ingeniería en Computación Inteligente

**Materia:** Programación Funcional

**Profesor:** González Zepeda Sebastián

### Integrantes y responsabilidades

**1. Dustin Haziel Feliciano Velasco**

- GitHub: [@dfeliciano-eng](https://github.com/dfeliciano-eng)
- Módulo asignado: `datos.py`
- Responsabilidad: Lectura y preparación de los registros de ventas desde el archivo CSV.
- Estado: Implementado y probado.

**2. Cristian Yael Naranjo Ruelas**

- GitHub: [@criss-cmd594](https://github.com/criss-cmd594)
- Módulo asignado: `transformaciones.py`
- Responsabilidad: Implementación de funciones puras, filtros y cálculos para el análisis de ventas.
- Estado: Implementado y probado.

**3. Francisco Javiel Villaseñor Cernas**

- GitHub: [@fvillasenor4](https://github.com/fvillasenor4)
- Módulo asignado: `main.py` y pruebas.
- Responsabilidad: Desarrollo del menú principal, integración de los módulos y realización de pruebas básicas.
- Estado: Implementado y probado.

### Organización del trabajo

Cada integrante fue responsable de desarrollar y documentar su módulo, colaborando con los demás integrantes para lograr el funcionamiento completo del sistema.

## 📌 ESTADO ACTUAL DEL PROYECTO

Se desarrolló un sistema funcional que integra los módulos de lectura de datos, transformaciones y menú principal.

Los tres módulos fueron probados en Visual Studio Code, comprobando que el programa puede leer y analizar los 3,547 registros del archivo CSV.

El sistema cuenta con:

- Lectura y organización de los registros de ventas.
- Funciones de filtrado por fecha y hora.
- Cálculo de ingresos y conteo de productos vendidos.
- Menú interactivo en la terminal.
- Validación de entradas del usuario.
- Pruebas de las funciones de análisis.

## 💻 FUNCIONALIDADES DEL SISTEMA

El programa cuenta con un menú principal de cinco opciones:

**1. Mostrar resumen general de ventas**

Permite consultar la cantidad total de ventas, los ingresos registrados y el promedio de ingresos por venta.

**2. Consultar ventas por fecha**

Permite introducir una fecha en formato `AAAA-MM-DD` y consultar las ventas realizadas ese día, mostrando la cantidad de registros, los ingresos y el detalle de cada transacción.

**3. Consultar ventas por hora**

Permite introducir una hora entre 0 y 23 para consultar las ventas realizadas durante ese horario, incluyendo la cantidad de transacciones y sus ingresos.

**4. Mostrar cafés más vendidos**

Muestra los diferentes tipos de café ordenados desde el más vendido hasta el menos vendido, indicando la cantidad de ventas de cada producto.

**5. Salir**

Finaliza la ejecución del sistema.

El programa también incluye validaciones para entradas incorrectas, como fechas inexistentes, horas fuera de rango y opciones no disponibles.

## 📂 ESTRUCTURA DEL PROYECTO

```text
Sistema_Analisis_Ventas_Cafe/
│
├── README.md
│
├── data/
│   ├── Coffe_sales.csv
│   └── README.md
│
├── src/
│   ├── datos.py
│   ├── transformaciones.py
│   └── main.py
│
├── tests/
│   └── test_transformaciones.py
│
└── docs/
    └── EMPRENDIMIENTO.md
```

**Descripción de los archivos principales:**

- `datos.py`: lectura del CSV y preparación de los registros de ventas.
- `transformaciones.py`: funciones puras para filtrar y analizar las ventas.
- `main.py`: menú principal e integración de los módulos.
- `test_transformaciones.py`: pruebas para verificar los resultados de las funciones de análisis.
- `Coffe_sales.csv`: base de datos utilizada por el sistema.
- `EMPRENDIMIENTO.md`: propuesta de emprendimiento y posible comercialización del sistema.

## 🚀 INSTALACIÓN Y EJECUCIÓN

Para ejecutar el proyecto es necesario tener instalado Python 3 y se recomienda utilizar un editor de código como Visual Studio Code.

No se requiere instalar bibliotecas externas, ya que el programa utiliza herramientas incluidas en Python.

**Pasos para ejecutar el sistema:**

1. Descargar el proyecto desde GitHub.
2. Abrir la carpeta `Sistema_Analisis_Ventas_Cafe` en Visual Studio Code.
3. Abrir una terminal dentro de esa carpeta.
4. Ejecutar el siguiente comando:

```powershell
py src/main.py
```

Al ejecutarlo aparecerá el menú principal, donde el usuario podrá seleccionar las diferentes opciones de análisis.

En sistemas donde no esté disponible el comando `py`, se puede utilizar:

```bash
python src/main.py
```

## 🧪 PRUEBAS REALIZADAS

El funcionamiento del sistema fue comprobado en Visual Studio Code utilizando el archivo CSV original.

Entre los resultados obtenidos se encuentran:

- **Total de ventas:** 3,547 registros.
- **Ingresos totales:** 112,245.58 unidades monetarias.
- **Tipos de café identificados:** 8.
- **Café más vendido:** Americano with Milk, con 809 ventas.
- **Ventas del 1 de marzo de 2024:** 11 registros.

También se realizaron pruebas con fechas incorrectas, horas fuera de rango y opciones inexistentes del menú.

### Pruebas automáticas

Se utiliza la biblioteca `unittest` para comprobar las cuatro funciones principales de `transformaciones.py`.

Para ejecutar las pruebas desde la carpeta principal del proyecto:

```powershell
py -m unittest discover -s tests -v
```

**Resultado obtenido:**

- 4 pruebas ejecutadas.
- 4 pruebas aprobadas.
- 0 errores.

## 🔧 PROGRAMACIÓN FUNCIONAL UTILIZADA

Durante el desarrollo se aplicaron los siguientes conceptos:

- **Funciones puras:** las funciones de análisis reciben datos y devuelven resultados sin modificar las ventas originales.
- **Inmutabilidad:** se utilizan tuplas para almacenar los registros de ventas.
- **`map()`:** se utiliza para convertir y procesar registros.
- **`filter()`:** se utiliza para seleccionar ventas según determinadas condiciones.
- **`reduce()`:** se utiliza para calcular los ingresos acumulados.
- **Composición de funciones:** permite combinar operaciones de filtrado y cálculo.

La lectura del archivo y las operaciones de entrada y salida se mantienen separadas de las funciones puras de análisis.

## 💼 PROPUESTA DE EMPRENDIMIENTO

Como parte del proyecto se elaboró una propuesta de emprendimiento enfocada en ofrecer el sistema como una herramienta de análisis de ventas para pequeñas cafeterías, negocios independientes y establecimientos que almacenen sus registros en archivos CSV.

La propuesta contempla un servicio de instalación y configuración, así como posibles adaptaciones a las necesidades de otros negocios.

El documento completo se encuentra en:

[Consultar propuesta de emprendimiento](docs/EMPRENDIMIENTO.md)

## 📚 FUENTE DE DATOS

**Nombre:** Coffee Sales Dataset

**Autor del notebook:** Mahmoud Gamil

**Plataforma:** Kaggle

**Archivo utilizado:** `Coffe_sales.csv`

**Enlace:** https://www.kaggle.com/code/mahmoudredagamail/coffee-sales-dataset/input

El conjunto de datos contiene información sobre transacciones de ventas de café y fue utilizado con **fines académicos y educativos**, para desarrollar, probar y comprobar el funcionamiento del sistema mediante los principios de la programación funcional.
