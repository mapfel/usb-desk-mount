# Projektkontext für Claude

Dieses Repository enthält die Konstruktion eines 3D-druckbaren Halters für eine USB-Buchse (Montage unter dem Schreibtisch).

## Zuerst lesen

1. `docs/auftrag.md` für Aufgabe, Maße und Anforderungen.
2. `docs/konstruktion.md` für Entscheidungen, Annahmen und offene Ausbaustufen.

## Arbeitsweise

- Das Modell entsteht ausschließlich in `src/usb_cage.py` (CadQuery). STL und STEP in `models/` werden daraus erzeugt und nicht von Hand bearbeitet.
- Alle Maße in Millimetern. Z=0 ist die Tischseite und zugleich das Druckbett, Y=0 die Vorderseite.
- Nach jeder Änderung `python src/usb_cage.py` und `python src/check_fit.py` ausführen. Kollisionsvolumen muss 0 sein, das Mesh wasserdicht.
- Neue Erkenntnisse und Änderungen im Änderungsprotokoll von `docs/konstruktion.md` festhalten.
- Antworten auf Deutsch, sachlich und ohne Floskeln.
