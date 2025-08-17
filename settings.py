class Settings:
    """Configuration class for all settings in game"""

    def __init__(self):
        """Init of game settings"""
        #Screen params
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (15, 14, 48)
        self.ship_speed = 10

        #Bullet params
        self.bullet_speed = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3