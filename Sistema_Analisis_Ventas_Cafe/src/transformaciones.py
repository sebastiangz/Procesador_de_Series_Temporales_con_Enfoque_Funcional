from functools import reduce
# Modulo de transformaciones de ventas de cafe

def filtrar_por_fecha(ventas, fecha):
    return tuple(filter(lambda venta: venta.fecha == fecha, ventas))



def filtrar_por_hora(ventas, hora):
    return tuple(filter(lambda venta: venta.hora == hora, ventas))


def calcular_ingresos(ventas):
    return reduce(lambda total, venta: total + venta.importe, ventas, 0)


def contar_ventas_por_cafe(ventas):
    cafes = set(map(lambda venta: venta.cafe, ventas))

    return tuple(
        (cafe, len(tuple(filter(lambda venta: venta.cafe == cafe, ventas))))
        for cafe in sorted(cafes)
    )
