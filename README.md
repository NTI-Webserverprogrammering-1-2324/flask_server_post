# Flask Server: POST 🌐

## Innehållsförteckning
1. [Projektbeskrivning](#projektbeskrivning-)
2. [Appöversikt](#appöversikt-)
3. [HTML-mallar](#html-mallar-)
4. [Hantera formulärinskick](#hantera-formulärinskick-)
5. [Dynamiska ruttåtgärder](#dynamiska-ruttåtgärder-)
6. [Rendera uppgifter](#rendera-uppgifter-)
7. [Uppgiftssökning](#uppgiftssökning-)
8. [Kom igång](#kom-igång-)
9. [Fördjupad förståelse av `app.run()`](#fördjupad-förståelse-av-apprun-)
10. [Ange Portnummer](#ange-portnummer-)
11. [Aktivera Felsökningsläge](#aktivera-felsökningsläge-)
12. [Ange Värd](#ange-värd-)
13. [Avancerade inställningar i `app.run()`](#avancerade-inställningar-i-apprun-)
14. [Threaded Mode](#threaded-mode-)
15. [SSL/TLS Certifikat](#ssltls-certifikat-)
16. [Viktigt att Notera](#viktigt-att-notera-)
    
## Projektbeskrivning

Detta repo introducerar en Flask-server som utnyttjar POST-metoden för att ta emot data från användaren. Tillsammans med GET-metoden, som används för att hämta data, utgör dessa funktioner fundamentet för CRUD-operationerna – Skapa (Create), Läsa (Read), Uppdatera (Update) och Ta bort (Delete) – vilka är centrala för funktionaliteten i server-renderade webbapplikationer. Servern hanterar dessa operationer genom att tillhandahålla särskilda ändpunkter för att lägga till, hämta, uppdatera och ta bort objekt.

## Appöversikt

 I den här serverapplikationen undersöker vi hur dessa operationer kan integreras med Flask-rutter och olika HTTP-metoder för att skapa en fungerande TODO-listapplikation.

### HTML-mallar 📄

- `GET /`: Renderar `index.html`, applikationens huvudsida.
- `GET /page`: Renderar `page.html`, visar ytterligare information eller funktioner.

### Hantera formulärinskick ✉️

- `POST /add_task`: Tar emot data från ett formulär och lägger till en ny uppgift. Användaren omdirigeras sedan till `todo`-vyn.

### Dynamiska ruttåtgärder 🔄

- `POST /edit_task/<task_id>`: Uppdaterar en specifik uppgift baserat på dess ID.
- `POST /delete_task/<task_id>`: Raderar en specifik uppgift.

### Rendera uppgifter 📜

- `GET /todo`: Visar alla uppgifter som lagras på servern.

### Uppgiftssökning 🔎

- `POST /search_task`: Söker efter uppgifter med ett specifikt ID och omdirigerar till detaljvyn.
- `GET /view_task/<task_id>`: Visar detaljer för en enskild uppgift.

## Kom igång 🚀

För att snabbt komma igång med din Flask-applikation, följ dessa enkla steg:

1. **Installera Flask**: Använd kommandot `pip install flask` för att installera Flask i din miljö.
2. **Starta servern**: Navigera till din projektmappe och utför `flask run` för att sätta igång servern.
3. **Utforska applikationen**: Besök `http://127.0.0.1:5000` i din webbläsare för att utforska din applikations gränssnitt och funktioner.

När du har din grundläggande Flask-server uppe och kör, är det dags att utforska några av de inställningar som kan optimeras för att förbättra din applikations prestanda och säkerhet.

---

## Fördjupad förståelse av `app.run()` 🎛️

`app.run()` är kommandot som får din Flask-server att starta. Men det finns mycket mer att förstå om denna kraftfulla funktion. Genom att anpassa inställningarna kan du förbättra utvecklingsupplevelsen och förbereda din applikation för en säker och effektiv produktionssättning.

### Ange Portnummer 🚪

Flask använder som standard port `5000`, men detta är fullt konfigurerbart. Genom att använda argumentet `port` kan du specificera en annan port för din server. Så, om du föredrar att använda port `6000`, skulle du starta din server med `app.run(port=6000)`.

### Aktivera Felsökningsläge 🔍

Att ha felsökningsläget aktiverat är ovärderligt under utveckling, då det ger utförliga felrapporter direkt i webbläsaren. Du aktiverar detta läge genom att sätta `debug=True` när du kör `app.run()`. Dock, av säkerhetsskäl, se till att avaktivera detta läge när din applikation går live i en produktionsmiljö.

### Ange Värd 🌐

Med `host`-argumentet kan du bestämma vilka nätverksgränssnitt som din server ska lyssna på. För att servern ska kunna nås utanför din egen maskin, ange `app.run(host='0.0.0.0')`. Tänk på att detta kan öppna upp för säkerhetsrisker, så använd det med omsorg.

## Avancerade inställningar i `app.run()` 🎛️

### Threaded Mode 💻

För applikationer som hanterar flera förfrågningar parallellt, kan det vara fördelaktigt att aktivera threaded mode genom att ställa in `threaded=True`. Detta låter Flask hantera förfrågningar i separata trådar, vilket kan förbättra prestanda avsevärt.

### SSL/TLS Certifikat 🔐

Under utveckling kan du köra din applikation över HTTPS genom att använda ett självsignerat certifikat med `ssl_context='adhoc'`. För produktionsanvändning krävs ett certifikat från en certifieringsmyndighet, vilket du kan konfigurera genom att ange sökvägarna till ditt certifikat och din privata nyckel i `ssl_context`.

### Viktigt att Notera 📝

Kom ihåg att `app.run()` är avsedd för utveckling och testning. När du är redo för produktion bör du använda en mer robust serverlösning som Gunicorn eller en ASGI-server. Vi kommer att utforska dessa alternativ och deras fördelar senare i kursen.

---

> _**Om du har några frågor eller behöver ytterligare förtydliganden, tveka inte att fråga.  
KaahinAtNTI**_
