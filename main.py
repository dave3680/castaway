import pygame
from game.game import Game
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Castaway Chronicles")
    
    game = Game(screen)

    running = True
    while running:
        running = game.handle_events()  # This should return a boolean
        game.update()
        game.render()

    pygame.quit()

if __name__ == "__main__":
    main()