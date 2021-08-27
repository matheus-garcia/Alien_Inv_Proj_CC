class Settings():
    """A class to keep all settings from Alien Invasion"""
    
    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (146, 223, 255)
        
        # Ship settings
        self.ship_speed_factor = .5
        
        # Bullet settings
        self.bullet_speed_factor = .5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (94, 104, 27)
        self.bullets_allowed = 3