from backend.graph.tortoise import Tortoise
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple

Point = Tuple[int, int]

LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 5
NODE_COLOR = (255, 255, 255)
NODE_OUTLINE = (0, 0, 0)
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)


class DrawGraph:

    def __init__(self, graph, width, height):
        
        self.im = Image.new("RGB", (width, height), BG_COLOR)
        # Drawing context for image
        self.draw = ImageDraw.Draw(self.im)

        self.graph = graph
        self.nodes = self.get_nodes()

        self.node_distance =  width // 3

        self.node_radius = 10

        self.dx = width // 5
        self.dy = None

        font_size = max(width, height) // 20
        self.font = ImageFont.truetype("arial.ttf", font_size)
        # ---

        self.nodes_coords = self.get_node_coords(width)
        self.lines = set()

    def get_node_coords(self, width):

        n = len(self.nodes)
        tortoise = Tortoise()
        coords = []

        tortoise.setpos(300, 300)

        angle = 360 // n
        for i in range(n):
            
            tortoise.forward(self.node_distance)
            coords.append((tortoise.xcor(), tortoise.ycor()))
            tortoise.backward(self.node_distance)
            tortoise.left(angle)

        nodes_coords = dict(zip(self.nodes, coords))
        return nodes_coords

    def get_nodes(self):

        members = set()

        for from_, to in self.graph.items():

            members = members | {from_}
            members = members | set(to)

        return list(members)

    def get_image(self):

        lines = self.get_lines()

        for line in lines:
            from_, to = line
            self.line(from_, to)

        for node, pos in self.nodes_coords.items():
            self.circle(pos)
            # self.text(pos, node)

        return self.im

    def get_lines(self):

        lines = set()
        for from_, to in self.graph.items():

            for node in to:
                lines.add((self.nodes_coords[from_], self.nodes_coords[node]))

        return lines

    #------------------Shape procedures-----------------------------#
    def circle(self, m: Point) -> None:
        x, y = m
        self.draw.ellipse((x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius),
                          fill=NODE_COLOR, outline = NODE_OUTLINE)

    def line(self, from_: Point, to: Point) -> None:
        x1, y1 = from_
        x2, y2 = to
        self.draw.line((x1, y1, x2, y2), fill = LINE_COLOR, width = LINE_WIDTH)

    def text(self, where: Point, val) -> None:

        x, y = where
        w, h = self.draw.textsize(val)
        self.draw.text((x - 2 * w, y - 2 * h), val, TEXT_COLOR, font = self.font)
    #--------------------------------------------------------------#
