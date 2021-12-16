from typing import Any, Tuple, List, Optional
from PIL import Image, ImageDraw, ImageFont
from backend.draw import Draw
from backend.tree import Tree


Point = Tuple[int, int]
DEFINING_CONST = 6

class DrawTree(Draw):

    def __init__(self,
                width: int,
                height: int,
                tree: Tree) -> None:
        
        self.im = Image.new("RGB", (width, height), self.get_bg())
        # Drawing context for image
        self.draw = ImageDraw.Draw(self.im)

        #----------Tree properties------------#
        self.tree = tree
        depth = self.tree.get_depth()
        self.tree_width = self.tree.get_width()
        #------------------------------------#

        #------------Scale--------------------------------------------------------------------#
        self.node_radius = min(width, height) // (max(depth, self.tree_width) * DEFINING_CONST)
        font_size = self.node_radius
        self.font = ImageFont.truetype("arial.ttf", font_size)

        if depth != 1:
            self.y_step = height // (depth - 1)
        else:
            self.y_step = height

        self.y_step -= 2 * self.node_radius + 50
        #-------------------------------------------------------------------------------------#

        self.lines: List[Tuple[Point, Point]] = []
        self.nodes: List[Point] = []

    def get_text(self) -> str:
        """
        Method to get text-representation of tree
        """

        out = []
        self.draw_levels(self.tree, 0, "", "", out)

        return "<br/>".join(out)

    def draw_levels(self,
                    tree: Tree,
                    level: int,
                    branching: str,
                    previous: str,
                    output: List[str]) -> None:

        """
        Help-func for text representation of tree
        """

        content = tree.value

        if level != 0:
            spacing = "─ "
        else:
            spacing = ""

        ln = previous + branching + spacing + content

        # Console output
        # print(ln)

        output.append(ln)


        vertical = "│" if branching == "├" else ""

        if vertical == "":
            if level != 0:
                padding = 3 * " " if tree.parent else ""
            else:
                padding = ""
        else:
            padding = 2 * " " if tree.parent else ""

        previous += vertical + padding

        for i in range(len(tree.children)):

            # If we are starting new branch
            if i == 0:
                branching = "├"

            # If we finish current branch
            if i == len(tree.children) - 1:
                branching = "└"

            # Goin' deeper
            self.draw_levels(tree.children[i],
                level + 1, branching, previous, output)


    def get_image(self) -> Image:

        self.draw_rec(self.tree, self.tree, 1,
                      (self.im.width // 2, self.node_radius + 5),
                      (self.im.width // 2, self.node_radius + 5),
                      self.im.width // 4
                     )

        #---------Actual drawing--------#
        for prev, curr in self.lines:
            self.line(prev, curr)

        for point, val in self.nodes:
            self.circle(point)
            self.text(point, str(val))
        #------------------------------#

        return self.im

    def overlap(self, point: Point) -> Optional[Point]:
        """
        If points overlap -- it moves new point
        """

        for points in self.lines:

            a, b = points
            if point == b:

                if a[0] < b[0]:
                    x, y = point
                    return x - self.im.width // 5, y
                else:
                    x, y = point
                    return x + self.im.width // 5, y

    def draw_rec(self,
                tree: Tree,
                root: Tree,
                level: int,
                prev: Point,
                curr: Point,
                prev_xs: int) -> None:

        if not tree:
            return

        overlap_ = self.overlap(curr)
        if overlap_:
            curr = overlap_

        x, y = curr

        self.lines.append((prev, curr))
        self.nodes.append((curr, tree.value))

        next_width = root.gw_b_l(level + 1)
        width = root.gw_b_l(level)
        nw = next_width

        if width > next_width:
            next_width = width

        if next_width == 0:
            return
        elif next_width == 1:
            x_step = x
        else:
            x_step = (self.im.width // (next_width - 1)) // 2

        next_width = nw
        if next_width == 1:
            leftmost = x
        elif next_width % 2 == 0:
            leftmost = x - ((next_width // 4) * (x_step) + (x_step // 2))
        else:
            leftmost = leftmost = x - (next_width // 2) * (x_step)
            

        for i, child in enumerate(tree.children):

            self.draw_rec(child, root, level + 1, (x,y), (leftmost + i * x_step, y + self.y_step),  x_step)
