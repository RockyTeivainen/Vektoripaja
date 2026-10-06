"""Itsetesti: tarkistaa, että sovellus ja sen kirjastot ovat mukana ja toimivat.

Ajo:  python main.py --itsetesti   tai   Vektoripaja.exe --itsetesti

Itsetesti lukee mukana tulevan tiedoston esimerkit/esimerkki.svg. Se tekee
SVG:n kahdesta profiilista pyörähdyskappaleet ja viivasta putken. Sitten se vie ne
.obj-tiedostoksi väliaikaiskansioon ja tarkistaa, että jokainen osa on oma objektinsa.
Ikkunaa ei avata. Paluukoodi on 0, kun kaikki toimii, ja muuten 1.

Tulos kirjoitetaan myös tiedostoon %TEMP%\\vektoripaja-itsetesti.log, koska
valmiilla .exe:llä ei ole terminaalia, johon tulostaa.
"""
import os
import sys
import tempfile
import traceback
from pathlib import Path

LOKI = Path(tempfile.gettempdir()) / "vektoripaja-itsetesti.log"
PYORAHDYS = ("maljakko", "kansi")
PUTKET = ("sarvi",)
OSAT = PYORAHDYS + PUTKET


def _juuri() -> Path:
    """Kansio, jossa esimerkit/ on: .exe:ssä PyInstallerin purkukansio, muuten repositoryn juuri."""
    return Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[1]))


def _profiilit(svg_polku: Path) -> dict:
    """Lukee SVG:stä polut, joiden id on OSAT-listassa. Palauttaa {nimi: [(x, korkeus), ...]}."""
    from svgelements import SVG, Close, Path as SvgPolku

    tulos = {}
    for elementti in SVG.parse(str(svg_polku)).elements():
        if isinstance(elementti, SvgPolku) and elementti.id in OSAT:
            # SVG:n y-akseli osoittaa alas, 3D:n korkeus ylös: siksi -y.
            pisteet = [(s.end.x, -s.end.y) for s in elementti.segments() if not isinstance(s, Close)]
            tulos[elementti.id] = pisteet
    return tulos


def _tarkista_qt(kirjaa) -> None:
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PySide6.QtCore import QLibraryInfo
    from PySide6.QtWidgets import QApplication

    from vektoripaja.teema import lataa_teema

    app = QApplication.instance() or QApplication([])
    lataa_teema(app)
    liitannaiset = Path(QLibraryInfo.path(QLibraryInfo.LibraryPath.PluginsPath)) / "platforms"
    if sys.platform == "win32" and not (liitannaiset / "qwindows.dll").exists():
        raise RuntimeError(f"Qt:n Windows-liitännäinen puuttuu: {liitannaiset / 'qwindows.dll'}")
    kirjaa(f"OK  Qt ja teema ({', '.join(sorted(p.name for p in liitannaiset.glob('*')))})")


def _tarkista_geometria(kirjaa) -> None:
    import pyvista
    import pyvistaqt  # noqa: F401  (tarkistaa, että 3D-näkymän Qt-osa on mukana)
    import trimesh

    svg = _juuri() / "esimerkit" / "esimerkki.svg"
    profiilit = _profiilit(svg)
    if set(profiilit) != set(OSAT):
        raise RuntimeError(f"SVG:stä löytyi {sorted(profiilit)}, odotettiin {sorted(OSAT)}")
    kirjaa(f"OK  SVG luettu: {svg.name}, polut {', '.join(OSAT)}")

    import numpy

    malli = trimesh.Scene()
    for nimi in PYORAHDYS:
        kappale = trimesh.creation.revolve(profiilit[nimi], sections=12)
        if pyvista.wrap(kappale).n_points == 0:
            raise RuntimeError(f"{nimi}: PyVista ei saanut pisteitä")
        malli.add_geometry(kappale, geom_name=nimi, node_name=nimi)
    for nimi in PUTKET:
        viiva = pyvista.lines_from_points(numpy.array([(x, y, 0.0) for x, y in profiilit[nimi]]))
        putki = viiva.tube(radius=4.0, n_sides=6, capping=True).triangulate()
        kappale = trimesh.Trimesh(vertices=numpy.asarray(putki.points), faces=putki.faces.reshape(-1, 4)[:, 1:], process=False)
        malli.add_geometry(kappale, geom_name=nimi, node_name=nimi)
    for nimi, kappale in malli.geometry.items():
        if len(kappale.faces) == 0:
            raise RuntimeError(f"{nimi}: kappaleessa ei ole tahkoja")
    kirjaa(f"OK  geometria: {len(PYORAHDYS)} pyörähdyskappaletta ja {len(PUTKET)} putki, PyVista {pyvista.__version__}, trimesh {trimesh.__version__}")

    with tempfile.TemporaryDirectory() as kansio:
        obj = Path(kansio) / "itsetesti.obj"
        malli.export(obj)
        objektit = [rivi[2:].strip() for rivi in obj.read_text(encoding="utf-8").splitlines() if rivi.startswith("o ")]
    if sorted(objektit) != sorted(OSAT):
        raise RuntimeError(f"OBJ:n o-rivit {objektit}, odotettiin {list(OSAT)}")
    kirjaa(f"OK  OBJ-vienti: o-rivit {', '.join(objektit)}")


def aja() -> int:
    rivit = []

    def kirjaa(teksti: str) -> None:
        rivit.append(teksti)
        print(teksti)

    kirjaa(f"Vektoripajan itsetesti · Python {sys.version.split()[0]} · {'exe' if getattr(sys, 'frozen', False) else 'kehitys'}")
    try:
        _tarkista_qt(kirjaa)
        _tarkista_geometria(kirjaa)
        kirjaa("ITSETESTI LÄPI")
        koodi = 0
    except Exception:
        kirjaa(traceback.format_exc())
        kirjaa("ITSETESTI EI MENNYT LÄPI")
        koodi = 1
    LOKI.write_text("\n".join(rivit) + "\n", encoding="utf-8")
    return koodi
