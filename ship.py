import pygame

class Ship():
    """Creating a ship"""
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and its initial position"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Loads the image of the ship and  get its rectangle
        self.image = pygame.image.load('images\ship_alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Initialize each new ship in the middle bottom of the screen
        self.rect.centery = self.screen_rect.centery
        #self.rect.bottom = self.screen_rect.bottom
        
        # Store a float to the center of the ship
        self.center = float(self.rect.centerx)
        #self.bottom = float(self.rect.bottom)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False
        
    def update(self):
        """
        Update the position of the ship  according to the movement flags
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #elif self.moving_up and self.rect.top > self.screen_rect.top:
            #self.bottom -= self.ai_settings.ship_speed_factor
            
        #elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #self.bottom += self.ai_settings.ship_speed_factor
            
        # Update object rect
        self.rect.centerx = self.center
        #self.rect.bottom = self.bottom
        
    def blitme(self):
        """Draw a spaceship on its current position"""
        self.screen.blit(self.image, self.rect)
        