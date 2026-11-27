"""Pruebas unitarias de las validaciones de entrada."""

import pytest

from validaciones import VALOR_MAXIMO_PERMITIDO, validar_numero


def test_validar_numero_entero():
    """Un entero en texto se convierte correctamente."""
    assert validar_numero("10") == 10


def test_validar_numero_decimal():
    """Un decimal en texto se convierte correctamente."""
    assert validar_numero("2.5") == 2.5


def test_validar_numero_vacio():
    """Un valor vacío es rechazado."""
    with pytest.raises(ValueError):
        validar_numero("")


def test_validar_numero_nulo():
    """Un valor nulo es rechazado."""
    with pytest.raises(ValueError):
        validar_numero(None)


def test_validar_numero_no_numerico():
    """Un texto no numérico es rechazado."""
    with pytest.raises(ValueError):
        validar_numero("abc")


def test_validar_numero_fuera_de_rango():
    """Un valor que supera el máximo permitido es rechazado."""
    with pytest.raises(ValueError):
        validar_numero(VALOR_MAXIMO_PERMITIDO + 1)
