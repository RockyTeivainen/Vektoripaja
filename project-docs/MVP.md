# MVP

## MVP-ominaisuuslista
- Align & Snap Tool
- Bezier Pen 
- Camera Control & View Lock System

- Edit Paths by Nodes 
- Hierarchy-Aware Raycasting (Toisiinsa liittymättömät kappaleet eivät uppoa toisiinsa. Suorassa parent-child-suhteessa olevien kappaleiden on tarkoitus upota hieman toisiinsa, jotta liitoskohdat näyttävät luontevilta eivätkä esimerkiksi jätä näkyvää aukkoa)
- Move Tool 

- Parent-Child Linking & Sockets

- Primary Contour & Depth Profiling 

- Resize Tool (koko objekti)
- Revolve Tool 

- Selection Tool 
- Structural Mapping & Layer Extraction
- Surface Lock & Parametric Adaptability (UV Surface-Binding) 

- Viewport Navigation & Canvas Interface 
- Volumetric Inflation Algorithms
- Vector-based zoom up to 200%







## MVP:n jälkeen tulevat ominaisuudet
- Rotate Tool 
- Pivot Mechanics & Repositioning
- Mesh Pipeline 

- Polyhedra Placeholders 
- Boolean-operariot (yhdistäminen ja leikkaaminen)
## Miksi?
Alkuperäinen orientaatio periytyy 2D luonnosten perusteella ja kappaleen kääntely on poikkeus ohjelman perustoimintaan.
Mesh pipeline-osio on pienempiä yksityiskohtia varten eli ei välttämättömyys.

Monitahokkaat ja niihin liittyvät luonnos placeholderit toimivat eri periaatteella kuin ydintoiminta.
Tarkoitus on, että esim. sivuprofiilin luonnos on mahdollisimman tarkka ja kirjaimellinen kuvaus kyseisen kuvakulman siluetista.

Boolean-operaatiot eivät ole suoraan osa "Kolmiulotteista piirtämistä" eli ohjelman perusperiaatetta, joten se on P2-version ominaisuus.

Loput ominaisuudet taas ovat osa perustoiminnallisuutta ja käyttöliittymää, jolloin ne kuuluvat P0-versioon



