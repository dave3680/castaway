import numpy as np
import pygame
from opensimplex import OpenSimplex
from config import TILE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, TILE_COLORS

class World:
    def __init__(self, width=4000, height=4000):
        self.width = width
        self.height = height
        self.tiles = self.generate_world()

    def generate_world(self):
        # Create noise generator
        gen = OpenSimplex(seed=np.random.randint(0, 1000000))

        # Generate base noise
        scale = 50.0
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0

        noise = np.zeros((self.height // TILE_SIZE, self.width // TILE_SIZE))
        for y in range(noise.shape[0]):
            for x in range(noise.shape[1]):
                noise[y][x] = self.generate_noise(gen, x, y, octaves, persistence, lacunarity, scale)

        # Normalize noise
        noise = (noise - noise.min()) / (noise.max() - noise.min())

        # Apply circular mask
        Y, X = np.ogrid[:noise.shape[0], :noise.shape[1]]
        center = (noise.shape[0] / 2, noise.shape[1] / 2)
        dist_from_center = np.sqrt((X - center[1])**2 + (Y - center[0])**2)
        mask = dist_from_center <= (noise.shape[0] / 2)
        noise = noise * mask

        # Generate tiles based on noise values
        tiles = [['deep_water' for _ in range(self.width // TILE_SIZE)] for _ in range(self.height // TILE_SIZE)]
        for y in range(noise.shape[0]):
            for x in range(noise.shape[1]):
                if noise[y][x] < 0.3:
                    tiles[y][x] = 'deep_water'
                elif noise[y][x] < 0.35:
                    tiles[y][x] = 'shallow_water'
                elif noise[y][x] < 0.4:
                    tiles[y][x] = 'sand'
                elif noise[y][x] < 0.7:
                    tiles[y][x] = 'grass'
                else:
                    tiles[y][x] = 'forest'

        return tiles

    def generate_noise(self, gen, x, y, octaves, persistence, lacunarity, scale):
        noise = 0
        amplitude = 1
        frequency = 1
        for _ in range(octaves):
            noise += amplitude * gen.noise2(x * frequency / scale, y * frequency / scale)
            amplitude *= persistence
            frequency *= lacunarity
        return noise

    def is_valid_position(self, x, y):
        tile_x, tile_y = int(x // TILE_SIZE), int(y // TILE_SIZE)
        if 0 <= tile_x < self.width // TILE_SIZE and 0 <= tile_y < self.height // TILE_SIZE:
            return self.tiles[tile_y][tile_x] not in ['deep_water', 'shallow_water']
        return False

    def update(self):
        # For future dynamic world updates
        pass

    def render(self, screen, camera_x, camera_y):
        start_x = max(0, camera_x // TILE_SIZE - SCREEN_WIDTH // (2 * TILE_SIZE))
        start_y = max(0, camera_y // TILE_SIZE - SCREEN_HEIGHT // (2 * TILE_SIZE))
        end_x = min(self.width // TILE_SIZE, start_x + SCREEN_WIDTH // TILE_SIZE + 1)
        end_y = min(self.height // TILE_SIZE, start_y + SCREEN_HEIGHT // TILE_SIZE + 1)

        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                tile = self.tiles[y][x]
                color = self.get_tile_color(tile)
                pygame.draw.rect(screen, color, 
                                 (x * TILE_SIZE - camera_x + SCREEN_WIDTH // 2, 
                                  y * TILE_SIZE - camera_y + SCREEN_HEIGHT // 2, 
                                  TILE_SIZE, TILE_SIZE))

    def get_tile_color(self, tile):
        return TILE_COLORS.get(tile, (0, 0, 0))  # Default to black if tile type is unknown