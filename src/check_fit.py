import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cadquery as cq, trimesh
import usb_cage as u

# Attrappe der Buchse in Sollmaßen, vorne bei Y=0.1, mittig in der Höhe
y0 = 0.1
zc = u.dc / 2
body = cq.Workplane("XY").box(u.BODY_W, u.BODY_L, u.BODY_H, centered=(True, False, True)).translate((0, y0, zc))
pts = [(-u.BODY_W/2, 0), (u.BODY_W/2, 0), (u.CABLE_W/2, u.TAPER_L), (-u.CABLE_W/2, u.TAPER_L)]
taper = cq.Workplane("XY").workplane(offset=zc - u.BODY_H/2).polyline(pts).close().extrude(u.BODY_H).translate((0, y0 + u.BODY_L, 0))
shell = cq.Workplane("XY").box(u.SHELL_W, u.SHELL_L, u.SHELL_H, centered=(True, False, True)).translate((0, y0 - u.SHELL_L, zc))
cable = cq.Workplane("XY").box(u.CABLE_W, 20, u.CABLE_W, centered=(True, False, True)).translate((0, y0 + u.BODY_L + u.TAPER_L, zc))
dummy = body.union(taper).union(shell).union(cable)

inter = u.result.intersect(dummy)
v = inter.val().Volume() if inter.vals() else 0.0
print(f"Kollision Attrappe/Halter: {v:.3f} mm3 (0 = passt)")

m = trimesh.load(os.path.join(HERE, '..', 'models', 'usb_halter.stl'))
print("watertight:", m.is_watertight, "| Volumen cm3:", round(m.volume/1000, 2), "| Bounds:", m.bounds.round(1).tolist())
