import pygame

# Game settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

# World settings
WORLD_SIZE = (3840, 2160)  # Twice the screen size to allow for scrolling
TILE_SIZE = 32

# Player settings
PLAYER_SPEED = 5
PLAYER_START_HEALTH = 100
PLAYER_START_HUNGER = 100
PLAYER_START_THIRST = 100
PLAYER_START_STAMINA = 100

# Input settings
MOVEMENT_KEYS = {
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1)
}

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Tile colors
TILE_COLORS = {
    'deep_water': (0, 0, 139),    # Dark blue
    'shallow_water': (0, 191, 255),  # Deep sky blue
    'sand': (238, 214, 175),      # Light yellow
    'grass': (34, 139, 34),       # Forest green
    'forest': (0, 100, 0),        # Dark green
    'mountain': (139, 137, 137),  # Gray
    'snow': (255, 250, 250)       # Snow white
}

# Resource settings
RESOURCE_RESPAWN_TIME = 300  # seconds

# UI settings
UI_FONT_SIZE = 24
UI_PADDING = 10
UI_BAR_HEIGHT = 20
UI_BAR_WIDTH = 200

# Game states
STATE_MAIN_MENU = 0
STATE_PLAYING = 1
STATE_PAUSED = 2
STATE_GAME_OVER = 3

# Inventory settings
INVENTORY_SIZE = 20

PLAYER_SPEED = 5  # Adjust this value to change movement speed