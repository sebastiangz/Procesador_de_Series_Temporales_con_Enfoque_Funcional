import os
from datetime import datetime
from datos import leer_ventas
from transformaciones import (
    filtrar_por_fecha,
    filtrar_por_hora,
    calcular_ingresos,
    contar_ventas_por_cafe
)

RUTA_CSV = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "Coffe_sales.csv"
)

RUTA_CSV = os.path.abspath(RUTA_CSV)

def cargar_ventas():
    resultado = leer_ventas(RUTA_CSV)

    if resultado.ok:
        return resultado.valor

    print(resultado.valor)
    return None

def mostrar_menu():
    print("\n===== SISTEMA DE ANALISIS DE VENTAS DE CAFE =====")
    print("1. Mostrar resumen general de ventas")
    print("2. Consultar ventas por fecha")
    print("3. Consultar ventas por hora")
    print("4. Mostrar cafes mas vendidos")
    print("5. Salir")

def mostrar_resumen(ventas):
    total_ventas = len(ventas)
    ingresos = calcular_ingresos(ventas)
    promedio = ingresos / total_ventas

    print("\n===== RESUMEN GENERAL =====")
    print("Total de ventas:", total_ventas)
    print("Ingresos totales: $", round(ingresos, 2))
    print("Promedio por venta: $", round(promedio, 2))

def consultar_fecha(ventas):
    fecha = input("Ingresa la fecha (AAAA-MM-DD): ")

    try:
        fecha_validada = datetime.strptime(fecha, "%Y-%m-%d")

        if fecha_validada.strftime("%Y-%m-%d") != fecha:
            print("Formato de fecha no valido.")
            return

    except ValueError:
        print("Fecha no valida. Usa el formato AAAA-MM-DD.")
        return

    ventas_fecha = filtrar_por_fecha(ventas, fecha)

    if not ventas_fecha:
        print("No se encontraron ventas en esa fecha.")
        return

    print("\n===== VENTAS POR FECHA =====")
    print("Fecha:", fecha)
    print("Cantidad de ventas:", len(ventas_fecha))
    print("Ingresos: $", round(calcular_ingresos(ventas_fecha), 2))

    for venta in ventas_fecha:
        print(venta.hora, "-", venta.cafe, "- $", venta.importe)

def consultar_hora(ventas):
    hora = input("Ingresa la hora (0-23): ")

    if not hora.isdigit() or int(hora) < 0 or int(hora) > 23:
        print("Hora no valida.")
        return

    ventas_hora = filtrar_por_hora(ventas, int(hora))

    if not ventas_hora:
        print("No se encontraron ventas en esa hora.")
        return

    print("\n===== VENTAS POR HORA =====")
    print("Hora:", hora)
    print("Cantidad de ventas:", len(ventas_hora))
    print("Ingresos: $", round(calcular_ingresos(ventas_hora), 2))

    for venta in ventas_hora:
        print(venta.fecha, "-", venta.cafe, "- $", venta.importe)

def mostrar_cafes(ventas):
    cantidades = contar_ventas_por_cafe(ventas)

    cafes_ordenados = sorted(
        cantidades,
        key=lambda cafe: cafe[1],
        reverse=True
    )

    print("\n===== CAFES MAS VENDIDOS =====")

    for cafe, cantidad in cafes_ordenados:
        print(cafe, "-", cantidad, "ventas")

def main():
    ventas = cargar_ventas()

    if ventas is None:
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_resumen(ventas)

        elif opcion == "2":
            consultar_fecha(ventas)

        elif opcion == "3":
            consultar_hora(ventas)

        elif opcion == "4":
            mostrar_cafes(ventas)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")

if __name__ == "__main__":
    main()