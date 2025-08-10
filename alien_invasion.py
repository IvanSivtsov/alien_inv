import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class for managing of game bahavior and resources"""

    def __init__(self):
        """Init of game and game`s resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Launch of game loop"""
        while True:
            #Track events from keyboard & mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)

            #Display of last draw screen
            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == '__main__':
    #Create instance of class and run game
    ai = AlienInvasion()
    ai.run_game()