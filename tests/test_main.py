"""Pruebas unitarias de la aplicación principal."""

import pytest

from main import calcular, main, saludar


def test_saludar_por_defecto():
    """El saludo por defecto contiene el mensaje del curso."""
    assert "estudiantes del ITM" in saludar()


def test_saludar_personalizado():
    """El saludo acepta un nombre personalizado."""
    assert saludar("Brayan") == "Hola Brayan!"


def test_calcular_retorna_las_cuatro_operaciones():
    """El cálculo retorna las cuatro operaciones aritméticas."""
    resultados = calcular("10", "50")
    assert set(resultados) == {"suma", "resta", "multiplicacion", "division"}


def test_calcular_valores_correctos():
    """Los resultados de las operaciones son los esperados."""
    resultados = calcular("10", "50")
    assert resultados["suma"] == 60
    assert resultados["resta"] == -40
    assert resultados["multiplicacion"] == 500


def test_calcular_con_entrada_invalida():
    """Una entrada inválida detiene el cálculo."""
    with pytest.raises(ValueError):
        calcular("abc", "50")


def test_main_imprime_los_resultados(capsys):
    """La ejecución principal imprime el saludo y controla los errores."""
    main()
    salida = capsys.readouterr().out
    assert "estudiantes del ITM" in salida
    assert "Suma" in salida
    assert "Entrada inválida controlada" in salida
    assert "División entre cero controlada" in salida
