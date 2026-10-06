# Projektin toteutuksen suunnitelma

## Tekninen ehdotus, ehdotettu toteutustapa

Python, PySide6, PyVista, trimesh ja pytest. PySide6 tekee ikkunan ja painikkeet. PyVista piirtää 3D-näkymän. trimesh tekee 3D-kappaleet ja .obj-tiedoston. pytest ajaa testit. Päätät viikolla 41, hyväksytkö ehdotuksen.

### Valmiit osat
 svgelements lukee SVG:n. trimesh tekee pyörähdyskappaleen ja .obj-tiedoston. PyVista tekee putken ja näyttää mallin suoraan edestä, sivulta ja ylhäältä.

### Pakollinen ydin ennen joulua
 SVG-tuonti, layerit ja ryhmät osiksi, pyörähdyskappale 3–32 segmentillä, putki 3–8 sivulla, valinta, siirto, kierto ja skaalaus, kiertopiste eli pivot, suorat näkymät, kameran lukitus eli view lock, .obj-vienti sekä tallennus. JSON on ehdotettu tallennusmuoto. Vertailet vaihtoehtoja viikolla 50 ja perustelet valintasi suunnitelmassa.

### Tärkeä jatko loman jälkeen
 Päivitä SVG, kierto tasakulmiin, pieni esikatseluikkuna, kierto lapselle ja sen alaosille, oma teema ja isot kahvat, ortografinen näkymä ja view lockin pikanäppäin. Kahva on tartuntakohta, josta osaa siirretään tai kierretään. Ortografisessa näkymässä kaukana olevat osat eivät pienene kuten valokuvassa.

Julkaisu: zip-tiedosto GitHubin julkaisusivulla eli releasessa. GitHubin automaatio GitHub Actions tekee Windows-version ja tarkistaa sen. Valmis versio toimii ilman Pythonia.

### Pidä rajaus

Jatkolista odottaa: Bézier-kynä ja polkujen muokkaus sovelluksessa, Boolean-toiminnot, platoniset kappaleet, medial axis, UV-sidonta ja törmäyssäännöt. Ne tehdään näytön jälkeen.

Piirrä Inkscapessa: sovellus ei ole piirto-ohjelma. Piirros tehdään Inkscapessa ja tuodaan sovellukseen.

Testit ovat sinun: älä anna GitHub Copilotin muuttaa testejä.

Älä vaihda tekniikkaa kesken projektin. Jos pohja ei toimi, kerro siitä palaverissa.

## Ehdotuksen ratkaisu
Hyväksyn pakollisesta "Pakollinen ydin ennen joulua"-osiosta, paitsi että siirrän kiertotyökalun ja kiertopisteen P1 osioon.

- Kameran kääntö tasakulmiin
- Bézier-kynä
- Polkujen muokkaus sovelluksessa
siirtyy P0 osioon: kameran asettaminern tasakulmiin, Bézier-kynä ja polkujen tukipisteiden muokkaamaninen sovelluksessa ovat oleellisia kun tehdään epäsäännöllisiä kappaleita.

## käyttöliittymävaatimukset
