
# Modulo de transformaciones de ventas de cafe

def filtrar_por_fecha(ventas, fecha):
    return tuple(filter(lambda venta: venta.fecha == fecha, ventas))



def filtrar_por_hora(ventas, hora):
    return tuple(filter(lambda venta: venta.hora == hora, ventas))
