# 📅 BVB Heimspiel-Kalender (ICS)

## Idee

Ein automatisiert gepflegter Kalender im **ICS-Format**, der alle
**Heimspiele von Borussia Dortmund** enthält.\
Der Kalender wird über eine feste URL bereitgestellt und automatisch
aktualisiert.\
So kann man ihn in **Google Kalender** oder jede andere Kalender-App
abonnieren.

------------------------------------------------------------------------

## Datenquelle

-   Spiele werden über die **[API-Football
    (API-Sports)](https://www.api-football.com/documentation-v3)**
    abgerufen.\
-   Liga: Bundesliga (league id = `78`)\
-   Saison: aktuelle Saison (z. B. `2025`)\
-   Team: Borussia Dortmund (team id = `165`)


------------------------------------------------------------------------

## Anforderungen

1.  **Filterung**
    -   Es sollen nur **Heimspiele des BVB** in den Kalender geschrieben
        werden.
2.  **ICS-Datei**
    -   Standardformat [RFC
        5545](https://datatracker.ietf.org/doc/html/rfc5545).\
    -   Jeder Termin enthält:
        -   Titel: `BVB vs Gegner`\
        -   Datum/Uhrzeit (aus API)\
        -   Dauer ca. 2 Stunden\
        -   Ort: *Signal Iduna Park, Dortmund*\
        -   Beschreibung: Wettbewerb / Spieltag
3.  **Automatische Aktualisierung**
    -   Script läuft regelmäßig (alle 6 Stunden).\
    -   ICS-Datei wird neu erzeugt und ins Repo geschrieben.
4.  **Hosting**
    -   GitHub Pages hostet die `.ics`-Datei im Ordner `docs/`.\

    -   Ergebnis: öffentliche URL, z. B.:

            https://<username>.github.io/bvb-kalender/bvb_heimspiele.ics
5.  **Integration**
    -   Nutzer kann diese URL in Google Kalender → *Kalender hinzufügen
        → per URL* einfügen.\
    -   Google synchronisiert automatisch alle paar Stunden.

------------------------------------------------------------------------

## Umsetzungsschritte

1.  **Repository einrichten** - schon erledigt
    -   Neues Repo bei GitHub (`bvb-kalender`).\
    -   Dateien:
        -   `generate_calendar.py` (Script)\
        -   `requirements.txt` (Dependencies)\
        -   `.github/workflows/update.yml` (GitHub Actions Workflow)\
        -   `docs/` (Ordner für die ICS-Datei)
2.  **Python-Script**
    -   Ruft API-Football ab:

        ``` http
        GET https://v3.football.api-sports.io/fixtures?team=165&season=2025&league=78
        ```

    -   Filtert nur Heimspiele.\

    -   Schreibt `docs/bvb_heimspiele.ics`.
3.  **GitHub Actions Workflow**
    -   Läuft alle 6h.\
    -   Führt Script aus.\
    -   Committet aktualisierte ICS-Datei.
4.  **GitHub Pages aktivieren**
    -   Branch `main`, Ordner `docs/`.\
    -   URL für Google Kalender freigeben.

------------------------------------------------------------------------

## Deliverables

-   `generate_calendar.py`\
-   `requirements.txt`\
-   `.github/workflows/update.yml`\
-   `docs/bvb_heimspiele.ics` (automatisch generiert)\
-   `README.md` (dieses Dokument)

------------------------------------------------------------------------

Aufgabe für einen KI-Agenten

- Quelle = API-Football\
- Output = ICS-Datei mit Heimspielen des BVB\
- Automatisierung = GitHub Actions\
- Bereitstellung = GitHub Pages
