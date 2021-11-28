from typing import Any, Tuple, List
from PIL import Image, ImageDraw
from structures import Tree


Point = Tuple[int, int]


#-----Colors-----#
NODE_COLOR = (0, 0, 0)
NODE_OUTLINE = (255, 255, 255)
LINE_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)

#-----Others-----#
LINE_WIDTH = 2


class DrawTree:

    def __init__(self,
                width: int,
                height: int,
                tree: Tree) -> None:
        
        self.im = Image.new("RGB", (width, height), (0, 0, 0))

        # Drawing context for image
        self.draw = ImageDraw.Draw(self.im)

        self.tree = tree

        self.lines: List[Tuple[Point, Point]] = []
        self.nodes: List[Point] = []

        depth = self.tree.get_depth()
        tree_width = self.tree.get_max_width()

        self.y_step = height // depth
        self.smallest_x = width // (tree_width * 4)

        self.node_radius = min(width, height) // (max(depth, tree_width) * 6)


    def get_image(self) -> Image:

        self.draw_rec(self.tree, (self.im.width // 2, self.node_radius + 5), (self.im.width // 2, self.node_radius + 5))

        for prev, curr in self.lines:
            self.line(prev, curr)

        for point, val in self.nodes:
            self.circle(point)
            self.text(point, str(val))

        return self.im


    def draw_rec(self,
                tree: Tree,
                prev: Point,
                curr: Point) -> None:

        if not tree:
            return

        x, y = curr

        self.lines.append((prev, curr))
        self.nodes.append((curr, tree.value))

        line = len(tree.children) - 1

        x_step = len(tree.children) * self.smallest_x
        leftmost = x - line * x_step // 2

        for i, child in enumerate(tree.children):

            self.draw_rec(child, (x,y), (leftmost + i * x_step, y + self.y_step))


    def circle(self, m):

        x, y = m
        self.draw.ellipse((x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius),
                            fill=NODE_COLOR, outline = NODE_OUTLINE)


    def line(self, from_, to):

        x1, y1 = from_
        x2, y2 = to
        self.draw.line((x1, y1, x2, y2), fill = LINE_COLOR, width = LINE_WIDTH)


    def text(self, where, val):

        x, y = where

        w, h = self.draw.textsize(val)
        self.draw.text((x - w // 2, y - h // 2), val, TEXT_COLOR)


t1 = Tree(50)
t1.children = [Tree(1), Tree(1), Tree(1), Tree(8)]
for child in t1.children:
    child.children = [Tree(1), Tree(1)]


#print(t1.get_depth())
#print(t1.get_MaxWidth())

vis = DrawTree(800, 600, t1)
im = vis.get_image()

im.show()
