# Vektoripaja

Vektoripaja on Windows-työpöytäsovelluksen kehitysprojekti. Tavoitteena on
auttaa vektorigrafiikkaa osaavia käyttäjiä tekemään 3D-malleja tutusta
SVG-piirroksesta ilman perinteisen 3D-mallinnuksen piste- ja särmätyöskentelyä.
Sovellus pyrkii käyttämään yleistä SVG-muotoa, jota voi tehdä ja muokata eri
vektorigrafiikkaohjelmissa, eikä edellytä Inkscape-kohtaista tiedostomuotoa.

## Tavoiteversion työnkulku

1. Käyttäjä avaa SVG-piirroksen Vektoripajassa. Piirroksen ryhmät ja muut
   tunnistettavat osat muodostavat 3D-mallin osat ja niiden hierarkian.
   Hierarkian ansiosta esimerkiksi pään voi pitää kiinni vartalossa ja siirtää
   niitä yhdessä.
2. Puoliprofiilista muodostetaan pyörähdyskappale, kuten maljakko. Piirroksen
   viivasta muodostetaan putki, kuten johto tai sarvi. Näin SVG:n muodoista
   syntyy vähämonikulmaisia 3D-kappaleita.
3. Käyttäjä valitsee mallin osia ja muokkaa niitä siirtämällä, kiertämällä ja
   skaalaamalla. Mallia voi tarkastella suoraan edestä, sivulta ja ylhäältä;
   käyttöliittymän tavoitteena on antaa 3D-näkymälle tilaa ja käyttää selkeitä,
   suuria painikkeita sekä hyvää kontrastia.
4. Keskeneräisen työn voi tallentaa ja avata myöhemmin samassa tilassa. Kun
   SVG:tä muokataan toisessa vektorigrafiikkaohjelmassa, mallin voi päivittää
   ilman, että koko työ aloitetaan alusta.
5. Valmis malli viedään OBJ-tiedostoksi siten, että jokainen mallin osa säilyy
   omana objektinaan ja tiedostoa voi jatkokäyttää toisessa ohjelmassa.

### Ehdotus SVG:n päivittämiseen

Yksinkertainen ja editorista riippumaton tapa olisi, että käyttäjä tallentaa
muokatun SVG:n ja valitsee Vektoripajassa **Päivitä SVG:stä**. Sovellus lukee
tiedoston uudelleen ja päivittää geometrian säilyttäen mallin osien muokkaukset
ja asetukset silloin, kun osan tunniste pysyy samana. SVG:n standardin mukaista
`id`-tunnistetta voisi käyttää osan tunnistamiseen päivitysten välillä.
Lisätyt, poistetut tai tunnisteeltaan muuttuneet osat näytettäisiin käyttäjälle
selkeästi, jotta sovellus ei hiljaisesti hukkaa tehtyä työtä.

Tämä on ehdotus toteutustavaksi, ei nykyisen prototyypin ominaisuus eikä vielä
vahvistettu toteutuspäätös. Se ei edellytä taustalla pyörivää tiedostovahtia ja
toimii yleisen SVG-työnkulun kanssa.

Projektin tavoitteita ja suunnitteluratkaisuja kuvataan tarkemmin tiedostossa
[project-docs/suunnitelma.md](project-docs/suunnitelma.md). Vaatimusten
alkuperäinen määrittely on [projektin määrittelysivulla](https://mattiseise.github.io/projektikoontisivu/vektoripaja/).

## Nykyinen versio

Sovellus on prototyyppi: sen käyttöliittymässä näkyy pyörivä testikuutio.
Yllä kuvatut SVG:n tuonti, mallinnus, muokkaus, tallennus, päivittäminen ja
OBJ-vienti ovat tavoiteversion ominaisuuksia, eivät vielä käyttöliittymästä
käytettävissä.

Erillinen itsetesti lukee projektin esimerkkitiedoston
`esimerkit/esimerkki.svg`, muodostaa testigeometriaa ja tarkistaa OBJ-viennin.
Itsetesti ei tarkoita, että nämä toiminnot olisivat käytettävissä sovelluksen
käyttöliittymässä.

## Vaatimukset

- Windows
- Python 3.13 kehitystä ja lähdekoodista käynnistämistä varten

Valmiiksi rakennettu Windows-versio on tarkoitettu toimimaan ilman Pythonin
asennusta.

## Kehitysympäristön käyttöönotto

Avaa PowerShell projektin juuressa ja suorita:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r project-docs\requirements.txt
```

Käynnistä sovellus:

```powershell
.\.venv\Scripts\python.exe main.py
```

Lisää käynnistys-, itsetesti- ja asennusohjeita on tiedostossa
[Käyttöohje.md](Käyttöohje.md).

## Testit ja itsetesti

Aja automaattiset testit projektin juuressa:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Suorita sovelluksen riippuvuuksia ja SVG-/geometria-/OBJ-käsittelyä tarkistava
itsetesti ilman käyttöliittymän avaamista:

```powershell
.\.venv\Scripts\python.exe main.py --itsetesti
```

Itsetestin loki kirjoitetaan tiedostoon
`%TEMP%\vektoripaja-itsetesti.log`.

## Windows-version rakentaminen

Kun kehitysympäristö on asennettu, suorita projektin juuressa:

```bat
rakenna_exe.bat
```

Rakennustulos tulee kansioon `dist\Vektoripaja\`. Käynnistä
`Vektoripaja.exe` ja säilytä `_internal`-kansio sen vieressä. Katso tarkemmat
käynnistysohjeet tiedostosta [Käyttöohje.md](Käyttöohje.md).

## Projektin rakenne

- `main.py` käynnistää sovelluksen tai itsetestin.
- `vektoripaja/ikkuna.py` sisältää nykyisen testikäyttöliittymän.
- `vektoripaja/kierto.py` sisältää kiertokulman laskentafunktion.
- `vektoripaja/itsetesti.py` toteuttaa sovelluksen itsetestin.
- `vektoripaja/teema.py` ja `vektoripaja/teema.qss` määrittävät käyttöliittymän teeman.
- `esimerkit/` sisältää itsetestin SVG-esimerkin.
- `tests/` sisältää automaattiset testit.
- `project-docs/` sisältää suunnitelmat, dokumentaation ja riippuvuuslistan.

## Käytetyt kirjastot

Projektissa käytetään muun muassa Pythonia, PySide6:ta, PyVistaa, pyvistaqt:ta,
trimeshiä, NumPya, svgelements-kirjastoa, pytestiä ja PyInstalleria.
Riippuvuuksien versiot on määritelty tiedostossa
`project-docs/requirements.txt`.
