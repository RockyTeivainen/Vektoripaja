"""SVG-tiedostojen tuonti."""

import xml.etree.ElementTree as ET
from pathlib import Path

from svgelements import Path as SvgPath
from svgelements import SVG


def tuo_svg(tiedostopolku: str | Path) -> list[SvgPath]:
    """Lukee SVG-tiedoston ja palauttaa sen piirrospolut."""
    polku = Path(tiedostopolku)
    if polku.suffix.lower() != ".svg":
        raise ValueError("Tiedoston pitää olla .svg- tai .obj-päätteinen.")

    juuri = ET.parse(polku).getroot()
    if any(
        isinstance(element.tag, str)
        and element.tag.rsplit("}", 1)[-1].lower() == "script"
        for element in juuri.iter()
    ):
        raise ValueError("Tiedostossa on vihamielistä koodia, tiedosto hylätään.")

    return [
        element
        for element in SVG.parse(str(polku)).elements()
        if isinstance(element, SvgPath)
    ]
