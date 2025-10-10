# Pylint-raportti

Alla on raportti, jonka Pylint antaa sovelluksesta:

...
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:82:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:95:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:120:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:137:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:155:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:155:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:174:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:174:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:191:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:197:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:225:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:243:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:276:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:289:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:276:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:296:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:300:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:320:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:329:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:320:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:340:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module reviews
reviews.py:1:0: C0114: Missing module docstring (missing-module-docstring)
reviews.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:42:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:73:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:84:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:94:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:104:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:108:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:113:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

------------------------------------------------------------------
Your code has been rated at 8.37/10 (previous run: 8.35/10, +0.03)
...

Käyn seuraavaksi läpi raportin sisällön ja perustelen, miksi raportissa mainittuja asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suurin osa raportin ilmoituksista koskee docstringiä seuraavaan tapaan:

...
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)D
...

Pylint antaa nämä ilmoitukset, koska en ole käyttänyt docstring-kommentteja sovelluksessani. Docstring-kommentit eivät kuulu kurssin vaatimuksiin, joten olen tietoisesti jättänyt ne pois.


## Tarpeeton else-haara

Pylint-ilmoitusten joukossa on muutama ilmoitus tarpeettomista else-haaroista:

...
users.py:25:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
...

Kurssin materiaalin tavoin katson, että näissä tapauksissa koodi on selkeämpää else-haarojen kanssa, joten olen jättänyt ne koodiin.

## Palautusarvojen puuttuminen

Ilmoituksissa on useampi seuraavanlainen ilmoitus:

...
app.py:155:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
...

Näissä tilanteissa funktio käsittelee metodit GET ja POST, mutta ei muita metodeita. Koska funktion dekoraattorin vaatimuksena on joko GET tai POST, niin ei ole riskiä siitä, ettei funktio palauttaisi mitään arvoa.

## Vaarallinen oletusarvo

Raportissa nousee esiin useampi ilmoitus, joka koskee vaarallista oletusarvoa:

...
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
...

Parametrin oletusarvona on tyhjä lista, josta voi muodostua ongelma, jos sama oletusarvoinen tyhjä lista on jaettu kaikkien funktion kutsujen kesken ja listaa jostain syystä muutettaisiin jossain kutsussa. Tällöin muutos välittyisi myös muihin kutsuihin. Koska koodi ei muuta listaa, tästä ei käytännössä muodostu ongelmaa.
