import pygame
from typing import Tuple

class Player:

    def __init__(self,
                 block_width: int,
                 block_height: int,
                 color: Tuple[int, int, int]) -> None:
        
        self.bh = block_height
        self.bw = block_width
        self.color = color

        # --- To be initialized
        self.block = None
        self.surface = None
        self.pos: Optional[Tuple[int, int]] = None
        self.base = None

        self.rotation = {
            "up": 90,
            "down": 270,
            "left": 180,
            "right": 0
        }

    def init_attrs(self, screen_w: int, screen_h: int) -> None:

        self.pos = (screen_w // 2, screen_h // 2)
        self.surface, self.block = self.load_texture("textures//player.png")
        self.block.center = self.pos
        self.base = self.surface

    def move(self, dx: int, dy: int) -> None:

        x, y = self.pos

        self.block.move_ip(dx, dy)
        self.pos = (x + dx, y + dy)

    def rotate(self, direction: int) -> None:

        self.surface = pygame.transform.rotate(self.base, self.rotation[direction])

    def attack(self):

        x, y = self.pos

        # --- Temporary
        attacked = pygame.Rect(x, y, self.bw, self.bh)
        attacked_surface = pygame.Surface(attacked.size)

        return attacked_surface, attacked

    def load_texture(self, path: str):

        texture = pygame.image.load(path)
        texture = pygame.transform.scale(texture, (self.bw, self.bh))
        block = texture.get_rect()

        return texture, block
