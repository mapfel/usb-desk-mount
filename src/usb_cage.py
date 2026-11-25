"""Parametrischer Halter (Käfig) für eine USB-Buchse zur Montage unter einer Tischplatte.

Koordinaten (alle Maße in mm):
  X = Breite, Y = Länge (Y=0 ist die Vorderseite, Kabel geht nach +Y raus),
  Z = Höhe (Z=0 ist die Auflagefläche an der Tischplatte = Druckbett).
Die Seite zur Tischplatte ist offen. Die Tischplatte schließt den Käfig also von oben und
hält die Buchse. Gedruckt wird in genau dieser Lage: Laschen flach auf dem Bett, keine Stützen.
"""
import os
import sys
import cadquery as cq

# ---------------- gemessene Maße der Buchse ----------------
BODY_W, BODY_L, BODY_H = 16.0, 18.0, 9.0      # Kunststoffteil hinten
TAPER_L = 12.0                                 # konischer Übergang zum Kabel
CABLE_W = 8.0                                  # Kabelbreite
SHELL_W, SHELL_L, SHELL_H = 14.0, 9.0, 5.0     # Metallteil vorne
SHELL_Z_OFFSET = 0.0                           # Metallteil mittig in der Höhe (+ = weg vom Tisch)

# ---------------- Toleranzen / Konstruktion ----------------
CLR_SIDE = 0.15        # Luft je Seite um den Kunststoffkörper
CLR_H = 0.2            # Luft in der Höhe
CLR_LEN = 0.3          # Luft in der Länge
CLR_SHELL = 0.2        # Luft je Seite um das Metallteil
CLR_CABLE = 0.3        # Luft je Seite um das Kabel
WALL = 2.4             # Wandstärke (6 Linien bei 0,4er Düse)
FLOOR = 2.4            # Boden (Seite weg vom Tisch)
NECK_L = 3.0           # gerader Kabelkanal am Ende

TAB_T = 3.5            # Dicke der Laschen
TAB_LEN = 12.0         # Überstand der Laschen seitlich der Außenwand
TAB_WIDTH = 14.0       # Breite der Laschen in Y-Richtung
SCREW_D = 4.2          # Bohrung (für Schrauben bis 4 mm)
HEAD_D = 8.4           # Senkung für Senk- oder Linsenkopf
TAB_FILLET = 5.0

# ---------------- abgeleitete Größen ----------------
w = BODY_W + 2 * CLR_SIDE
cw = CABLE_W + 2 * CLR_CABLE
dc = BODY_H + CLR_H                    # Tiefe des Hohlraums
L = BODY_L + 0.1 + CLR_LEN             # gerader Teil des Hohlraums
H = dc + FLOOR

y_taper_end = L + TAPER_L
y_end = y_taper_end + NECK_L

cav_pts = [
    (-w / 2, 0), (w / 2, 0), (w / 2, L), (cw / 2, y_taper_end),
    (cw / 2, y_end), (-cw / 2, y_end), (-cw / 2, y_taper_end), (-w / 2, L),
]

outer = cq.Workplane("XY").polyline(cav_pts).close().offset2D(WALL, "intersection").extrude(H)
cavity = (cq.Workplane("XY").workplane(offset=-0.1).polyline(cav_pts).close().extrude(dc + 0.1))
body = outer.cut(cavity)

# Kabelkanal durch die Endwand (zur Tischseite offen)
cable_slot = cq.Workplane("XY").box(cw, WALL + 1.0, dc + 0.1, centered=(True, False, False)) \
    .translate((0, y_end - 0.1, -0.1))
body = body.cut(cable_slot)

# Schlitz in der Vorderwand für das Metallteil (zur Tischseite offen)
shell_w_slot = SHELL_W + 2 * CLR_SHELL
shell_top = dc / 2 + SHELL_Z_OFFSET + SHELL_H / 2 + CLR_SHELL
front_slot = cq.Workplane("XY").box(shell_w_slot, WALL + 1.0, shell_top + 0.1, centered=(True, False, False)) \
    .translate((0, -WALL - 0.5, -0.1))
body = body.cut(front_slot)

# Laschen links und rechts, mittig am geraden Teil
cy = L / 2
for side in (-1, 1):
    x_in = side * (w / 2 + WALL / 2)
    x_out = side * (w / 2 + WALL + TAB_LEN)
    cx = (x_in + x_out) / 2
    tab = cq.Workplane("XY").box(abs(x_out - x_in), TAB_WIDTH, TAB_T, centered=(True, True, False)).translate((cx, cy, 0))
    tab = tab.edges("|Z").edges(">X" if side > 0 else "<X").fillet(TAB_FILLET)
    body = body.union(tab)

    hx = side * (w / 2 + WALL + TAB_LEN / 2 + 0.5)
    hole = cq.Workplane("XY").workplane(offset=-0.1).center(hx, cy).circle(SCREW_D / 2).extrude(TAB_T + 0.2)
    csk_h = (HEAD_D - SCREW_D) / 2
    cone = cq.Workplane("XY").add(cq.Solid.makeCone(
        SCREW_D / 2, HEAD_D / 2 + 0.05, csk_h + 0.05,
        pnt=cq.Vector(hx, cy, TAB_T - csk_h), dir=cq.Vector(0, 0, 1)))
    body = body.cut(hole).cut(cone)

result = body

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "models")
    os.makedirs(out, exist_ok=True)
    cq.exporters.export(result, f"{out}/usb_halter.step")
    cq.exporters.export(result, f"{out}/usb_halter.stl", tolerance=0.01, angularTolerance=0.1)
    bb = result.val().BoundingBox()
    print(f"Maße: {bb.xlen:.1f} x {bb.ylen:.1f} x {bb.zlen:.1f} mm, Volumen {result.val().Volume()/1000:.2f} cm3")
