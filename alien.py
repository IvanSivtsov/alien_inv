import pygame

class Alien:
    """Class for alien control"""
    def __init__(self, ai_game):
        """Init of alien and set initial coordinates"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load alien image and get rect
        self.image = pygame.image.load('alien_inv/images/alien.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        #Spawn new alien at the top left corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
    def blitme(self):
        """Draw alien in current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien down the screen"""
        self.rect.y += self.settings.alien_speed
