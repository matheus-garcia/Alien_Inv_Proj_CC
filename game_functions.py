import sys
import pygame

def check_keydown_events(event, ship):
    """Answer to  key press events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    
def check_keyups_events(event, ship):
    """Answer to key release events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        

def check_events(ship):
    """Answer to keyboard and mouse press events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)
                    
            elif event.type == pygame.KEYUP:
                check_keyups_events(event, ship)             
                
def update_screen(ai_settings, screen, ship):
    """Update images on screen and alternate to a new one"""
    # Redraw the screen after each loop pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()