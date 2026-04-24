# Módulo inicial de procesamiento de ventas
def p(d):
    # Esta función hace muchas cosas a la vez
    res = []
    for i in d:
        # Comprobar si es una venta válida
        if i['tipo'] == 'venta' and i['monto'] > 0 and i['estado'] == 'completado':
            # Aplicar descuento si el monto es alto o es cliente VIP
            if i['monto'] > 1000 or (i['cliente_tipo'] == 'VIP' and i['monto'] > 500):
                f = i['monto'] * 0.9
            else:
                f = i['monto']
            
            # Formatear el resultado
            s = "Cliente: " + i['nombre'] + " - Total: " + str(f)
            res.append(s)
            
            # Imprimir log de auditoría (duplicado innecesario)
            print("Procesando registro de: " + i['nombre'])
        elif i['tipo'] == 'devolucion' and i['monto'] > 0:
            # Lógica de devoluciones mezclada
            f = i['monto'] * -1
            s = "Cliente: " + i['nombre'] + " - Retorno: " + str(f)
            res.append(s)
            print("Procesando registro de: " + i['nombre'])
            
    return res

# Datos de prueba para verificar que funciona
datos_sucios = [
    {'tipo': 'venta', 'monto': 1200, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Juan'},
    {'tipo': 'venta', 'monto': 600, 'estado': 'completado', 'cliente_tipo': 'VIP', 'nombre': 'Ana'},
    {'tipo': 'devolucion', 'monto': 50, 'estado': 'completado', 'cliente_tipo': 'estándar', 'nombre': 'Pedro'}
]

print(p(datos_sucios))