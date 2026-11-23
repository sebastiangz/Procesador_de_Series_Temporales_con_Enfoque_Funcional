Esta guía explica cómo ejecutar el programa y utilizar sus principales funciones.

### 1. Requisitos

Para ejecutar el sistema se necesita:

- Tener instalado Python 3.
- Tener los archivos del proyecto en la computadora.
- Se recomienda utilizar Visual Studio Code.

El programa no requiere instalar bibliotecas adicionales.

### 2. Preparar el proyecto

Abrir la carpeta `Sistema_Analisis_Ventas_Cafe` en Visual Studio Code.

Comprobar que contenga los siguientes archivos:

- `data/Coffe_sales.csv`
- `src/datos.py`
- `src/transformaciones.py`
- `src/main.py`

### 3. Ejecutar el programa

Abrir una terminal desde Visual Studio Code mediante **Terminal → New Terminal**.

Asegurarse de estar dentro de la carpeta `Sistema_Analisis_Ventas_Cafe`.

Escribir el siguiente comando:

`py src/main.py`

Si el comando `py` no está disponible, utilizar:

`python src/main.py`

### 4. Utilizar el sistema

Al ejecutar el programa aparecerá el siguiente menú:

1. Mostrar resumen general de ventas.
2. Consultar ventas por fecha.
3. Consultar ventas por hora.
4. Mostrar cafés más vendidos.
5. Salir.

El usuario debe introducir el número de la opción que desea consultar.

Para consultar ventas por fecha, utilizar el formato `AAAA-MM-DD`, por ejemplo `2024-03-01`.

Para consultar ventas por hora, introducir un número entre 0 y 23.

### 5. Ejecutar las pruebas

Para comprobar las funciones de análisis, ejecutar desde la carpeta principal:

`py -m unittest discover -s tests -v`

El sistema cuenta con cuatro pruebas automáticas desarrolladas mediante `unittest`.

### 6. Finalizar el programa

Para salir del sistema, seleccionar la opción `5` del menú principal.
