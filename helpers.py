from typing import Tuple
from math import sqrt


Point = Tuple[int, int]
def distance(p1: Point, p2: Point) -> float:

    x1, y1 = p1
    x2, y2 = p2

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)