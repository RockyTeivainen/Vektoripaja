"""Sovelluksen teema: Qt-tyylit tiedostosta teema.qss ja 3D-näkymän värit.

Käyttö ikkunassa:
    from vektoripaja.teema import lataa_teema, TAUSTA, KOROSTUS
    lataa_teema(app)                  # app on QApplication
    plotter.set_background(TAUSTA)    # PyVistan 3D-näkymä
"""
from pathlib import Path

TAUSTA = "#000000"
KOROSTUS = "#1fa4e3"

# teema.qss on tämän tiedoston vieressä. Valmiissa .exe:ssä PyInstaller
# kopioi sen samaan paikkaan (katso vektoripaja.spec, kohta datas).
QSS = Path(__file__).with_name("teema.qss")


def lataa_teema(app) -> None:
    """Asettaa teeman koko sovellukseen."""
    from PySide6.QtGui import QFont

    fontti = app.font()
    fontti.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 1)
    app.setFont(fontti)
    app.setStyleSheet(QSS.read_text(encoding="utf-8"))
