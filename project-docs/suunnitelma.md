<style>
    *{
        background-color: rgb(1, 7, 9);
        color: hsl(199, 77%, 74%);
    }
    h1, h2{
        color: hsl(26, 95%, 30%);
    }
    h3, h4{ 
        color: hsl(226, 82%, 45%);
    }
    /* Style bold text as rounded pill tags */
strong {
    background-color: #03007b !important;
    color: #caa23c !important;
    padding: 2px 8px !important;
    border-radius: 6px !important;
    font-weight: normal !important;
}
ul{
    list-style-type: square;
    color: Red;
    padding: 9px
}
</style>

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

Hyväksyn ehdotetusta pakollisesta ytimestä kaiken muun paitsi siirrän kiertotyökalun ja kiertopisteen P1-osioon. Kameran kääntö tasakulmiin, Bézier-kynä ja polkujen muokkaus sovelluksessa siirtyvät P0-osioon. Kameran asettaminen tasakulmiin, Bézier-kynä ja polkujen tukipisteiden muokkaaminen ovat oleellisia epäsäännöllisiä kappaleita tehdessä.

### Käyttöliittymävaatimus (viikko 43)
> Kirjoita taustaväri, tekstin väri, tekstin koko ja painikkeiden koko.

- pääalueen tausta: tummanvioletti (#120012)
- ikkunan kehys: tummanpunainen (#b00000)
- yläpalkin tausta: oranssi (#ff6800)
- sivupalkin tausta: tummansininen (#000055)
- jakajien väri: keltainen (#ffff00) 

Yläpalkin painikkeissa käytetään vuorotelevia väripareja 
- taustana tummanvihreää (#004500) ja tekstivärinä turkoosia (#00c8df)
- taustana (#000055) ja oranssia (#ff6800) tekstiä

Työkalupainikkeissa värit vuorottelevat: 
- oranssi (#FF6500) tausta, musta (#000000) teksti
- vihreä (#008000), musta (#000000) teksti 
- turkoosi (#00c8df) musta (#000000) teksti. 
Pääalueen tekstit ovat valkoisia.

- yläpalkin lähtökorkeus: 100 px
- yläpalkin vähimmäiskorkeus: 40 px
- sivupalkin lähtöleveys: 246 px
- sivupalkin vähimmäisleveys: 40 px
- yläpalkin painikkeet täyttävät niille varatun tilan
- työkalupainikkeita: 8 neliön muotoista painiketta
- työkalupainikkeiden koko määräytyy sivupalkin käytettävissä olevan tilan mukaan
- yläpalkin painikkeiden tekstikoko: 12–72 px tilan mukaan
- työkalupainikkeiden tekstikoko: 10–48 px tilan mukaan
- painikkeiden teksti sovitetaan painikkeeseen

### Kansiorakenne ja moduulien rajat (viikko 43)

Sovelluksen koodi pidetään `vektoripaja/`-paketissa. Käyttöliittymä, SVG:n luku,
geometria ja tiedostojen vienti erotetaan omiin moduuleihinsa. Geometria- ja
muunnoslaskenta pidetään puhtaissa funktioissa ilman Qt-riippuvuutta, jotta niitä
voi testata erillään käyttöliittymästä. Rakenne kuvaa tavoitetta: uusia moduuleja
lisätään, kun niiden toiminnallisuutta toteutetaan.

```text
Vektoripaja/
├── main.py                    Käynnistää sovelluksen tai itsetestin.
├── vektoripaja/
│   ├── __init__.py            Määrittää sovelluskoodin Python-paketiksi.
│   ├── ikkuna.py              Kokoaa pääikkunan ja välittää käyttäjän toiminnot.
│   ├── nakyma3d.py            Näyttää 3D-mallin ja hallitsee näkymää sekä kameraa.
│   ├── svg_tuonti.py          Lukee SVG:n ja poimii siitä mallinnettavat osat.
│   ├── geometria.py           Muodostaa ja muuntaa 3D-geometriaa puhtaina funktioina.
│   ├── kierto.py              Laskee kiertoon liittyviä arvoja ilman Qt-riippuvuutta.
│   ├── malli.py               Määrittää mallin osien tiedot ja sovelluksen mallin tilan.
│   ├── obj_vienti.py          Vie mallin osat OBJ-tiedostoon.
│   ├── projekti.py            Tallentaa projektin ja avaa sen tallennustiedostosta.
│   ├── teema.py               Lataa sovelluksen tyylit ja tarjoaa yhteiset väriarvot.
│   ├── teema.qss              Määrittää Qt-käyttöliittymän tyylit.
│   └── itsetesti.py           Tarkistaa sovelluksen riippuvuudet ja perustoiminnot.
├── esimerkit/                 Sisältää sovelluksessa käytettäviä esimerkkitiedostoja.
├── tests/                     Sisältää automaattiset testit.
├── project-docs/              Sisältää projektin suunnitelman ja dokumentaation.
├── Päiväkirja/                Sisältää projektin päiväkirjan.
├── AI-loki/                   Sisältää tekoälyn käytön lokit.
└── README.md                  Esittelee projektin ja sovelluksen käynnistämisen.
```

### Dokumentointitapa (viikko 43)
<!-- Soivitaan 20.10.26 -->
> Kirjoita palaverissa sovittu tapa: README ja käyttöohje. Kirjoita palaverin päivä.

### Valinnan toiminta (viikko 45)
> Kun käyttäjä napsauttaa osaa, valitaanko lapsi vai koko kappale? Kirjoita päätös ja peruste.

### Revolven valintatapojen vertailu (viikko 45)
> Vertaa kahta tapaa. Kirjoita kummastakin hyvät ja huonot puolet ja oma suosituksesi.

### Revolven valintatapa (viikko 47)
> Kirjoita palaverissa sovittu tapa ja palaverin päivä.

### Profiili akselin väärällä puolella (viikko 47)
> Mitä tehdään, jos profiilin piste on akselin väärällä puolella? Vastaus on testin 11 odotettu tulos.

### Tallennustapa (viikko 3)
> Vertaa tallennustapoja omilla kriteereilläsi. Kirjoita valinta, peruste ja oman tallennustiedostosi koko.

### Tärkeän jatkon järjestys (viikko 5)
> Kirjoita toiminnot järjestyksessä. Kirjoita jokaiselle tuntiarvio ja asiakkaan prioriteetti.

### Osien tunnistus päivityksessä (viikko 6)
> Tunnistetaanko osa nimellä vai tunnisteella? Kirjoita palaverissa sovittu tapa ja peruste.

### Seuraava toiminto (viikko 7)
> Kirjoita, minkä tärkeän jatkon toiminnon teet ja miksi juuri sen.

### Käyttöliittymävaatimuksen tarkistus (viikko 9)
> Mitä viikon 43 käyttöliittymävaatimuksesta vielä puuttuu?

## C · Ohjaajan päätökset
> Kirjoita päätös vasta, kun ohjaaja on päättänyt. Kirjoita myös päivä. Tyhjä kohta on oikein, kunnes asia on sovittu.

### Krediittien lisärahoitus (lokakuun loppuun mennessä)
> Ohjaajan päätös ja päivä.

### Pakollisen ytimen myöhästymisen ratkaisu (viikko 49)
> Ohjaajan päätös ja päivä. Tarvitaan vain, jos pakollinen ydin on myöhässä.

### Katselmoinnin kirjaustapa (ennen viikkoa 4)
> Ohjaajan päätös ja päivä.

### Julkaisutestaaja (viikko 9)
> Kirjoita vain rooli, esimerkiksi toinen opiskelija. Lähetä nimi ohjaajalle Teamsissa.

### Lisenssi (ennen viikkoa 10)
> Ohjaajan päätös ja päivä.

### Näytön ajankohta ja arvioijat (viikko 12)
> Ohjaajan päätös ja päivä.
