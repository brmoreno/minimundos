import bpy
import bmesh
import numpy
import math
import random

polinizados = []

def chipote (mesh_, ind_, rad_, amp_):    
    for i in range(len(mesh_.vertices)):
        dist = numpy.linalg.norm(mesh_.vertices[ind_].co - mesh_.vertices[i].co)
        if dist<rad_ :
           amps[i] +=(amp_ * math.sin(((rad_-dist)/rad_)*math.pi/2))
      
 
def polin (mesh_, ind_, rad_): 
    posibles = []   
    for i in range(len(mesh_.vertices)):
        dist = numpy.linalg.norm(mesh_.vertices[ind_].co - mesh_.vertices[i].co)
        if dist<rad_ :
           posibles.append(i)
    nuevapos = random.choice(posibles)
    return nuevapos
    
      
            
bm = bmesh.new()
bmesh.ops.create_icosphere(bm, subdivisions  = 4, diameter = 1)
mesh = bpy.data.meshes.new('_mesh') 
bm.to_mesh(mesh)

amps = []
for i in range(len(mesh.vertices)):
    amps.append(1)

for i in range (200):
    radio = random.random()*0.4 
    amp =  -0.25 + random.random()*0.5
    chipote(mesh,random.randrange(len(mesh.vertices)),radio,amp)
    
for i in range(len(mesh.vertices)):
    mesh.vertices[i].co*=amps[i]

pos = 0;
for i in range(100):
    polinizados.append(polin(mesh,pos,0.3))
    pos = polin(mesh,pos,0.3)

polinizados = list(dict.fromkeys(polinizados))
print(polinizados)

obj = bpy.data.objects.new('_mesh',mesh)
bpy.context.collection.objects.link(obj)
bpy.data.objects['_mesh'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['_mesh']

for i in polinizados:
    bpy.ops.mesh.primitive_cube_add(size=0.1, location=(mesh.vertices[i].co))
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
