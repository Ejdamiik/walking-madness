from typing import Any
from PIL import Image, ImageDraw

class BinaryTree:

    def __init__(self, value: Any):

        self.value = value

        self.right = None
        self.left = None


t1 = BinaryTree(1)
t2 = BinaryTree(2)

t3 = BinaryTree(3)
t3.left = t1
t3.right = t2

t4 = BinaryTree(5)
t4.right = t2
t4.left = t3


def draw_tree(tree: BinaryTree, im: Image) -> Image:
    """
    draw = ImageDraw.Draw(image)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,0))
    """
    draw = ImageDraw.Draw(im)
    draw_rec(tree, draw, (im.width // 2, 20), (im.width // 2, 20))

    return im

def draw_rec(tree, im, prev, point):

    if not tree:
        return

    x, y = point
    circle(im, 10, point)
    line(im, prev, point)

    draw_rec(tree.left, im, (x,y), (x - 50, y + 50))
    draw_rec(tree.right, im, (x,y), (x + 50, y + 50))

def circle(im, r, m):

    x, y = m
    im.ellipse((x-r, y-r, x+r, y+r), fill=(255,0,0,0))


def line(im, from_, to):

    x1, y1 = from_
    x2, y2 = to
    im.line((x1, y1, x2, y2), fill=128)


im = Image.new("RGB", (800, 800), (0, 0, 0))

draw_tree(t4, im)

im.show()