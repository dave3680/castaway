import pygame

class UI:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.font = pygame.font.Font(None, 36)

    def render(self):
        health_text = self.font.render(f"Health: {self.player.health}", True, (255, 255, 255))
        hunger_text = self.font.render(f"Hunger: {self.player.hunger}", True, (255, 255, 255))
        thirst_text = self.font.render(f"Thirst: {self.player.thirst}", True, (255, 255, 255))
        stamina_text = self.font.render(f"Stamina: {self.player.stamina}", True, (255, 255, 255))

        self.screen.blit(health_text, (10, 10))
        self.screen.blit(hunger_text, (10, 50))
        self.screen.blit(thirst_text, (10, 90))
        self.screen.blit(stamina_text, (10, 130))