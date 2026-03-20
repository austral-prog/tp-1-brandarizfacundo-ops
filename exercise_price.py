def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    impuesto=precio_base*0.21
    print(impuesto)
    subtal=(precio_base+impuesto)
    print(subtal)
    monto=(subtal*0.1)
    print(monto)
    print(subtal+monto)

