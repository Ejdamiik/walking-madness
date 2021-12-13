import math

class Tortoise():
    def __init__(self):
        self.x, self.y, self.angle = 0.0, 0.0, 0.0
        self.pointsVisited = []
        self._visit()

    def position(self):
        return self.x, self.y

    def xcor(self):
        return self.x

    def ycor(self):
        return self.y

    def forward(self, distance):
        angle_radians = math.radians(self.angle)

        self.x += math.cos(angle_radians) * distance
        self.y += math.sin(angle_radians) * distance

        self._visit()

    def backward(self, distance):
        self.forward(-distance)

    def right(self, angle):
        self.angle -= angle

    def left(self, angle):
        self.angle += angle

    def setpos(self, x, y = None):
        """Can be passed either a tuple or two numbers."""
        if y == None:
            self.x = x[0]
            self.y = y[1]
        else:
            self.x = x
            self.y = y
        self._visit()

    def _visit(self):
        """Add point to the list of points gone to by the turtle."""
        self.pointsVisited.append(self.position())
