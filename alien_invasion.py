import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def  run_game():
    # Initialize the game and create a object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create a ship
    ship = Ship(ai_settings, screen)
    
    # Initiate the main loop of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
         
        # Turn the most recently screen visible
        pygame.display.flip()
        
run_game() 
