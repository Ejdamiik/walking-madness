from typing import Tuple
from backend.input_handle import get_config

Point = Tuple[int, int]

LINE_WIDTH = 5

conf = get_config("backend//config.json")

#-----Colors-----#
NODE_COLOR = tuple(conf["node-color"])
NODE_OUTLINE = tuple(conf["node-outline"])
LINE_COLOR = tuple(conf["line-color"])
TEXT_COLOR = tuple(conf["text-color"])
BG_COLOR = tuple(conf["background-color"])


class Draw:

    def get_bg(self) -> Tuple[int, int, int]:
        return BG_COLOR

    #------------------Shape procedures-----------------------------#
    def circle(self, m: Point) -> None:
        x, y = m
        self.draw.ellipse((x - self.node_radius, y - self.node_radius, x + self.node_radius, y + self.node_radius),
                          fill=NODE_COLOR, outline = NODE_OUTLINE)

    def line(self, from_: Point, to: Point) -> None:
        x1, y1 = from_
        x2, y2 = to
        self.draw.line((x1, y1, x2, y2), fill = LINE_COLOR, width = LINE_WIDTH)

    def text(self, where: Point, val: str) -> None:

        x, y = where
        w, h = self.draw.textsize(val)
        self.draw.text((x - self.node_radius // 2 + w, y - self.node_radius // 2), val, TEXT_COLOR,
                        anchor="ms",  font = self.font)
    #--------------------------------------------------------------#
