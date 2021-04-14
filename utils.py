import bpy

def clear_scene():
    override = bpy.context.copy()
    override["selected_objects"] = list(bpy.context.scene.objects)
    bpy.ops.object.delete(override)

def add_cube(location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), multiplier=0.2):
    location = (location[0] * multiplier, location[1] * multiplier, location[2] * multiplier)
    scale = (scale[0] * multiplier, scale[1] * multiplier, scale[2] * multiplier)
    bpy.ops.mesh.primitive_cube_add(location=location, rotation=rotation, scale=scale)