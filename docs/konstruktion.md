# Konstruktionsnotizen

## Koordinatensystem

- X = Breite, Y = Länge (Y=0 vorne, das Kabel geht nach +Y raus), Z = Höhe.
- Z=0 ist die Auflagefläche an der Tischplatte und zugleich das Druckbett.
- Alle Maße in Millimetern.

## Grundidee

Der Käfig ist zur Tischseite offen. Die Buchse wird von dort eingelegt. Die Tischplatte schließt den Käfig beim Anschrauben und hält die Buchse in Z-Richtung. Eine zweite Teilschale oder Schnapphaken sind damit unnötig.

Die Buchse wird in den übrigen Richtungen formschlüssig gehalten:
- Nach vorne (Stecker ziehen): Die Vorderwand hat nur einen Schlitz für das Metallteil. Der breitere Kunststoffkörper stößt an die Wand, links und rechts bleiben rund 0,95 mm Steg.
- Nach hinten (Stecker stecken): Die konisch zulaufenden Rückwände fangen den Körper ab.
- Seitlich: Die Wände liegen mit 0,15 mm Luft an.

## Aufbau des Modells

1. Hohlraum als Polygon (gerader Teil, Konus, gerader Kabelhals).
2. Außenkontur als Offset dieses Polygons um die Wandstärke (`offset2D`, Eckenart `intersection`), auf Gesamthöhe extrudiert.
3. Hohlraum abgezogen, nach Z=0 hin offen.
4. Kabelkanal durch die Endwand, Schlitz für das Metallteil in der Vorderwand, beide zur Tischseite offen.
5. Zwei Laschen links und rechts auf Höhe des geraden Teils, außen mit Radius 5 mm gerundet.
6. Je Lasche eine Bohrung mit Senkung. Die Senkung liegt auf der Seite, an der später der Schraubenkopf sitzt.

## Parameter (Standardwerte im Skript)

| Parameter | Wert | Zweck |
|---|---|---|
| `CLR_SIDE` | 0,15 mm | Luft je Seite um den Kunststoffkörper |
| `CLR_H` | 0,2 mm | Luft in der Höhe |
| `CLR_LEN` | 0,3 mm | Luft in der Länge |
| `CLR_SHELL` | 0,2 mm | Luft je Seite um das Metallteil |
| `CLR_CABLE` | 0,3 mm | Luft je Seite um das Kabel |
| `WALL` / `FLOOR` | 2,4 mm | Wand- und Bodenstärke (6 Linien bei 0,4er Düse) |
| `TAB_T` | 3,5 mm | Laschendicke |
| `TAB_LEN` | 12 mm | Überstand der Laschen |
| `SCREW_D` / `HEAD_D` | 4,2 / 8,4 mm | Bohrung und Senkung |
| `SHELL_Z_OFFSET` | 0 mm | Höhenlage des Metallteils im Körper |

Ergebnis: Außenmaße 45,1 x 38,2 x 11,6 mm, Volumen 4,48 cm³.

## Druckausrichtung

Gedruckt wird in der exportierten Lage: Laschen flach auf dem Bett, offene Seite nach unten. Der Boden des Käfigs entsteht als Brücke über 16,3 mm, der Schlitz in der Vorderwand als Brücke über 14,6 mm. Die Senkung der Laschen öffnet sich nach oben. Stützmaterial ist nicht nötig.

## Prüfungen

`src/check_fit.py` baut eine Attrappe der Buchse in Sollmaßen und schneidet sie mit dem Halter. Ergebnis: Kollisionsvolumen 0 mm³. Das STL-Mesh ist wasserdicht.

## Annahmen, die noch nicht am echten Teil geprüft sind

1. Das Metallteil sitzt mittig in der Höhe des Kunststoffkörpers.
2. Der Konus verjüngt sich nur in der Breite, die Höhe bleibt bei 9 mm.
3. Das Kabel hat 8 mm Breite und passt in den Kanal von 8,6 mm.
4. Die Messwerte stammen von Hand (Schieblehre oder Lineal) und können um einige Zehntel abweichen.

## Mögliche Ausbaustufen

- Passprobe: nur die vordersten 8 mm des Halters drucken, um Schlitz und Körperbreite zu testen.
- Konus auch in der Höhe abbilden, falls das echte Teil dort schmaler wird.
- Zugentlastung für das Kabel am Halterende.
- Variante mit zwei Buchsen nebeneinander (zum Beispiel USB-A und USB-C).
- Rastnasen als Alternative zur Tischplatte als Deckel, falls der Halter auch außerhalb des Schreibtischs montiert werden soll.
- Schraubenlöcher als Langlöcher, falls der Abstand zur Tischkante variieren soll.

## Änderungsprotokoll

- 2026-11-25: Erste Version. Halter mit offener Tischseite, Schlitz vorne, Kabelkanal hinten, zwei Laschen.
