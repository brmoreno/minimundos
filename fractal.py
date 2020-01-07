import bpy 
import bmesh 
import random
import mathutils

bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action="DESELECT")
bpy.ops.mesh.select_mode(type = "FACE")
bm = bmesh.from_edit_mesh(bpy.context.object.data)

for j in range (3):
    bm.faces.ensure_lookup_table()
    extrude = random.random()
    escala = random.random()
    for i in range(len(bm.faces)):
        bm.faces.ensure_lookup_table()
        bm.faces[i].select = True
        original = bm.faces[i].calc_center_median_weighted()
        var1 = 0.8 +random.random()*0.3
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate = {"value": original*extrude*var1})
        tam = escala
        var2 = -0.1 +random.random()*0.2
        bpy.ops.transform.resize(value =(tam+var2,tam+var2,tam+var2))
        bpy.ops.mesh.select_all(action="DESELECT")
bpy.ops.object.mode_set(mode='OBJECT')
