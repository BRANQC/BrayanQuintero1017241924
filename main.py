"""Aplicación principal del taller de Aplicaciones y servicios web.

Actividad de la Guía de Trabajo No. 5 - Taller evaluativo 20%.
Esta aplicación es la que ejecuta el flujo de CI/CD en GitHub Actions.
"""

from operaciones import dividir, multiplicar, restar, sumar


def saludar(nombre="estudiantes del ITM"):
    """Construye el mensaje de bienvenida de la aplicación."""
    return "Hola {}!".format(nombre)


def main():
    """Punto de entrada de la aplicación."""
    print(saludar())

    primer_numero = 10
    segundo_numero = 50

    print("Operandos: {} y {}".format(primer_numero, segundo_numero))
    print("Suma: {}".format(sumar(primer_numero, segundo_numero)))
    print("Resta: {}".format(restar(primer_numero, segundo_numero)))
    print("Multiplicación: {}".format(multiplicar(primer_numero, segundo_numero)))
    print("División: {}".format(dividir(primer_numero, segundo_numero)))

    try:
        dividir(primer_numero, 0)
    except ZeroDivisionError as error:
        print("División entre cero controlada: {}".format(error))

    print("Aplicación ejecutada correctamente desde el flujo de CI/CD.")


if __name__ == "__main__":
    main()
