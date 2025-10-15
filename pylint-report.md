# Pylint-raportti

Alla on raportti, jonka Pylint antaa sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:44:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:67:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:91:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:101:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:114:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:139:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:156:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:174:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:174:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:193:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:193:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:210:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:216:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:244:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:262:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:295:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:308:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:295:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:315:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:319:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:342:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:351:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:342:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:362:0: C0116: Missing function or method docstring (missing-function-docstring)
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
reviews.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:48:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:65:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:73:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:79:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:90:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:109:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:113:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:117:0: C0116: Missing function or method docstring (missing-function-docstring)
reviews.py:122:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

------------------------------------------------------------------
Your code has been rated at 8.43/10 (previous run: 8.43/10, +0.00)
```

Käyn seuraavaksi läpi raportin sisällön ja perustelen, miksi raportissa mainittuja asioita ei ole korjattu sovelluksessa.

## Docstring-ilmoitukset

Suurin osa raportin ilmoituksista koskee docstringiä seuraavaan tapaan:

```
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)D
```

Pylint antaa nämä ilmoitukset, koska en ole käyttänyt docstring-kommentteja sovelluksessani. Docstring-kommentit eivät kuulu kurssin vaatimuksiin, joten olen tietoisesti jättänyt ne pois.


## Tarpeeton else-haara

Pylint-ilmoitusten joukossa on muutama ilmoitus tarpeettomista else-haaroista:

```
users.py:25:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

Kurssin materiaalin tavoin katson, että näissä tapauksissa koodi on selkeämpää else-haarojen kanssa, joten olen jättänyt ne koodiin.

## Palautusarvojen puuttuminen

Ilmoituksissa on useampi seuraavanlainen ilmoitus:

```
app.py:174:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Näissä tilanteissa funktio käsittelee metodit GET ja POST, mutta ei muita metodeita. Koska funktion dekoraattorin vaatimuksena on joko GET tai POST, niin ei ole riskiä siitä, ettei funktio palauttaisi mitään arvoa.

## Vaarallinen oletusarvo

Raportissa nousee esiin useampi ilmoitus, joka koskee vaarallista oletusarvoa:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Parametrin oletusarvona on tyhjä lista, josta voi muodostua ongelma, jos sama oletusarvoinen tyhjä lista on jaettu kaikkien funktion kutsujen kesken ja listaa jostain syystä muutettaisiin jossain kutsussa. Tällöin muutos välittyisi myös muihin kutsuihin. Koska koodi ei muuta listaa, tästä ei käytännössä muodostu ongelmaa.
