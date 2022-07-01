# Blender Add-on: GeoNodes Viewport-Render

Duplicates selected Geometry Nodes modifier and connects inputs between them via drivers to setup one for viewport and other for render. Modifier for render will have drivers on its inputs connected with corresponding inputs of the modifier for viewport. If you want input value to be different either edit or remove driver.

**NOTE**: this is just an alternative solution of using a combination of [Is Viewport](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) and [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) nodes.

## Which approach to choose?

Choose this add-on if:
- you like to create inputs to your node tree
- you don't like to pollute your tree with Is Viewport + Switch nodes
- you want to be able to see how render would look even in viewport

Choose Is Viewport + Switch nodes if:
- you don't like to create inputs to your node tree
- you don't mind adding Is Viewport + Switch nodes
- you don't mind if you have to start an actual render to see how it would look

![screenshot](https://user-images.githubusercontent.com/3518025/175836534-cc0ab52c-7d14-47e8-9b8a-a2472ac7f5cc.png)
