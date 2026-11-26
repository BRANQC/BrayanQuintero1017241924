# Actividad Guía 5 - Aplicaciones y servicios web

Taller evaluativo (20%) del curso **Aplicaciones y servicios web** del ITM.
El objetivo es configurar un flujo de **Integración Continua y Despliegue
Continuo (CI/CD)** con **GitHub Actions**, de forma que cada commit sobre la
rama `main` dispare automáticamente la construcción, las pruebas y la
ejecución del proyecto.

## Tecnologías

- Python 3.12
- pytest (pruebas unitarias)
- pytest-cov (cobertura de pruebas)
- flake8 (análisis estático de código)
- GitHub Actions (CI/CD)

## Estructura del proyecto

```
.
├── .github/workflows/ci.yml   Definición del flujo de CI/CD
├── tests/                     Pruebas unitarias
├── main.py                    Aplicación principal
├── operaciones.py             Operaciones aritméticas
├── validaciones.py            Validación de datos de entrada
├── requirements.txt           Dependencias del proyecto
└── pytest.ini                 Configuración de pytest
```

## Ejecución local

```bash
python -m pip install -r requirements.txt
python main.py
pytest -v
```

## Flujo de CI/CD

El archivo `.github/workflows/ci.yml` se activa con cada `push` o
`pull_request` sobre la rama `main` y ejecuta los siguientes pasos sobre un
runner `ubuntu-latest`:

1. Clonación del repositorio.
2. Configuración del entorno de Python.
3. Instalación de dependencias.
4. Análisis estático del código con flake8.
5. Ejecución de las pruebas unitarias con reporte de cobertura.
6. Ejecución de la aplicación.

## Autor

Brayan Quintero - Instituto Tecnológico Metropolitano (ITM)
