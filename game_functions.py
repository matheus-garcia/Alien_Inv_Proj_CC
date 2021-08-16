import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Answer to  key press events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and adds it to bullet group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    
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
        

def check_events(ai_settings, screen, ship, bullets):
    """Answer to keyboard and mouse press events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ai_settings, screen, ship, bullets)
                    
            elif event.type == pygame.KEYUP:
                check_keyups_events(event, ship)             
                
def update_screen(ai_settings, screen, ship, bullets):
    """Update images on screen and alternate to a new one"""
    # Redraw the screen after each loop pass
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets after ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()