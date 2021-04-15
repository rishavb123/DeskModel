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


# Save
save()
