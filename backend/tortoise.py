import math
from typing import Tuple, Union

class Tortoise():

    def __init__(self):

        self.x, self.y, self.angle = 0.0, 0.0, 0.0

    def position(self) -> Tuple[float, float]:
        return self.x, self.y

    def xcor(self) -> float:
        return self.x

    def ycor(self) -> float:
        return self.y

    def forward(self, distance: Union[float, int]) -> None:
        angle_radians = math.radians(self.angle)

        self.x += math.cos(angle_radians) * distance
        self.y += math.sin(angle_radians) * distance

    def backward(self, distance: int) -> None:
        self.forward(-distance)

    def right(self, angle: Union[float, int]) -> None:
        self.angle -= angle

    def left(self, angle: Union[float, int]) -> None:
        self.angle += angle

    def setpos(self, x: Union[float, int], y: Union[float, int]) -> None:
        """Can be passed either a tuple or two numbers."""
        if y == None:
            self.x = x[0]
            self.y = y[1]
        else:
            self.x = x
            self.y = y
