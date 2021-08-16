import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def  run_game():
    # Initializes the game and create a object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Creates a ship
    ship = Ship(ai_settings, screen)
    
    # Create a group which will be used to store the bullets
    bullets = Group()
    
    
    # Initiates the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        
        # Get rid of disappeared bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
                 
        # Turn the most recently screen visible
        pygame.display.flip()
        
run_game() 
