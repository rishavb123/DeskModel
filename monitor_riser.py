import bpy

def clear_scene():
    override = bpy.context.copy()
    override["selected_objects"] = list(bpy.context.scene.objects)
    bpy.ops.object.delete(override)

def add_cube(location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), multiplier=0.2):
    location = (location[0] * multiplier, location[1] * multiplier, location[2] * multiplier)
    scale = (scale[0] * multiplier, scale[1] * multiplier, scale[2] * multiplier)
    bpy.ops.mesh.primitive_cube_add(location=location, rotation=rotation, scale=scale)

# total dimensions in inches
w = 24.5
d = 11
h = 6.25

b = 1.01
clear_scene()
# add_cube(location=(0, 0, 0), scale=(w, d, h))

# Outer plates
hw = w/2
add_cube(location=(-hw, 0, h/2), scale=(0.5, d * b, h))
add_cube(location=(hw, 0, h/2), scale=(0.5, d * b, h))

# Large Connecting Plate
zb = 2.5
add_cube(location=(0, 0, zb), scale=(w, d, 0.5))

# Inner vertical plates
zt = 4.5
ht = 3.5
xivp = hw - 4.25
add_cube(location=(-xivp, 0, zt), scale=(0.5, d * b, ht))
add_cube(location=(xivp, 0, zt), scale=(0.5, d * b, ht))

# Top Inner Plate
add_cube(location=(0, 0, 5.625), scale=(15.5, d, 0.75))

# Side Covers
wsc = 3.75
hsc = 3.5
dsc = 0.25
scale_sc = (wsc, dsc, hsc)

xsc = (hw + xivp) / 2
zsc = (h + zb + 0.25) / 2

add_cube(location=(xsc, 0.9 * d / 2, zsc), scale=scale_sc)
add_cube(location=(xsc, -0.9 * d / 2, zsc), scale=scale_sc)

add_cube(location=(-xsc, 0.9 * d / 2, zsc), scale=scale_sc)
add_cube(location=(-xsc, -0.9 * d / 2, zsc), scale=scale_sc)

add_cube(location=(xsc, 0.9 * d / 2 - 5.75, zsc), scale=scale_sc)
add_cube(location=(-xsc, -0.9 * d / 2 + 5.75, zsc), scale=scale_sc)
