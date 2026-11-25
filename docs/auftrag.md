# Auftrag

Stand: 2026-11-25

## Ziel

Die Buchse einer USB-Verlängerung soll unter die Schreibtischplatte geschraubt werden. Vorne lässt sich dann ein USB-Stecker einstecken, zum Beispiel das Headset.

Für die Buchse wird ein Käfig konstruiert, der per 3D-Drucker hergestellt wird. Der Käfig nimmt die Buchse auf und hat seitlich Laschen zum Anschrauben.

## Gemessene Maße der Buchse

| Teil | Breite | Länge | Höhe | Bemerkung |
|---|---|---|---|---|
| Kunststoffkörper hinten | 16 mm | 18 mm | 9 mm | quaderförmig |
| Konischer Übergang | 16 mm auf 8 mm | 12 mm | 9 mm (angenommen) | läuft zum Kabel zusammen |
| Kabel | 8 mm | | | Querschnitt unbekannt, als 8 mm breit angenommen |
| Metallteil vorne | 14 mm | 9 mm | 5 mm | steht vorne aus dem Kunststoff heraus |

## Anforderungen

- Konstruktion in einem CAD-Programm, das ein druckbares Modell exportieren kann (STL, STEP).
- Käfig nimmt die Buchse auf, Metallteil ragt nach vorne heraus.
- Seitliche Laschen mit Bohrungen zum Anschrauben unter dem Schreibtisch.
- Im 3D-Drucker ohne Stützmaterial herstellbar (Wunsch aus der Konstruktion, nicht ausdrücklich gefordert).

## Entscheidung zum Werkzeug

CadQuery (Python, parametrisch). Gründe: Das Modell lässt sich per Skript erzeugen, versionieren und mit geänderten Maßen neu exportieren. STEP und STL kommen aus derselben Quelle.

## Projektorganisation

Dediziertes Git-Repository für diese Aufgabe. Auftragsbeschreibung, Konstruktionsüberlegungen und Ergebnisse bleiben darin für spätere Ausbaustufen erhalten.
