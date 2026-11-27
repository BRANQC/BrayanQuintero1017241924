"""Validaciones de los datos de entrada de la aplicación.

Estas validaciones corresponden a las técnicas de verificación y
aseguramiento que se ejecutan dentro del flujo de CI/CD antes de permitir
el despliegue del desarrollo.
"""

VALOR_MAXIMO_PERMITIDO = 1000000


def validar_numero(valor):
    """Convierte un valor de entrada a número y verifica que sea válido.

    Lanza ValueError cuando el valor está vacío, no es numérico o
    sobrepasa el límite permitido por la aplicación.
    """
    if valor is None or (isinstance(valor, str) and valor.strip() == ""):
        raise ValueError("El valor recibido está vacío.")

    try:
        numero = float(valor)
    except (TypeError, ValueError):
        raise ValueError("El valor '{}' no es un número válido.".format(valor))

    if abs(numero) > VALOR_MAXIMO_PERMITIDO:
        raise ValueError(
            "El valor {} supera el máximo permitido ({}).".format(
                numero, VALOR_MAXIMO_PERMITIDO
            )
        )

    return numero
