from backend.tortoise import Tortoise
from backend.draw import Draw
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, Dict, List
from backend.input_handle import get_config


Point = Tuple[int, int]


class DrawGraph(Draw):

    def __init__(self,
                 graph: Dict[str, List[str]],
                 width: int,
                 height: int) -> None:
        
        self.im = Image.new("RGB", (width, height), self.get_bg())
        # Drawing context for image
        self.draw = ImageDraw.Draw(self.im)

        self.graph = graph
        self.nodes = self.get_nodes()

        self.node_distance =  width // 3
        self.node_radius = min(width, height) // (4 * len(self.nodes))

        font_size = self.node_radius
        self.font = ImageFont.truetype("arial.ttf", font_size)
        # ---

        self.nodes_coords = self.get_node_coords(width, height)
        self.lines = set()

    def get_node_coords(self, width: int, height: int) -> Dict[str, int]:

        n = len(self.nodes)
        tortoise = Tortoise()
        coords = []

        tortoise.setpos(width // 2, height // 2)

        angle = 360 // n
        for i in range(n):
            
            tortoise.forward(self.node_distance)
            coords.append((tortoise.xcor(), tortoise.ycor()))
            tortoise.backward(self.node_distance)
            tortoise.left(angle)

        nodes_coords = dict(zip(self.nodes, coords))
        return nodes_coords

    def get_nodes(self) -> List[str]:

        members = set()

        for from_, to in self.graph.items():

            members = members | {from_}
            members = members | set(to)

        return list(members)

    def get_image(self) -> Image:

        lines = self.get_lines()

        for line in lines:
            from_, to = line
            self.line(from_, to)

        for node, pos in self.nodes_coords.items():
            self.circle(pos)
            self.text(pos, node)

        return self.im

    def get_lines(self) -> List[Tuple[int, int]]:

        lines = set()
        for from_, to in self.graph.items():

            for node in to:
                lines.add((self.nodes_coords[from_], self.nodes_coords[node]))

        return lines
