import pygame

class Ship:
    """Class for ship control"""
    def __init__(self, ai_game):
        """Init of ship and set initial coordinates"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Downdload ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Spawn new ship at screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)