# Vektoripaja – suunnitelma

> Kirjoita oma tekstisi jokaisen >-ohjerivin jälkeen omalle rivilleen. Älä poista ohjerivejä.
> Kirjoita päätös sillä viikolla, joka otsikossa lukee. Tee jokaisen muutoksen jälkeen commit ja push.

## A · Perustiedot
> Projektin nimi ja tekijä. Kirjoita ne viikolla 40.

### Projektin nimi (viikko 40)
> Vektoripaja

### Tekijä (viikko 40)
> Rocky

## 1 · Tavoite
> Esitäytetty toimeksiannosta. Älä muuta.

Windowsilla toimiva työpöytäsovellus, joka avaa Inkscapessa piirretyn SVG-tiedoston ja tekee siitä
low-poly-mallin. Layerit ja ryhmät muuttuvat mallin osiksi, puoliprofiilista syntyy pyörähdyskappale
ja viivasta putki. Malli viedään .obj-tiedostoksi niin, että jokainen osa on oma objektinsa.

## 2 · Asiakkaat ja käyttäjät
> Esitäytetty toimeksiannosta. Älä muuta.

Asiakkaat ovat Matti Seise ja Antti Honkasalo. Käyttäjät ovat opiskelijoita, jotka piirtävät
sujuvasti Inkscapessa mutta jäävät jumiin perinteisissä 3D-ohjelmissa.
Vaatimukset ja niiden tärkeysjärjestys: https://mattiseise.github.io/projektikoontisivu/vektoripaja/#view-toimeksianto

## 3 · Omat päätökset
> Sinun päätöksesi ja perustelusi. Jokaisen otsikon viikko kertoo, milloin kirjoitat.

### MVP omin sanoin (viikko 40)
> Mikä kuuluu pakolliseen ytimeen ja miksi? Mitkä asiat odottavat ja miksi?

Pakolliseen ytimeen kuuluvat SVG-tuonti, layerien ja ryhmien muuttaminen osiksi, pyörähdyskappaleiden ja putkien tekeminen, osien valinta, siirto ja skaalaus, suorat näkymät, kameran lukitus, .obj-vienti ja tallennus. Ehdotuksessa myös kierto ja kiertopiste kuuluvat ytimeen, mutta päätän siirtää ne P1-osioon. Kameran kääntö tasakulmiin, Bézier-kynä ja polkujen tukipisteiden muokkaus nostetaan P0-osioon, koska ne ovat oleellisia epäsäännöllisten kappaleiden tekemisessä. SVG:n päivitys ja muut tärkeän jatkon ominaisuudet odottavat, koska ne eivät kuulu ensimmäisen toimivan version ytimeen.

#### Tekninen ehdotus

Python, PySide6, PyVista, trimesh ja pytest. PySide6 tekee ikkunan ja painikkeet. PyVista piirtää 3D-näkymän. trimesh tekee 3D-kappaleet ja .obj-tiedoston. pytest ajaa testit. Päätän viikolla 41, hyväksynkö ehdotuksen.

#### Valmiit osat

svgelements lukee SVG:n. trimesh tekee pyörähdyskappaleen ja .obj-tiedoston. PyVista tekee putken ja näyttää mallin suoraan edestä, sivulta ja ylhäältä.

#### Pakollinen ydin ennen joulua

Alkuperäiseen ehdotukseen kuuluivat SVG-tuonti, layerit ja ryhmät osiksi, pyörähdyskappale 3–32 segmentillä, putki 3–8 sivulla, valinta, siirto, kierto ja skaalaus, kiertopiste eli pivot, suorat näkymät, kameran lukitus eli view lock, .obj-vienti sekä tallennus. Ehdotuksen ratkaisussa kiertotyökalu ja kiertopiste siirretään P1-osioon. JSON on ehdotettu tallennusmuoto. Vertaan tallennusvaihtoehtoja viikolla 50 ja perustelen valintani suunnitelmassa.

#### Tärkeä jatko loman jälkeen

Alkuperäisessä jatkolistassa olivat SVG:n päivitys, kameran kääntö tasakulmiin, pieni esikatseluikkuna, kierto lapselle ja sen alaosille, oma teema ja isot kahvat, ortografinen näkymä sekä view lockin pikanäppäin. Ehdotuksen ratkaisussa kameran kääntö tasakulmiin nostetaan P0-osioon; muut ominaisuudet jäävät tärkeäksi jatkoksi. Kahva on tartuntakohta, josta osaa siirretään tai kierretään. Ortografisessa näkymässä kaukana olevat osat eivät pienene kuten valokuvassa.

#### Julkaisu

Julkaisu tehdään zip-tiedostona GitHubin julkaisusivulla eli releasessa. GitHub Actions rakentaa Windows-version ja tarkistaa sen. Valmis versio toimii ilman Pythonia.

#### Rajaus

Alkuperäisessä rajauksessa Bézier-kynä ja polkujen muokkaus sovelluksessa, Boolean-toiminnot, platoniset kappaleet, medial axis, UV-sidonta ja törmäyssäännöt jäivät näytön jälkeiseen aikaan. Ehdotuksen ratkaisussa Bézier-kynä ja polkujen tukipisteiden muokkaus kuitenkin nostetaan P0-osioon, koska ne ovat oleellisia epäsäännöllisten kappaleiden tekemisessä.

Piirrän Inkscapessa: sovellus ei ole piirto-ohjelma. Piirros tehdään Inkscapessa ja tuodaan sovellukseen.

Testit ovat minun: en anna GitHub Copilotin muuttaa testejä.

En vaihda tekniikkaa kesken projektin. Jos pohja ei toimi, kerron siitä palaverissa.

#### Ehdotuksen ratkaisu

Hyväksyn ehdotetusta pakollisesta ytimestä kaiken muun paitsi siirrän kiertotyökalun ja kiertopisteen P1-osioon. Kameran kääntö tasakulmiin, Bézier-kynä ja polkujen muokkaus sovelluksessa siirtyvät P0-osioon. Kameran asettaminen tasakulmiin, Bézier-kynä ja polkujen tukipisteiden muokkaaminen ovat oleellisia, kun tehdään epäsäännöllisiä kappaleita.

### Käyttöliittymävaatimus (viikko 43)
> Kirjoita taustaväri, tekstin väri, tekstin koko ja painikkeiden koko.

### Kansiorakenne ja moduulien rajat (viikko 43)
> Kirjoita kansiot ja tiedostot. Kirjoita jokaisen moduulin perään sen yksi vastuu.

### Dokumentointitapa (viikko 43)
> Kirjoita palaverissa sovittu tapa: README ja käyttöohje. Kirjoita palaverin päivä.

### Rajapinnat (viikot 44, 48 ja 49)
> Kirjoita jokaisesta viikon funktiosta nimi, syöte ja paluuarvo.

### Valinnan toiminta (viikko 44)
> Kun käyttäjä napsauttaa osaa, valitaanko lapsi vai koko kappale? Kirjoita päätös ja peruste.

### Revolven valintatapojen vertailu (viikko 44)
> Vertaa kahta tapaa. Kirjoita kummastakin hyvät ja huonot puolet ja oma suosituksesi.

### Revolven valintatapa (viikko 45)
> Kirjoita palaverissa sovittu tapa ja palaverin päivä.

### Profiili akselin väärällä puolella (viikko 45)
> Mitä tehdään, jos profiilin piste on akselin väärällä puolella? Vastaus on testin 11 odotettu tulos.

### Tallennustapa (viikko 50)
> Vertaa tallennustapoja omilla kriteereilläsi. Kirjoita valinta, peruste ja oman tallennustiedostosi koko.

### Tärkeän jatkon järjestys (viikko 2)
> Kirjoita toiminnot järjestyksessä. Kirjoita jokaiselle tuntiarvio ja asiakkaan prioriteetti.

### Osien tunnistus päivityksessä (viikko 3)
> Tunnistetaanko osa nimellä vai tunnisteella? Kirjoita palaverissa sovittu tapa ja peruste.

### Seuraava toiminto (viikko 4)
> Kirjoita, minkä tärkeän jatkon toiminnon teet ja miksi juuri sen.

### Käyttöliittymävaatimuksen tarkistus (viikko 5)
> Mitä viikon 43 käyttöliittymävaatimuksesta vielä puuttuu?

## C · Ohjaajan päätökset
> Kirjoita päätös vasta, kun ohjaaja on päättänyt. Kirjoita myös päivä. Tyhjä kohta on oikein, kunnes asia on sovittu.

### Krediittien lisärahoitus (lokakuun loppuun mennessä)
> Ohjaajan päätös ja päivä.

### Pakollisen ytimen myöhästymisen ratkaisu (viikko 47)
> Ohjaajan päätös ja päivä. Tarvitaan vain, jos pakollinen ydin on myöhässä.

### Katselmoinnin kirjaustapa (ennen viikkoa 51)
> Ohjaajan päätös ja päivä.

### Julkaisutestaaja (viikko 5)
> Kirjoita vain rooli, esimerkiksi toinen opiskelija. Lähetä nimi ohjaajalle Teamsissa.

### Lisenssi (ennen viikkoa 6)
> Ohjaajan päätös ja päivä.

### Näytön ajankohta ja arvioijat (viikko 9)
> Ohjaajan päätös ja päivä.
