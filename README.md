# Elokuva-arvostelut

##Sovelluksen toiminta

*  Sovelluksessa käyttäjät pystyvät jakamaan elokuva-arvostelujaan.
*  Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
*  Käyttäjä pystyy lisäämään elokuva-arvosteluja ja muokkaamaan ja poistamaan niitä.
*  Käyttäjä näkee sovellukseen lisätyt arvostelut.
*  Käyttäjä pystyy etsimään arvosteluja hakusanalla.
*  Käyttäjäsivu näyttää, montako arvostelua käyttäjä on lisännyt ja listan käyttäjän lisäämistä arvosteluista.
*  Käyttäjä pystyy valitsemaan arvostelulle yhden tai useamman luokittelun (esim. draama, komedia, jännitys, toiminta).
*  Käyttäjä pystyy antamaan arvostelulle kommentin ja tykkäyksen. Arvosteluista näytetään kommentit ja tykkäysten lukumäärä.

## Sovelluksen asennusohjeet

Asenna ensin tietokoneellesi `flask`-kirjasto kirjoittamalla komentoriville:

```
$ pip install flask
```

Saat luotua tietokannan taulut seuraavasti:

```
$ sqlite3 database.db < schema.sql
```

Sovellus käynnistyy ajamalla komento:

```
$ flask run
```
