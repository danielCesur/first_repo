from src.main.scripts.main import *


def test_almacenarFrase():
    assert almacenarFrase("hola que tal") == "HOLA QUE TAL"


def test_cantidadDePalabras():
    assert cantidadDePalabras("hola que tal") == 3


def test_opcionAdivinarLetra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: "A")
    assert opcionAdivinarLetra(5, "HOLA QUE TAL") == 5
