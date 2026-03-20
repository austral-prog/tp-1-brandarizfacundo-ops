from ctypes import pythonapi


def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 1
    num2 = 8
    num3 = 23
    num4 = 12

    print("Promedio:", (num1 + num2 + num3 + num4) / 4)
    print("Máximo:", max(num1, num2, num3, num4))
    print("Mínimo:", min(num1, num2, num3, num4))
    print("Rango:", max(num1, num2, num3, num4) - min(num1, num2, num3, num4))
