from typing import List, Tuple, Optional


class Tree:

    def __init__(self, value: int):

        self.value = value

        self.parent: Optional["Tree"] = None
        self.children: List["Tree"] = []


    def get_depth(self) -> int:

        if self.children == []:
            return 1

        depths: List[int] = []

        for child in self.children:
            depths.append(child.get_depth())

        depth = 1 + max(depths)

        return depth


    def get_max_width(self) -> int:

        max_width = 0
        depth = self.get_depth()

        for i in range(1, depth + 1):
            width = self.get_width(i)

            if width > max_width:
                max_width = width

        return max_width


    def get_width(self, level: int) -> int:

        if level == 1:
            return 1

        elif level > 1:

            width = 0
            for child in self.children:
                width += child.get_width(level - 1)

        return width
