# Dokumentation projekt
====================
## Mål för projekt
Målet med detta projekt är att skapa ett memory-spel. I konsolen ska det slumpas fram 
en siffersekvens som sedan blir längre och längre för varje gång du svarar rätt. Det måste även finnas 
någon form av tidsbegränsning innan siffersekvensen försvinner och då man måste gissa. Det finns alltså vissa delmål med detta projekt för att slutresultatet ska bli som ett slags spel.
## Delmål för projekt
- Slumpmässigt skapa en sekvens med siffor i en lista
- Spara poäng i en variabel?
- Nedräkning
## 2025/01/14
Idag har jag gjort det mesta i spelet. Jag har skapat en string för varje siffersekvens där de ökar i antal. Värden i form av ental slumpas fram som sedan sparas i varje text. Jag valde att spara siffersekvensen i "strings" istället för listor för att slippa konverta mellan datatyper när man ska gissa siffrorna. För att få det att fungera fick jag importera "random". Jag importerar även "sleep" från "time" för att kunna göra en nedräkning i programmet. Till sist importerade jag "os" för att kunna rensa konsolen i Windows. Jag skapade sedan en variablel för antalet sekunder det tar innan skärmen rensas. Därefter använde jag while-slingor för dra bort 1 från variabeln tills seconds=0. Sedan efter 5 sekunder rensas skärmen och man behöver gissa siffersekvensen. Om ditt svar är samma som textslingan får du rätt. Till detta använde jag if-satser. Till nästkommande fråga insåg jag att jag behövde skriva ett nytt värde för "seconds" eftersom variabeln blev nollställd i den föregående nedräkningen. Problemet som kvarstår är däremot att jag inte får rätt utskrift om svaret är fel, dessa lägger jag i "else" men de verkar inte appliceras. Det blir även ganska många nestade if-satser vilket gör koden svår att arbeta med. En annan förbättringsåtgärd, hade varit att göra koden lite mer övergripande dvs att spelet i teorin bör kunna fortsätta i all oändlighet. Jag skulle alltså kunna göra koden lite mer effektiv så att jag inte behöver upprepa kod till exempel.
## 2025/01/28
Idag känner jag mig mer eller mindre färdig med det första projektet, dvs memory-spelet. Jag testade dock att göra en mer optimerad version med funktioner och while-slingor, detta gjorde att det krävdes mindre kod och att spelet faktiskt fungerade felfritt. Jag tog hjälp av ChatGPT för att justera koden efter min ursprungliga kod som referens. Jag förstod koden men det fanns däremot vissa komponenter som jag inte var bekant med. Jag vill ändå påstå att jag begriper koden men jag hade troligen inte kunnat slutföra spelet på egen hand. Idag har jag installerat pygame och skapat en ny python-fil för en animerings-uppgift med en rektangel som ska studsa i fönstret.
## Summering moment memory-projekt:
- Klart: Slumpmässigt skapa en sekvens med siffror i en string (istället för lista)
- Klart: Nedräkning (samt rensning av konsolen)
- Inte klart: Spara poäng i en variabel (detta var onödigt eftersom spelet helt enkelt fortsätter om du svarar rätt)
## 2025/02/03
Idag har jag bytt från att använda Windows till Linux eftersom Git varken går att använda eller ominstallera i Windows. Sedan förra veckan har jag fått VSCodium att fungera i Linux, så när detta numera fungerar har jag nu fått installera pygame igen fast på Linux.
