"""Aplicación principal del taller de Aplicaciones y servicios web.

Actividad de la Guía de Trabajo No. 5 - Taller evaluativo 20%.
Esta aplicación es la que ejecuta el flujo de CI/CD en GitHub Actions.
"""

from operaciones import dividir, multiplicar, restar, sumar
from validaciones import validar_numero


def saludar(nombre="estudiantes del ITM"):
    """Construye el mensaje de bienvenida de la aplicación."""
    return "Hola {}!".format(nombre)


def calcular(primer_valor, segundo_valor):
    """Valida los datos de entrada y retorna el resultado de las operaciones."""
    a = validar_numero(primer_valor)
    b = validar_numero(segundo_valor)

    return {
        "suma": sumar(a, b),
        "resta": restar(a, b),
        "multiplicacion": multiplicar(a, b),
        "division": dividir(a, b),
    }


def main():
    """Punto de entrada de la aplicación."""
    print(saludar())

    resultados = calcular("10", "50")
    for nombre_operacion, resultado in resultados.items():
        print("{}: {}".format(nombre_operacion.capitalize(), resultado))

    try:
        calcular("abc", "50")
    except ValueError as error:
        print("Entrada inválida controlada: {}".format(error))

    try:
        dividir(10, 0)
    except ZeroDivisionError as error:
        print("División entre cero controlada: {}".format(error))

    print("Aplicación ejecutada correctamente desde el flujo de CI/CD.")


if __name__ == "__main__":
    main()
