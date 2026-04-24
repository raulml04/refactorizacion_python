def procesar_registros(registros):
    resultados = []
    for registro in registros:
        if es_venta_valida(registro):

            total = calcular_total_venta(registro)
            mensaje = formatear_resultado(registro['nombre'], total, "Total")
            resultados.append(mensaje)

        elif es_devolucion_valida(registro):

            total = calcular_total_devolucion(registro)
            mensaje = formatear_resultado(registro['nombre'], total, "Retorno")
            resultados.append(mensaje)

        # Log centralizado para evitar duplicación
        registrar_log(registro['nombre'])

    return resultados


def es_venta_valida(registro):
    return registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado'


def es_devolucion_valida(registro):
    return registro['tipo'] == 'devolucion' and registro['monto'] > 0


def calcular_total_venta(registro):
    if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
        return registro['monto'] * 0.9
    return registro['monto']


def calcular_total_devolucion(registro):
    return registro['monto'] * -1


def formatear_resultado(nombre, total, tipo):
    return f"Cliente: {nombre} - {tipo}: {total}"


def registrar_log(nombre):
    # Registro de auditoría centralizado
    print(f"Procesando registro de: {nombre}")