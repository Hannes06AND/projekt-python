# Dokumentation projekt
====================
## Mål för projekt
Målet med detta projekt är att skapa ett memory-spel. I konsolen ska det slumpas fram 
en siffersekvens som sedan blir längre och längre för varje gång du svarar rätt. Det måste även finnas 
någon form av tidsbegränsning innan siffersekvensen försvinner och då man måste gissa. Det finns alltså vissa delmål med detta projekt för att slutresultatet ska bli som ett slags spel.
## Delmål för projekt
- Slumpmässigt skapa en sekvens med siffor i en lista
- Spara poäng i en variabel
- Tidtagarur
## 2025/01/14
Idag har jag gjort det mesta i spelet. Jag har skapat en string för varje siffersekvens där de ökar i antal. Värden slumpas fram som sedan sparas i varje text. För att få det att fungera fick jag importera "random". Jag importerar även "sleep" från "time" för att kunna göra en nedräkning i programmet. Till sist importerar jag "os" för att kunna rensa konsolen i Windows.