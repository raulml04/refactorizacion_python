def procesar_registros(registros):
    """
    Procesa una lista de registros de ventas y devoluciones.

    Aplica las reglas de negocio correspondientes a cada tipo de registro
    (venta o devolución), genera un mensaje formateado con el resultado
    y registra cada operación para fines de auditoría.

    :param registros: lista de diccionarios con información de transacciones
    :return: lista de strings con los resultados procesados
    """
    resultados = []

    for registro in registros:
        # Se evalúa el tipo de registro y se procesa según corresponda
        if es_venta_valida(registro):

            total = calcular_total_venta(registro)
            mensaje = formatear_resultado(registro['nombre'], total, "Total")
            resultados.append(mensaje)

        elif es_devolucion_valida(registro):

            total = calcular_total_devolucion(registro)
            mensaje = formatear_resultado(registro['nombre'], total, "Retorno")
            resultados.append(mensaje)

        # Registro de auditoría centralizado para cada operación procesada
        registrar_log(registro['nombre'])

    return resultados


def es_venta_valida(registro):
    """
    Determina si un registro corresponde a una venta válida.
    """
    return (
        registro['tipo'] == 'venta' and
        registro['monto'] > 0 and
        registro['estado'] == 'completado'
    )


def es_devolucion_valida(registro):
    """
    Determina si un registro corresponde a una devolución válida.
    """
    return registro['tipo'] == 'devolucion' and registro['monto'] > 0


def calcular_total_venta(registro):
    """
    Calcula el total de una venta aplicando posibles descuentos.
    """
    if registro['monto'] > 1000 or (
        registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500
    ):
        return registro['monto'] * 0.9

    return registro['monto']


def calcular_total_devolucion(registro):
    """
    Calcula el total de una devolución.
    """
    return registro['monto'] * -1


def formatear_resultado(nombre, total, tipo):
    """
    Genera un mensaje formateado con el resultado.
    """
    return f"Cliente: {nombre} - {tipo}: {total}"


def registrar_log(nombre):
    """
    Registra en consola el procesamiento.
    """
    print(f"Procesando registro de: {nombre}")