import bpy

#Renames the uv map, and if the object does not have a uv map we create one.

def RenameUV():
  for obj in bpy.context.selected_objects :
    if obj.type == 'MESH':
      obj.select_set(True)
      if obj.data.uv_layers.active_index<0:
        obj.data.uv_layers.new(name="UVMap", do_init=True)
      else:
        for uvmap in  obj.data.uv_layers :
            uvmap.name = 'UVMap'
RenameUV()

###################

#Replace 1 material with another.
#Todo: Make smart.

def RemapMat():
    for obj in bpy.context.selected_objects :
    if obj.type == 'MESH':
      obj.select_set(True)
      old_mat = bpy.data.materials.get("FirstMaterialNameHere")
      new_mat = bpy.data.materials.get("SecondMaterialNameHere")
      old_mat.user_remap(new_mat)
RemapMat()
#################

#Joins object by material name.
def JoinByMaterial():
#Future dev: JoinByMaterialColor, join meshes by the color of the material.

    context = bpy.context
    scene = context.scene
    mats = [m.name for m in bpy.data.materials]
    for mat in mats:
        obs = [o for o in scene.objects
                if o.type == 'MESH'
                and mat in o.material_slots]
        if len(obs) > 1:
#clear prior selection
            for o in context.selected_objects:
                o.select_set(False)
            for o in obs:
                o.select_set(True)
#Check if the object has an uvmap, if not create one with name "UVMap"
                if o.data.uv_layers.active_index<0:
                    o.data.uv_layers.new(name="UVMap", do_init=True)
                else:
#If the object has a UVMap, rename it to "UVMap", so the Uvs wont break when we join objects
                    for uvmap in o.data.uv_layers :
                        uvmap.name = 'UVMap'
            context.view_layer.objects.active = obs[0]
            bpy.ops.object.join()
        
JoinByMaterial()
