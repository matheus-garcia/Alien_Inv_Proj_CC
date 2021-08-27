import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that manages bullets shoot by the ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """
        Creates a object for the bullet on the current ship position
        """
        super().__init__()
        self.screen = screen
        
        # Creates a rectangle for the bullet in (0, 0) and defines its
        # correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top + ai_settings.bullet_height
        
        # Stores the bullet's position as a float
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """Moves the bullet up the screen"""
        # Update the float position of the bullet
        self.y -=self.speed_factor
        
        # Update rectangle's position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw a bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)