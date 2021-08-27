import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from virus import Virus
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
    
    # Creates a group which will be used to store the bullets
    bullets = Group()
    
    # Creates an enemy
    virus = Virus(ai_settings, screen)
    
    
    # Initiates the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, virus, bullets)
                         
        # Turn the most recently screen visible
        pygame.display.flip()
        
run_game()