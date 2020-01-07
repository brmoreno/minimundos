import bpy
import bmesh
import numpy
import math
import random

def chipote (mesh_, ind_, rad_, amp_):    
    for i in range(len(mesh_.vertices)):
        dist = numpy.linalg.norm(mesh_.vertices[ind_].co - mesh_.vertices[i].co)
        if dist<rad_ :
           amps[i] +=(amp_ * math.sin(((rad_-dist)/rad_)*math.pi/2))
      
            
bm = bmesh.new()
bmesh.ops.create_icosphere(bm, subdivisions  = 5, diameter = 1)
mesh = bpy.data.meshes.new('_mesh') 
bm.to_mesh(mesh)

amps = []
for i in range(len(mesh.vertices)):
    amps.append(1)

for i in range (200):
    radio = random.random()*0.3 
    amp =  -0.5 + random.random()*1
    chipote(mesh,random.randrange(len(mesh.vertices)),radio,amp)
    
for i in range(len(mesh.vertices)):
    mesh.vertices[i].co*=amps[i]

obj = bpy.data.objects.new('_mesh',mesh)
bpy.context.collection.objects.link(obj)
bpy.data.objects['_mesh'].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects['_mesh']
