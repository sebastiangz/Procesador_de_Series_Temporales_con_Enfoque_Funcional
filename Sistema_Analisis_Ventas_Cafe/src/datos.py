
import csv
from collections import namedtuple

# Estructura para guardar los datos de cada venta
Venta = namedtuple("Venta", "fecha hora cafe importe")

# Estructura para indicar si la lectura fue correcta
Result = namedtuple("Result", "ok valor")


def convertir_fila(fila):
    """Convierte una fila del CSV en un registro de venta."""
    return Venta(
        fecha=fila["Date"],
        hora=int(fila["hour_of_day"]),
        cafe=fila["coffee_name"],
        importe=float(fila["money"])
    )


def leer_ventas(ruta):
    """Lee el archivo CSV y devuelve las ventas."""
    try:
        with open(ruta, encoding="utf-8", newline="") as archivo:
            filas = csv.DictReader(archivo)
            ventas = tuple(map(convertir_fila, filas))

        return Result(True, ventas)

    except (OSError, ValueError, KeyError) as error:
        return Result(False, "Error al leer los datos: " + str(error))
