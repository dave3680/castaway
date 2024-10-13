import pygame
from config import PLAYER_SPEED, PLAYER_START_HEALTH, PLAYER_START_HUNGER, PLAYER_START_THIRST, PLAYER_START_STAMINA, TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, world, start_x, start_y):
        self.world = world
        self.x = start_x
        self.y = start_y
        self.health = PLAYER_START_HEALTH
        self.hunger = PLAYER_START_HUNGER
        self.thirst = PLAYER_START_THIRST
        self.stamina = PLAYER_START_STAMINA
        self.inventory = []
        self.move_direction = [0, 0]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_direction[0] = -1
            elif event.key == pygame.K_RIGHT:
                self.move_direction[0] = 1
            elif event.key == pygame.K_UP:
                self.move_direction[1] = -1
            elif event.key == pygame.K_DOWN:
                self.move_direction[1] = 1
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                self.move_direction[0] = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                self.move_direction[1] = 0

    def update(self):
        dx = self.move_direction[0] * PLAYER_SPEED
        dy = self.move_direction[1] * PLAYER_SPEED
        new_x = self.x + dx
        new_y = self.y + dy
        if self.world.is_valid_position(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def render(self, screen, camera_x, camera_y):
        pygame.draw.rect(screen, (255, 0, 0),
                         (SCREEN_WIDTH // 2 - TILE_SIZE // 2,
                          SCREEN_HEIGHT // 2 - TILE_SIZE // 2,
                          TILE_SIZE, TILE_SIZE))