import sys
import pygame
from bullet import Bullet
from virus import Virus

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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()        
    
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
                
def update_screen(ai_settings, screen, ship, viruses, bullets):
    """Update images on screen and alternate to a new one"""
    # Redraw the screen after each loop pass
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets after ship and virus
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    viruses.draw(screen)
    
    pygame.display.flip()
    
    
def update_bullets(bullets):
    """Update bullets position and get rid of old ones"""
    # Update bullets position
    bullets.update()
    
    # Get rid of old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if the limit isn't reached."""
    # Create a new bullet and add to the bullets group
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        
        
def create_fleet(ai_settings, screen, viruses):
    """Creates a complete fleet of virus"""
    # Creates and calculates the number of virus in a line
    virus = Virus(ai_settings, screen)
    virus_width = virus.rect.width
    available_space_x = ai_settings.screen_width - 2 * virus_width
    number_viruses_x = int(available_space_x / (2 * virus_width))
    
    # Creates the first virus line
    for virus_number in range(number_viruses_x):
        # Creates the virus in the line
        virus = Virus(ai_settings, screen)
        virus.x = virus_width + 2 * virus_width * virus_number
        virus.rect.x = virus.x
        viruses.add(virus)