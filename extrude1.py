

import bpy
import bmesh
import random
import math

bm = bmesh.new()
bmesh.ops.create_icosphere(bm, subdivisions = 4, diameter = 1)
mesh = bpy.data.meshes.new('_mesh')
bm.to_mesh(mesh)
obj = bpy.data.objects.new('_mesh', mesh)
bpy.context.collection.objects.link(obj)
bpy.data.objects['_mesh'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['_mesh']
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.mesh.select_mode(type = 'FACE')
bm = bmesh.from_edit_mesh(bpy.context.object.data)
bm.faces.ensure_lookup_table()
for i in range(len(bm.faces)):
    bm.faces.ensure_lookup_table()
    bm.faces[i].select = True
    x = -0.2 + random.random()*0.4
    y = -0.2 + random.random()*0.4
    z = -0.2 + random.random()*0.4
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate = {"value":(x,y,z)})
    bpy.ops.mesh.select_all(action='DESELECT')
