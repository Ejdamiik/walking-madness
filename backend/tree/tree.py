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


    def get_width(self) -> int:

        depth = self.get_depth()

        res = 0
        for level in range(1, depth + 1):

            width = self.gw_b_l(level)
            if width > res:
                res = width

        return res


    def gw_b_l(self, level: int) -> int:

        if level == 1:
            return 1

        elif level > 1:

            width = 0
            for child in self.children:
                width += child.gw_b_l(level - 1)

        return width
