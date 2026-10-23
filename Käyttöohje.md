# Vektoripajan käyttöohje

## Tietoa nykyisestä versiosta

Vektoripaja on kehitysvaiheessa oleva prototyyppi. Kun käynnistät sovelluksen,
ikkunassa näkyy pyörivä testikuutio. Tässä versiossa SVG-piirrosta ei voi tuoda
käyttöliittymän kautta, eikä käyttöliittymästä voi muokata tai tallentaa
3D-mallia.

Itsetesti kokeilee SVG:n lukemista, testigeometrian muodostamista ja OBJ-vientiä
taustalla. Se on kehittäjille tarkoitettu tarkistus, ei mallinnuksen
käyttötoiminto.

## Sovelluksen käynnistäminen lähdekoodista

Tarvitset Windowsin ja Python 3.13:n.

1. Avaa PowerShell projektin kansiossa.
2. Luo virtuaaliympäristö ja asenna riippuvuudet, jos niitä ei ole vielä
   asennettu:

   ```powershell
   py -3.13 -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Käynnistä sovellus:

   ```powershell
   .\.venv\Scripts\python.exe main.py
   ```

Sovellus avaa 3D-näkymän ja näyttää pyörivän kuution. Sulje ikkuna normaalisti
lopettaaksesi sovelluksen.

## Itsetestin ajaminen

Itsetesti tarkistaa sovelluksen kirjastoja ja niiden yhteistoimintaa. Se lukee
tiedoston `esimerkit/esimerkki.svg`, muodostaa kaksi pyörähdyskappaletta ja
putken sekä tarkistaa, että OBJ-tiedostossa osat ovat erillisiä objekteja.
Testi ei avaa sovellusikkunaa.

Aja testi projektin juuressa:

```powershell
.\.venv\Scripts\python.exe main.py --itsetesti
```

Loki tallentuu tiedostoon `%TEMP%\vektoripaja-itsetesti.log`. Tarkastele sitä
PowerShellissä komennolla:

```powershell
Get-Content "$env:TEMP\vektoripaja-itsetesti.log"
```

Onnistuneen testin viimeisellä rivillä lukee `ITSETESTI LÄPI`. Jos testi
epäonnistuu, lokissa on virheen tiedot.

## Valmiin Windows-version käyttäminen

1. Pura julkaisu- tai rakennuszip kokonaan kansioon. Älä käynnistä ohjelmaa
   zip-tiedoston sisältä.
2. Avaa purettu `Vektoripaja`-kansio.
3. Kaksoisnapsauta `Vektoripaja.exe`-tiedostoa.
4. Pidä `_internal`-kansio samassa kansiossa exe-tiedoston kanssa.

Valmis versio ei tarvitse erillistä Python-asennusta. Nykyisessä prototyypissä
se näyttää saman pyörivän testikuution.

Jos Windows näyttää Microsoft Defender SmartScreen -varoituksen, ohjelmaa ei
välttämättä ole allekirjoitettu. Suorita se vain, jos luotat tiedoston
lähteeseen. Jos päätät jatkaa, avaa **Lisätietoja** ja valitse **Suorita silti**.

## Valmiin version itsetesti

1. Avaa Resurssienhallinnassa kansio, jossa `Vektoripaja.exe` sijaitsee.
2. Kirjoita osoiteriville `cmd` ja paina Enter.
3. Suorita komentokehotteessa:

   ```bat
   start /wait Vektoripaja.exe --itsetesti
   type %TEMP%\vektoripaja-itsetesti.log
   ```

Onnistuneen testin viimeisellä rivillä lukee `ITSETESTI LÄPI`.

## Testien ajaminen kehityksessä

Automaattiset testit voi ajaa projektin juuressa:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## Lisätiedot

Projektin tavoitteet, ominaisuussuunnitelma ja rajaukset löytyvät tiedostosta
[project-docs/suunnitelma.md](project-docs/suunnitelma.md). Riippuvuudet ja
niiden versiot on lueteltu tiedostossa
[requirements.txt](requirements.txt).
