def procesar_registros(registros):
    resultados = []
    for registro in registros:
        # Comprobar si es una venta válida
        if registro['tipo'] == 'venta' and registro['monto'] > 0 and registro['estado'] == 'completado':
            # Aplicar descuento si el monto es alto o es cliente VIP
            if registro['monto'] > 1000 or (registro['cliente_tipo'] == 'VIP' and registro['monto'] > 500):
                total = registro['monto'] * 0.9
            else:
                total = registro['monto']
            
            # Formatear el resultado
            mensaje = "Cliente: " + registro['nombre'] + " - Total: " + str(total)
            resultados.append(mensaje)
            
            # Imprimir log de auditoría
            print("Procesando registro de: " + registro['nombre'])

        elif registro['tipo'] == 'devolucion' and registro['monto'] > 0:
            # Lógica de devoluciones
            total = registro['monto'] * -1
            mensaje = "Cliente: " + registro['nombre'] + " - Retorno: " + str(total)
            resultados.append(mensaje)

            print("Procesando registro de: " + registro['nombre'])

    return resultados