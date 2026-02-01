# En simpel Directory Brute-Forcer
Detta verktyg är utvecklat i Python för att karlägga dolda mappar och filer på en webbserver.

# Funktioner :
HTTP Status Checking : identiferar 200 OK, 404 Not found och andra status kod.
Error handling : Använder try/except för att hantera nätverksfel och timeouts.
User-Agent Spoofing : Efter liknar en vanlig webbläsare för att undvika enkla enkla blockeringar.
Rate limiting : Inkluderar pauser (time.sleep) för att inte överbelasta målservern.

# Hur verktyget fungerar
Programmet skickar en HTTP-förfrågningar mot en måladdress baserat på en ordlista av mappar och filer.
Svarskoder analyseras för att avgöra om resurser existerar eller inte.

# Vad jag lärt mig
- Grundläggande HTTP-statuskod och deras betydelse
- Hur nätverksfel och timouts kan hanteras i Python.
- Vikten av rate limiting för att inte överbelasta en server.
- Hur man strukturerar ett litet projekt och dokumenterar det.

# Begränsningar och framtida förbättringar
Projektet är ett inlärningsprojekt och saknar avancerade funktioner som parallella förfråggningar, autentisering och avancerad rapportering.
Dessa områden är möjliga framtida förbättningar.

# Ansvarsfriskrivning
Verktyget är utvecklat i utbildningsyfte och ska endast användas i kontrollerade labbmiljöer eller på ett system där användaren har uttryckligt tillstånd.



# Bakgrund
Detta projekt skapades som ett självständigt inlärningsprojekt  för att förstå hur webbserver hanterar HTTP-förfrågningar och hur dolda resurser kan identifieras på ett struktuerat sätt.
