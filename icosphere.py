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
bpy.context.object.location[0] = 1.99
