# Vektoripaja – ohjeet GitHub Copilotille

## Projekti
Windows-työpöytäsovellus (Python): low-poly 3D-mallinnin.
Inkscapen SVG → 3D-malli → .obj-tiedosto.
Tekninen pohja: Python 3.13, PySide6 (Qt), PyVista ja pyvistaqt
(3D-näkymä), trimesh ja numpy (geometria ja OBJ), svgelements (SVG)
ja pytest (testit).
Käynnistys: python main.py
Julkaisu: PyInstaller tekee Windows-version, joka toimii ilman Pythonia.

## Rakenne
(Täydennä viikolla 43: kansiot ja moduulien rajat.)
Testit ovat kansiossa tests/: tests/test_nimi.py.

## Säännöt
- Toteuta vain tehtäväkortin tehtävä.
- Muuta vain kortin Tiedostot-kohdassa lueteltuja tiedostoja.
- Älä muuta testejä. Testit kirjoittaa opiskelija.
- Älä refaktoroi pyytämättä.
- Älä lisää pip-paketteja ilman lupaa. Uusi paketti menee requirements.txt:hen.
- Geometria- ja muunnosfunktiot ovat puhtaita funktioita ilman Qt:ta.
- Kysy, jos kortti on epäselvä. Älä arvaa.
- Kun kortti pyytää funktiota, kirjoita puhdas funktio.
- Koodin ja commitien kieli: ___ (oma valintasi).
- Vastaa suomeksi.
