# Einstieg in FreeCAD: Den Halter nachbauen

Diese Anleitung baut den Halter in FreeCAD (Arbeitsbereich Part Design) von Hand nach. Als Vorlage dienen die Maße aus `docs/auftrag.md` und die Koordinaten aus dem Skript `src/usb_cage.py`. Am Ende vergleichst Du Dein Modell mit `models/usb_halter.step`.

Hinweis: Die Anleitung ist für FreeCAD 1.0 geschrieben, aber nicht in FreeCAD durchgespielt. Menünamen und Schaltflächen können in anderen Versionen leicht abweichen. Wenn ein Schritt nicht aufgeht, hilft meistens der Schalter "Umkehren" (Reversed) im Dialog des jeweiligen Features.

## Das Modell vorab ansehen

1. FreeCAD starten, Datei → Öffnen, `models/usb_halter.step` wählen.
2. Mit der Maus drehen, mit dem Rad zoomen. Mit Ansicht → Standardansichten lassen sich Ober- und Unterseite prüfen.
3. Messen: Werkzeuge → Messen (Measure) oder Part → Messen. Du solltest 45,1 x 38,2 x 11,6 mm als Außenmaße finden.

Das ist der Zielzustand, den Du gleich selbst aufbaust.

## Koordinaten und Ausrichtung

- X ist die Breite, Y die Länge (Y=0 vorne, das Kabel geht nach +Y raus), Z die Höhe.
- Z=0 ist die Tischseite. Dort liegt auch das Druckbett.
- Alle Maße in Millimetern. Wähle unter Bearbeiten → Einstellungen → Allgemein → Einheiten das Standardsystem "Standard (mm/kg/s/Grad)".

Die Skizzen liegen auf der XY-Ebene, die Z-Richtung kommt aus Pad und Pocket.

## Schritt 1: Körper anlegen

1. Arbeitsbereich Part Design wählen.
2. Neuer Körper (Create body). Er erscheint im Baum als "Body".

## Schritt 2: Außenkontur als Pad

1. Körper markieren, Neue Skizze (Create sketch), Ebene XY_Plane wählen.
2. Ein Polygonzug (Polyline) mit diesen acht Punkten zeichnen und schließen:

| Punkt | X | Y |
|---|---|---|
| 1 | -10,55 | -2,4 |
| 2 | 10,55 | -2,4 |
| 3 | 10,55 | 18,776 |
| 4 | 6,7 | 30,776 |
| 5 | 6,7 | 35,8 |
| 6 | -6,7 | 35,8 |
| 7 | -6,7 | 30,776 |
| 8 | -10,55 | 18,776 |

3. Die Punkte fixierst Du am einfachsten, indem Du jeden Punkt anklickst und eine Koordinatenbedingung setzt (Sketcher → Bedingungen → Horizontalen/Vertikalen Abstand zum Ursprung). Die Skizze ist fertig, wenn sie vollständig bestimmt ist und die Linien grün werden.
4. Skizze schließen, Pad (Extrusion) mit Länge 11,6 mm. Die Richtung muss nach +Z zeigen.

## Schritt 3: Hohlraum und Kabelkanal als Pocket

1. Neue Skizze auf der XY-Ebene, wieder ein geschlossener Polygonzug. Der Hohlraum ist 0,1 mm länger als der Körper nötig hätte, und der Kabelkanal ist gleich dabei, weil der schmale Hals die Hinterwand durchstößt.

| Punkt | X | Y |
|---|---|---|
| 1 | -8,15 | 0 |
| 2 | 8,15 | 0 |
| 3 | 8,15 | 18,4 |
| 4 | 4,3 | 30,4 |
| 5 | 4,3 | 36 |
| 6 | -4,3 | 36 |
| 7 | -4,3 | 30,4 |
| 8 | -8,15 | 18,4 |

2. Skizze schließen, Pocket mit Länge 9,2 mm. Die Pocket schneidet standardmäßig gegen die Skizzennormale, also von der XY-Ebene nach -Z, und würde ins Leere schneiden. Schalte "Umkehren" ein, bis die Vorschau den Hohlraum im Körper zeigt.

Die Y-Koordinate 36 im Hals liegt bewusst hinter der Außenwand bei 35,8. Dadurch wird die Endwand sauber durchtrennt.

## Schritt 4: Schlitz in der Vorderwand für das Metallteil

1. Neue Skizze auf der XZ_Plane (sie liegt bei Y=0, also genau an der Vorderkante des Hohlraums). In dieser Ebene ist die Skizzen-X-Achse die globale X-Achse und die Skizzen-Y-Achse die globale Z-Achse.
2. Rechteck von (-7,2 | 0) bis (7,2 | 7,3). Breite 14,4 mm, Höhe 7,3 mm.
3. Pocket mit Länge 3 mm, Richtung nach -Y (in die Vorderwand hinein, die von Y=-2,4 bis Y=0 reicht). Bei falscher Richtung wieder "Umkehren".

Die Höhe 7,3 mm kommt aus der Mitte des Hohlraums (4,6) plus die halbe Höhe des Metallteils (2,5) plus 0,2 mm Luft.

## Schritt 5: Lasche

1. Neue Skizze auf der XY-Ebene, Rechteck von (9,35 | 2,2) bis (22,55 | 16,2). Die Lasche beginnt in der Seitenwand und ragt 12 mm nach außen.
2. Pad mit 3,5 mm nach +Z.
3. Die beiden äußeren senkrechten Kanten (die bei X=22,55) mit Verrundung (Fillet) von 5 mm versehen.

## Schritt 6: Bohrung mit Senkung

1. Neue Skizze, Ebene XY_Plane mit Versatz in Z von 3,5 mm (im Fenster der Skizzenplatzierung unter "Attachment Offset" den Z-Wert eintragen) oder direkt die Oberseite der Lasche wählen.
2. Einen Kreis mit Mittelpunkt (17,05 | 9,2) zeichnen. Der Durchmesser ist hier egal, die Bohrung bestimmt ihn.
3. Part Design → Bohrung (Hole). Durchmesser 4,2 mm, Tiefe "Durch alles" (Through all), Senkung als Kegelsenkung (Countersink) mit Durchmesser 8,4 mm und Winkel 90°.
4. Wenn die Senkung unten statt oben sitzt, Richtung der Bohrung umkehren. Sie muss auf der Seite weg vom Tisch liegen, also bei Z=3,5.

## Schritt 7: Zweite Seite spiegeln

1. Pad der Lasche, Verrundung und Bohrung im Baum zusammen markieren.
2. Part Design → Spiegeln (Mirrored), Spiegelebene YZ_Plane.

Damit sind beide Laschen da. Das Modell ist fertig.

## Schritt 8: Mit meiner Version vergleichen

1. Datei → Importieren, `models/usb_halter.step` zusätzlich in dasselbe Dokument laden.
2. Wechsle in den Arbeitsbereich Part. Wähle zuerst Dein Modell, dann den Import und führe Part → Boolesche Operationen → Differenz (Cut) aus.
3. Wenn alles passt, bleibt kein Körper übrig, oder nur kleine Splitter im Bereich der Rundungen. Vertausche die Reihenfolge und wiederhole den Test, um auch Material zu sehen, das bei Dir fehlt.

Abweichungen zeigen Dir, welche Schritte Du noch einmal nachrechnen solltest.

## Schritt 9: Für den Druck exportieren

1. Den Körper im Baum markieren.
2. Datei → Exportieren, Dateityp "STL Mesh" wählen, Datei `usb_halter.stl` benennen.
3. Im Slicer so lassen, wie die Datei geliefert wird: Laschen flach auf dem Bett, offene Seite nach unten.

## Danach

- **Parameter benennen:** Im Arbeitsbereich Spreadsheet (Tabelle) lassen sich Werte wie Wandstärke oder Luft als benannte Zellen anlegen. In Skizzen und Features verweist Du dann mit `Spreadsheet.Wand` auf den Wert. Das entspricht dem Parameterblock oben in `src/usb_cage.py`.
- **Python-Konsole:** Über Ansicht → Bereiche → Python-Konsole siehst Du, welche Befehle FreeCAD hinter jedem Klick ausführt. Das ist der Weg zum Skript.
- **Änderungen festhalten:** Wenn Du in FreeCAD Anpassungen am Halter machst, speichere sie als eigene Datei in `models/` und trage sie im Änderungsprotokoll von `docs/konstruktion.md` ein. Das Skript bleibt die Quelle für die Standardvariante.
