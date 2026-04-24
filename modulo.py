def procesar_registros(registros):
    resultados = []
    for registro in registros:
        # Validación directa (aún sin refactorizar)
        if registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado':

            # Cálculo separado en función
            total = calcular_total_venta(registro)

            # Formateo centralizado
            mensaje = formatear_resultado(registro['nombre'], total, "Total")
            resultados.append(mensaje)

            # Log duplicado (pendiente de refactor)
            print("Procesando registro de: " + registro['nombre'])

        elif registro['tipo'] == 'devolucion' and registro['monto'] > 0:

            # Cálculo de devolución separado
            total = calcular_total_devolucion(registro)

            mensaje = formatear_resultado(registro['nombre'], total, "Retorno")
            resultados.append(mensaje)

            print("Procesando registro de: " + registro['nombre'])

    return resultados


def calcular_total_venta(registro):
    # Aplica descuento según reglas de negocio
    if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
        return registro['monto'] * 0.9
    return registro['monto']


def calcular_total_devolucion(registro):
    # Convierte el monto en negativo para representar devolución
    return registro['monto'] * -1


def formatear_resultado(nombre, total, tipo):
    # Genera el mensaje de salida
    return f"Cliente: {nombre} - {tipo}: {total}"