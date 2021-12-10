from typing import Any, Tuple, List
from PIL import Image, ImageDraw, ImageFont
from backend.structures import Tree


Point = Tuple[int, int]


#-----Colors-----#
NODE_COLOR = (0, 0, 0)
NODE_OUTLINE = (255, 255, 255)
LINE_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)

#-----Others-----#
LINE_WIDTH = 2
DEFINING_CONST = 6


class DrawTree:

    def __init__(self,
                width: int,
                height: int,
                tree: Tree) -> None:
        
        self.im = Image.new("RGB", (width, height), (0, 0, 0))
        # Drawing context for image
        self.draw = ImageDraw.Draw(self.im)

        #----------Tree properties------------#
        self.tree = tree
        depth = self.tree.get_depth()
        tree_width = self.tree.get_max_width()
        #------------------------------------#

        #------------Scale--------------------------------------------------------------------#
        font_size = min(width, height) // (max(depth, tree_width) * 2 * DEFINING_CONST)
        self.font = ImageFont.truetype("arial.ttf", font_size)
        self.node_radius = min(width, height) // (max(depth, tree_width) * DEFINING_CONST)
        self.y_step = height // depth
        self.smallest_x = width // (tree_width * 4)
        #-------------------------------------------------------------------------------------#

        self.lines: List[Tuple[Point, Point]] = []
        self.nodes: List[Point] = []

    def get_text(self) -> None:
        """
        Method to get text-representation of tree
        """

        out = []
        self.draw_levels(self.tree, 0, "", "", out)

        with open("out.txt", "w", encoding = "utf-8") as f:

            for line in out:
                f.write(line + "\n")

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

        self.draw_rec(self.tree,
                      (self.im.width // 2, self.node_radius + 5),
                      (self.im.width // 2, self.node_radius + 5)
                     )

        #---------Actual drawing--------#
        for prev, curr in self.lines:
            self.line(prev, curr)

        for point, val in self.nodes:
            self.circle(point)
            self.text(point, str(val))
        #------------------------------#

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

    #------------------Shape procedures-----------------------------#
    def circle(self, m: Point) -> None:
        x, y = m
        self.draw.ellipse((x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius),
                          fill=NODE_COLOR, outline = NODE_OUTLINE)

    def line(self, from_: Point, to: Point) -> None:
        x1, y1 = from_
        x2, y2 = to
        self.draw.line((x1, y1, x2, y2), fill = LINE_COLOR, width = LINE_WIDTH)

    def text(self, where: Point, val: Any) -> None:

        x, y = where
        w, h = self.draw.textsize(val)
        self.draw.text((x - w, y - h), val, TEXT_COLOR, font = self.font)
    #--------------------------------------------------------------#
