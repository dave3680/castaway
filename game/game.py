import pygame
import random
from game.world import World
from game.player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, FPS

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.world = World(width=4000, height=4000)
        self.camera_x, self.camera_y = self.find_spawn_point()
        self.player = Player(self.world, self.camera_x, self.camera_y)

    def find_spawn_point(self):
        beach_tiles = []
        for y in range(len(self.world.tiles)):
            for x in range(len(self.world.tiles[y])):
                if self.world.tiles[y][x] == 'sand':
                    beach_tiles.append((x, y))
        
        if not beach_tiles:
            raise Exception("No beach tiles found in the world!")
        
        spawn_tile = random.choice(beach_tiles)
        return spawn_tile[0] * TILE_SIZE + TILE_SIZE // 2, spawn_tile[1] * TILE_SIZE + TILE_SIZE // 2

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            self.player.handle_event(event)
        return True


    def update(self):
        self.world.update()
        self.player.update()
        self.camera_x = self.player.x
        self.camera_y = self.player.y

    def render(self):
        self.screen.fill((0, 0, 0))  # Fill with black
        self.world.render(self.screen, self.camera_x, self.camera_y)
        self.player.render(self.screen, self.camera_x, self.camera_y)
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def get_tile_at_pixel(self, x, y):
        tile_x = x // TILE_SIZE
        tile_y = y // TILE_SIZE
        if 0 <= tile_x < self.world.width // TILE_SIZE and 0 <= tile_y < self.world.height // TILE_SIZE:
            return self.world.tiles[tile_y][tile_x]
        return None