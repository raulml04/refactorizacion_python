def procesar_registros(registros):
    resultados = []
    for registro in registros:
        # Validación mediante funciones (mejora legibilidad)
        if es_venta_valida(registro):

            total = calcular_total_venta(registro)
            mensaje = formatear_resultado(registro['nombre'], total, "Total")
            resultados.append(mensaje)

            # Log aún duplicado
            print("Procesando registro de: " + registro['nombre'])

        elif es_devolucion_valida(registro):

            total = calcular_total_devolucion(registro)
            mensaje = formatear_resultado(registro['nombre'], total, "Retorno")
            resultados.append(mensaje)

            print("Procesando registro de: " + registro['nombre'])

    return resultados


def es_venta_valida(registro):
    # Comprueba si el registro cumple condiciones de venta
    return registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado'


def es_devolucion_valida(registro):
    # Comprueba si el registro es una devolución válida
    return registro['tipo'] == 'devolucion' and registro['monto'] > 0


def calcular_total_venta(registro):
    # Aplica descuento si corresponde
    if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
        return registro['monto'] * 0.9
    return registro['monto']


def calcular_total_devolucion(registro):
    return registro['monto'] * -1


def formatear_resultado(nombre, total, tipo):
    return f"Cliente: {nombre} - {tipo}: {total}"