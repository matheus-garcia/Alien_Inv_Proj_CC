import pygame
from pygame.sprite import Sprite

class Virus(Sprite):
    """A class that represents the only enemy fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initializes the enemy and defines its initial position."""
        super(Virus, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Loads an image of the enemy and defines its rect.
        self.image = pygame.image.load('images\sirus.bmp')
        self.rect = self.image.get_rect()
        
        # Initializes each new enemy next to the left-top corner 
        # of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Stores virus' exactly position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draws the enemy on its current position."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Moves the virus to the right"""
        self.x += self.ai_settings.virus_speed_factor
        self.rect.x = self.x