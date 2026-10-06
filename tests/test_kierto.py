from vektoripaja.kierto import kiertokulma


def test_1_kiertokulma():
    assert kiertokulma(0, 0.5) == 0
    assert kiertokulma(3, 0.5) == 180
