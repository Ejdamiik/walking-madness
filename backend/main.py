import input_handle as ih
from draw import DrawTree

tree = ih.get_tree("in.txt")
vis = DrawTree(800, 800, tree)

res = vis.get_image()

vis.get_text()

res.show()
