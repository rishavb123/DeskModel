import bpy
import numpy as np
import os

MULTIPLIER = 0.2

def clear_scene():
    override = bpy.context.copy()
    override["selected_objects"] = list(bpy.context.scene.objects)
    bpy.ops.object.delete(override)

def add_cube(location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), multiplier=MULTIPLIER, n=None):
    location = (location[0] * multiplier, location[1] * multiplier, location[2] * multiplier)
    scale = (scale[0] * multiplier, scale[1] * multiplier, scale[2] * multiplier)
    bpy.ops.mesh.primitive_cube_add(location=location, rotation=rotation, scale=scale)
    if n is not None:
        name(n)

def add_cylinder(location=(0, 0, 0), rotation=(0, 0, 0), radius=0, height=0, multiplier=MULTIPLIER, n=None):
    location = (location[0] * multiplier, location[1] * multiplier, location[2] * multiplier)
    radius *= multiplier
    height *= multiplier
    bpy.ops.mesh.primitive_cylinder_add(location=location, rotation=rotation, radius=radius, depth=height)
    if n is not None:
        name(n)

def name(n):
    bpy.context.object.name = n

def group(g):
    bpy.context.object.group_link(group=g)

def save():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    bpy.ops.wm.save_as_mainfile(filepath=dir_path + "\\raw_models\\"  + ".".join(os.path.basename(__file__).split(".")[:-1]) + ".blend")

# total dimensions in inches
w = 24.5
d = 11
h = 6.25

b = 1.01
clear_scene()

# Outer plates
hw = w/2
add_cube(location=(-hw, 0, h/2), scale=(0.5, d * b, h), n="Outer Plane L")
add_cube(location=(hw, 0, h/2), scale=(0.5, d * b, h), n="Outer Plane R")

# Large Connecting Plate
zb = 2.5
add_cube(location=(0, 0, zb), scale=(w, d, 0.5), n="Bottom Plane")

# Inner vertical plates
zt = 4.5
ht = 3.5
xivp = hw - 4.25
add_cube(location=(-xivp, 0, zt), scale=(0.5, d * b, ht), n="Inner Vertical L")
add_cube(location=(xivp, 0, zt), scale=(0.5, d * b, ht), n="Inner Vertical R")

# Top Inner Plate
add_cube(location=(0, 0, 5.625), scale=(15.5, d, 0.75), n="Top Plane")

# Side Covers
wsc = 3.75
hsc = 3.5
dsc = 0.25
scale_sc = (wsc, dsc, hsc)

xsc = (hw + xivp) / 2
zsc = (h + zb + 0.25) / 2

add_cube(location=(xsc, 0.9 * d / 2, zsc), scale=scale_sc, n="Side Cover 1")
add_cube(location=(xsc, -0.9 * d / 2, zsc), scale=scale_sc, n="Side Cover 2")

add_cube(location=(-xsc, 0.9 * d / 2, zsc), scale=scale_sc, n="Side Cover 3")
add_cube(location=(-xsc, -0.9 * d / 2, zsc), scale=scale_sc, n="Side Cover 4")

add_cube(location=(xsc, 0.9 * d / 2 - 5.75, zsc), scale=scale_sc, n="Side Cover 5")
add_cube(location=(-xsc, -0.9 * d / 2 + 5.75, zsc), scale=scale_sc, n="Side Cover 6")


# Monitor Arms Cylinder
cylinder_h = 16
cylinder_r = 0.590551
add_cylinder(location=(0, 3.5, 6 + cylinder_h / 2), radius=cylinder_r, height=cylinder_h, n="Monitor Arm Base")

# Monitor Arms
# add_cube(location=(3 + cylinder_r / 2, 3.5, 18), scale=(6 + cylinder_r, 0.75, 1.25), n="Monitor Arm R1")
# add_cube(location=(9.5 + cylinder_r, 3.5, 18), scale=(7, 0.75, 1.25), n="Monitor Arm R2")
# add_cube(location=(14 + cylinder_r, 3.5, 18), scale=(2, 0.75, 1.25), n="Monitor Arm R3")
# add_cube(location=(15 + cylinder_r, 3.5, 18), scale=(0.1, 4.5, 4.5), n="Monitor Arm Plate R")

# add_cube(location=(-3 - cylinder_r / 2, 3.5, 18), scale=(6 + cylinder_r, 0.75, 1.25), n="Monitor Arm R1")
# add_cube(location=(-9.5 - cylinder_r, 3.5, 18), scale=(7, 0.75, 1.25), n="Monitor Arm R2")
# add_cube(location=(-14 - cylinder_r, 3.5, 18), scale=(2, 0.75, 1.25), n="Monitor Arm R3")
# add_cube(location=(-15 - cylinder_r, 3.5, 18), scale=(0.1, 4.5, 4.5), n="Monitor Arm Plate R")

y = 3.5
z = 18

L1 = 6 + cylinder_r
L2 = 7
L3 = 2
L4 = 4.5

JR = 0.75/2 * 1.5
arm_height = 1.25

sin = lambda x: np.sin(x)
cos = lambda x: np.cos(x)
flipx = lambda tup: (-tup[0], tup[1], tup[2])
flipz = lambda tup: (tup[0], tup[1], -tup[2])

# Right Arm

# Defaults
# theta = 0
# phi = 90
# alpha = 180

theta = 45
phi = 45
alpha = 90

theta = np.radians(theta)
phi = np.radians(phi)
alpha = np.radians(alpha)

P1 = (L1/2 * cos(theta), y + L1/2 * sin(theta), z)
R1 = (0, 0, theta)
add_cube(location=P1, rotation=R1, scale=(L1, 0.75, arm_height), n="Monitor Arm R1")

P2 = (L1 * cos(theta) + L2/2 * sin(phi), y + L1 * sin(theta) - L2/2 * cos(phi), z)
R2 = (0, 0, phi - np.pi/2)
add_cube(location=P2, rotation=R2, scale=(L2, 0.75, arm_height), n="Monitor Arm R2")

P3 = (L1 * cos(theta) + L2 * sin(phi) - L3/2 * cos(alpha), y + L1 * sin(theta) - L2 * cos(phi) - L3/2 * sin(alpha), z)
R3 = (0, 0, alpha)
add_cube(location=P3, rotation=R3, scale=(L3, 0.75, arm_height), n="Monitor Arm R3")

P4 = (L1 * cos(theta) + L2 * sin(phi) - L3 * cos(alpha), y + L1 * sin(theta) - L2 * cos(phi) - L3 * sin(alpha), z)
R4 = R3
add_cube(location=P4, rotation=R4, scale=(0.1, L4, L4), n="Monitor Arm R4")

J1 = (L1 * cos(theta), y + L1 * sin(theta), z)
add_cylinder(location=J1, radius=JR, height=arm_height * 1.1, n="Monitor Arm RJ1")

J2 = (L1 * cos(theta) + L2 * sin(phi), y + L1 * sin(theta) - L2 * cos(phi), z)
add_cylinder(location=J2, radius=JR, height=arm_height * 1.1, n="Monitor Arm RJ2")

# Left Arm

# Defaults
# theta = 0
# phi = 90
# alpha = 180

theta = 45
phi = 45
alpha = 90

theta = np.radians(theta)
phi = np.radians(phi)
alpha = np.radians(alpha)

P1 = (L1/2 * cos(theta), y + L1/2 * sin(theta), z)
R1 = (0, 0, theta)
add_cube(location=flipx(P1), rotation=flipz(R1), scale=(L1, 0.75, arm_height), n="Monitor Arm L1")

P2 = (L1 * cos(theta) + L2/2 * sin(phi), y + L1 * sin(theta) - L2/2 * cos(phi), z)
R2 = (0, 0, phi - np.pi/2)
add_cube(location=flipx(P2), rotation=flipz(R2), scale=(L2, 0.75, arm_height), n="Monitor Arm L2")

P3 = (L1 * cos(theta) + L2 * sin(phi) - L3/2 * cos(alpha), y + L1 * sin(theta) - L2 * cos(phi) - L3/2 * sin(alpha), z)
R3 = (0, 0, alpha)
add_cube(location=flipx(P3), rotation=flipz(R3), scale=(L3, 0.75, arm_height), n="Monitor Arm L3")

P4 = (L1 * cos(theta) + L2 * sin(phi) - L3 * cos(alpha), y + L1 * sin(theta) - L2 * cos(phi) - L3 * sin(alpha), z)
R4 = R3
add_cube(location=flipx(P4), rotation=flipz(R4), scale=(0.1, L4, L4), n="Monitor Arm L4")

J1 = (L1 * cos(theta), y + L1 * sin(theta), z)
add_cylinder(location=flipx(J1), radius=JR, height=arm_height * 1.1, n="Monitor Arm LJ1")

J2 = (L1 * cos(theta) + L2 * sin(phi), y + L1 * sin(theta) - L2 * cos(phi), z)
add_cylinder(location=flipx(J2), radius=JR, height=arm_height * 1.1, n="Monitor Arm LJ2")


# Save
save()
