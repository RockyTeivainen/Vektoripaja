"""Tarkistaa kehitysympäristön: Python-versio, virtuaaliympäristö ja kirjastot.

Aja repositoryn kansiossa:  python tarkista_ymparisto.py

Jokainen tarkistusrivi alkaa sanalla OK tai KORJAA. Jos rivillä lukee KORJAA,
tee rivin alla oleva ohje. Aja sitten tarkistus uudelleen.
"""
import re
import sys
from importlib import metadata
from pathlib import Path

PYTHON = (3, 13)
JUURI = Path(__file__).resolve().parent
VAATIMUKSET = JUURI / "requirements.txt"


def lue_vaatimukset(polku: Path) -> dict:
    """Palauttaa {kirjasto: versio} riveistä, jotka ovat muotoa nimi==versio. Kommentit ohitetaan."""
    tulos = {}
    for rivi in polku.read_text(encoding="utf-8-sig").splitlines():
        rivi = rivi.split("#", 1)[0].strip()
        osuma = re.fullmatch(r"([A-Za-z0-9_.-]+)\s*==\s*([^\s;]+)", rivi)
        if osuma:
            tulos[osuma.group(1)] = osuma.group(2)
    return tulos


def main() -> int:
    virheita = 0

    def ok(teksti):
        print(f"OK      {teksti}")

    def korjaa(teksti, ohje):
        nonlocal virheita
        virheita += 1
        print(f"KORJAA  {teksti}\n        → {ohje}")

    versio = sys.version_info
    if versio[:2] == PYTHON:
        ok(f"Python {versio.major}.{versio.minor}.{versio.micro}")
    else:
        korjaa(f"Python {versio.major}.{versio.minor}, pitää olla {PYTHON[0]}.{PYTHON[1]}",
               "Valitse VS Codessa Python: Select Interpreter. Valitse sitten tulkki, jonka polussa on .venv.")

    venv = Path(sys.prefix)
    if sys.prefix != sys.base_prefix and venv.name == ".venv":
        ok(f"virtuaaliympäristö päällä: {venv}")
    else:
        korjaa("virtuaaliympäristö .venv ei ole päällä",
               "Valitse VS Codessa Python: Select Interpreter. Valitse sitten tulkki, jonka polussa on .venv. Avaa uusi terminaali.")

    if not VAATIMUKSET.exists():
        korjaa("requirements.txt puuttuu", "Pura viikon 41 pohja repositorysi kansioon.")
    else:
        for nimi, haluttu in lue_vaatimukset(VAATIMUKSET).items():
            try:
                asennettu = metadata.version(nimi)
            except metadata.PackageNotFoundError:
                korjaa(f"{nimi} puuttuu", "Aja terminaalissa pip install -r requirements.txt")
                continue
            if asennettu == haluttu:
                ok(f"{nimi} {asennettu}")
            else:
                korjaa(f"{nimi} {asennettu}, requirements.txt:ssä {haluttu}",
                       "Aja terminaalissa pip install -r requirements.txt")

    print()
    if virheita:
        print(f"Korjattavaa: {virheita}. Tee ohjeet. Aja sitten tarkistus uudelleen.")
        return 1
    print("Ympäristö on kunnossa.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
