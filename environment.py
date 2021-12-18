import pygame
from typing import List, Tuple
from random import randint


class Game:

    def __init__(self, width: int, height: int, player: "Player") -> None:

        pygame.init()
        pygame.display.set_caption('Test Game')

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode( (width, height) )
        self.rect = self.screen.get_rect()

        self.bg_rect = self.rect
        self.to_blit = []

        self.player = player
        self.player.pos = (self.width // 2, self.height // 2)


    def load_texture(self, path: str) -> None:

        self.bg_surface = pygame.image.load(path)
        self.bg_surface = pygame.transform.scale(self.bg_surface, (self.width, self.height))
        self.rect.left, self.rect.top = (0, 0)

    def player_move(self, dx: int, dy: int) -> None:

        x, y = self.player.pos

        margin = min(self.player.bh, self.player.bw) // 2
        # --- Borders check ---
        if x + dx +  margin > self.width or x + dx - margin < 0:
            return

        if y + dy + margin > self.height or y + dy - margin < 0:
            return
        # ---

        self.player.move(dx, dy)
