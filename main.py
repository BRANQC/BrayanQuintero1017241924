"""Aplicación principal del taller de Aplicaciones y servicios web.

Actividad de la Guía de Trabajo No. 5 - Taller evaluativo 20%.
Esta aplicación es la que ejecuta el flujo de CI/CD en GitHub Actions.
"""


def saludar(nombre="estudiantes del ITM"):
    """Construye el mensaje de bienvenida de la aplicación."""
    return "Hola {}!".format(nombre)


def main():
    """Punto de entrada de la aplicación."""
    print(saludar())
    print("Aplicación ejecutada correctamente desde el flujo de CI/CD.")


if __name__ == "__main__":
    main()
