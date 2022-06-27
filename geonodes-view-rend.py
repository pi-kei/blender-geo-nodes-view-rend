bl_info = {
    "name": "GeoNodes Viewport-Render",
    "description": "Duplicates selected Geometry Nodes midifier and connects inputs via drivers to setup one for viewport and other for render.",
    "author": "ComputersDontCompost",
    "version": (1, 0),
    "blender": (3, 2, 0), # could work in older versions but not tested
    "location": "3D View > Object > GeoNodes Viewport-Render",
    #"warning": "", # used for warning icon and text in addons panel
    "doc_url": "https://github.com/pi-kei/blender-geo-nodes-view-rend#readme",
    "tracker_url": "https://github.com/pi-kei/blender-geo-nodes-view-rend/issues",
    "support": "COMMUNITY",
    "category": "Object",
}

import bpy


def main(context):
    object = context.object
    old_mod = object.modifiers.active
    old_mod.show_render = False
    old_mod.show_viewport = True
    bpy.ops.object.modifier_add(type='NODES')
    mod = object.modifiers.active
    bpy.ops.object.modifier_move_to_index(modifier=mod.name, index=object.modifiers.find(old_mod.name) + 1)
    mod.show_viewport = False
    mod.show_render = True
    mod.node_group = old_mod.node_group
    for name in old_mod.keys():
        if name.endswith("_use_attribute") or name.endswith("_attribute_name"):
            continue
        driver = object.driver_add("modifiers[\""+mod.name+"\"][\""+name+"\"]").driver
        for variable in driver.variables.values():
            driver.variables.remove(variable)
        variable = driver.variables.new()
        variable.type = 'SINGLE_PROP'
        variable.targets[0].id = object.id_data
        variable.targets[0].data_path = "modifiers[\""+old_mod.name+"\"][\""+name+"\"]"
        driver.expression = variable.name


class GeoNodesViewportRender(bpy.types.Operator):
    """Duplicates selected Geometry Nodes midifier and connects inputs via drivers to setup one for viewport and other for render"""
    bl_idname = "object.geonodes_view_rend"
    bl_label = "GeoNodes Viewport-Render"

    @classmethod
    def poll(cls, context):
        return bpy.context.object is not None and bpy.context.object.modifiers.active is not None and bpy.context.object.modifiers.active.type == 'NODES'

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(GeoNodesViewportRender.bl_idname, text=GeoNodesViewportRender.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(GeoNodesViewportRender)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(GeoNodesViewportRender)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
