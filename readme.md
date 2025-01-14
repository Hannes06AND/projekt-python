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
Idag har jag gjort det mesta i spelet. Jag har skapat en string för varje siffersekvens där de ökar i antal. Värden i form av ental slumpas fram som sedan sparas i varje text. För att få det att fungera fick jag importera "random". Jag importerar även "sleep" från "time" för att kunna göra en nedräkning i programmet. Till sist importerade jag "os" för att kunna rensa konsolen i Windows. Jag skapade sedan en variablel för antalet sekunder det tar innan skärmen rensas. Därefter använde jag while-slingor för dra bort 1 från variabeln tills seconds=0. Sedan efter 5 sekunder rensas skärmen och man behöver gissa siffersekvensen. Om ditt svar är samma som textslingan får du rätt. Till detta använde jag if-satser. Till nästkommande fråga insåg jag att jag behövde skriva ett nytt värde för "seconds" eftersom variabeln blev nollställd i den föregående nedräkningen. Problemet som kvarstår är däremot att jag inte får rätt utskrift om svaret är fel, dessa lägger jag i "else" men de verkar inte appliceras. Det blir även ganska många nestade if-satser vilket gör koden svår att arbeta med. En annan förbättringsåtgärd, hade varit att göra koden lite mer övergripande dvs att spelet i teorin bör kunna fortsätta i all oändlighet. Jag skulle alltså kunna göra koden lite mer effektiv så att jag inte behöver upprepa kod till exempel.