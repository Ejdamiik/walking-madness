import pygame
import random
import time
from player import Player
from environment import Game

# --- constants ---

WHITE = (255, 255, 255)
BLACK = (0  ,   0,   0)

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

FPS = 30

BLOCK_WIDTH = 80
BLOCK_HEIGHT = 80

SPEED = 10

# --- functions ---

def run():

    mainloop = True
    dx, dy = 0, 0

    while mainloop:

        # --- events ---

        for event in pygame.event.get():

            if event.type == pygame.QUIT: 
                mainloop = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False

                # - start moving -
                elif event.key == pygame.K_UP:
                    dy = -SPEED
                    player.rotate("up")

                elif event.key == pygame.K_DOWN:
                    dy = SPEED
                    player.rotate("down")

                elif event.key == pygame.K_LEFT:
                    dx = -SPEED
                    player.rotate("left")

                elif event.key == pygame.K_RIGHT:
                    dx = SPEED
                    player.rotate("right")

                # Ability
                elif event.key == pygame.K_SPACE:
                    game.player_attack()

            elif event.type == pygame.KEYUP:
                # - stop moving -
                if event.key == pygame.K_UP:
                    dy = 0
                elif event.key == pygame.K_DOWN:
                    dy = 0
                elif event.key == pygame.K_LEFT:
                    dx = 0
                elif event.key == pygame.K_RIGHT:
                    dx = 0          

        # --- updates ---

        game.player_move(dx, dy)

        # --- draws ---

        game.screen.blit(game.bg_surface, game.bg_rect)
        game.screen.blit(player.surface, player.block)

        for sur, rect in game.to_blit:
            game.screen.blit(sur, rect)

        pygame.display.flip()

        clock.tick(FPS)

# --- main ---

player = Player(BLOCK_WIDTH, BLOCK_HEIGHT, (0, 0, 0))
player.init_attrs(DISPLAY_WIDTH, DISPLAY_HEIGHT)

game = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT, player)
game.load_texture("textures//floor.png")

clock = pygame.time.Clock()

run()

pygame.quit()