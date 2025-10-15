# Elokuva-arvostelut

## Sovelluksen toiminta

*  Sovelluksessa käyttäjät pystyvät jakamaan elokuva-arvostelujaan.
*  Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
*  Käyttäjä pystyy lisäämään elokuva-arvosteluja ja muokkaamaan ja poistamaan niitä.
*  Käyttäjä pystyy lisäämään kuvia arvosteluun.
*  Käyttäjä näkee sovellukseen lisätyt arvostelut.
*  Käyttäjä pystyy etsimään arvosteluja hakusanalla.
*  Käyttäjäsivu näyttää, montako arvostelua käyttäjä on lisännyt ja listan käyttäjän lisäämistä arvosteluista.
*  Käyttäjä pystyy valitsemaan arvostelulle yhden tai useamman luokittelun (esim. elokuvagenre ja tähtiluokitus).
*  Käyttäjä pystyy antamaan arvostelulle kommentin sekä muokkaamaan ja poistamaan kommenttejaan. Arvosteluista näytetään kommentit.

## Sovelluksen asennusohjeet

Asenna ensin tietokoneellesi `flask`-kirjasto kirjoittamalla komentoriville:

```
$ pip install flask
```

Saat luotua tietokannan taulut seuraavasti:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Sovellus käynnistyy ajamalla komento:

```
$ flask run
```

## Sovelluksen testaus suurella tietomäärällä

Sovellusta on testattu suurella tietomäärällä, ja sen on todettu toimivan nopeasti kaikilla sivupyynnöillä.
Sovelluksen repositorioon on lisätty tiedosto seed.py, jonka avulla voi luoda tietokantaan testiaineiston seuraavalla komennolla:

```
$ python seed.py
```

Testiaineistolla on seuraavat ominaisuudet:
- Käyttäjien määrä on tuhat
- Arvostelujen määrä on sata tuhatta
- Viestien määrä on miljoona
- Jokaiselle arvostelulle valitaan satunnaisesti käyttäjä
- Jokaiselle viestille valitaan satunnaisesti käyttäjä ja arvostelu.

Jotta sovellus toimisi mahdollisimman nopeasti suurillakin tietomäärillä, pääsivulle ja hakutuloksiin  on lisätty sivutus.
Sivutus pääsivulle oli lisätty jo ennen testausta suurilla tietomäärillä, joten sen toimintaa ilman sivutusta ei ole testattu. Oletettavasti sovellus jumiutuisi ilman sivutusta, kun tietomäärä on suuri. Sivutuksen kanssa pääsivu toimii nopeasti.
Hakutuloksiin sivutus puolestaan lisättiin jälkikäteen, kun kävi ilmi, että sovellus meni jumiin, jos hakutuloksia oli paljon. Sivutuksen jälkeen haku toimii nopeasti.
Tietokantaan on myös lisätty indeksit tauluihin items ja messages, jotta tietokantakyselyt toimisivat tehokkaasti.
Sovellukseen on lisätty funktiot before_request ja after_request, joiden avulla voidaan seurata lokista, kuinka nopeasti sovellus vastaa tietopyyntöihin.
