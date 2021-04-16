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

clear_scene()

add_cube(scale=(16, 10, 1))

save()