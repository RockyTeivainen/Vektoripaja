# SVG-tiedoston tuonti
Nimi: tuo_svg
Syöte: tiedoston polku tiedostotyyppi mukaanlukien (esimerkiksi testiaineisto/oma-piirros.svg)
Paluuarvo: lista piirroksen poluista (svgelementsin Path-elementit)
Virhe: jos tiedosto ei ole SVG, funktio nostaa virheen ValueError ja näyttää viestin "Tiedoston pitää olla .svg- tai .obj-päätteinen"
Tiedosto: vektoripaja/tuonti.py
## Vihamielinen tiedosto
Tiedosto hylätään ja näytetään viesti "Tiedostossa on vihamielistä koodia, tiedosto hylätään."
## Testi 3: kolme polkua
Syöte: tiedostopolku tiedostotyyppi mukaanlukien (Testiaineisto/oma-piirros.svg)
Odotettu tulos: 3
## Testi 4: vihamielinen svg
Syöte: tiedostopolku "Testiaineisto/haitallinen.svg"
Odotettu tulos: Tiedosto hylätään ja näytetään viesti "Tiedostossa on vihamielistä koodia, tiedosto hylätään."
## Testi 5: väärä tiedosto
Syöte: tiedostopolku "Testiaineisto/ei-svg.txt"
Odotettu tulos: Jos tiedosto ei ole SVG, funktio nostaa virheen ValueError ja näyttää viestin "Tiedoston pitää olla .svg- tai .obj-päätteinen"
