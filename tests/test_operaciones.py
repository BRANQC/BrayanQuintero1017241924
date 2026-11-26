"""Pruebas unitarias de las operaciones aritméticas."""

import pytest

from operaciones import dividir, multiplicar, restar, sumar


def test_sumar():
    """La suma de dos números positivos es correcta."""
    assert sumar(10, 50) == 60


def test_sumar_negativos():
    """La suma funciona con números negativos."""
    assert sumar(-10, -5) == -15


def test_restar():
    """La resta de dos números es correcta."""
    assert restar(50, 10) == 40


def test_multiplicar():
    """La multiplicación de dos números es correcta."""
    assert multiplicar(10, 50) == 500


def test_multiplicar_por_cero():
    """Cualquier número multiplicado por cero es cero."""
    assert multiplicar(10, 0) == 0


def test_dividir():
    """La división de dos números es correcta."""
    assert dividir(50, 10) == 5


def test_dividir_entre_cero():
    """La división entre cero lanza la excepción esperada."""
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
