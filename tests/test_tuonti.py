import pytest

from vektoripaja.tuonti import tuo_svg


# Testi 3: oma piirros. Siinä on kolme polkua, joten tuonti palauttaa kolme polkua.
def test_3_kolme_polkua():
    polut = tuo_svg("Testiaineisto/oma-piirros.svg")
    assert len(polut) == 3


# Testi 4: haitallinen tiedosto. Tuonti hylkää tiedoston, koska siinä on skripti.
def test_4_haitallinen_svg():
    with pytest.raises(ValueError, match="Tiedostossa on vihamielistä koodia, tiedosto hylätään."):
        tuo_svg("Testiaineisto/haitallinen.svg")

# Testi 5: tiedosto, joka ei ole SVG. Tuonti antaa virheilmoituksen.
def test_5_ei_svg():
    with pytest.raises(ValueError, match="Tiedoston pitää olla .svg- tai .obj-päätteinen."):
        tuo_svg("Testiaineisto/ei-svg.txt")