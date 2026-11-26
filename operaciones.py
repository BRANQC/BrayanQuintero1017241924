"""Operaciones aritméticas básicas utilizadas por la aplicación."""


def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b


def restar(a, b):
    """Retorna la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b


def dividir(a, b):
    """Retorna la división de dos números.

    Lanza ZeroDivisionError cuando el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No es posible dividir entre cero.")
    return a / b
