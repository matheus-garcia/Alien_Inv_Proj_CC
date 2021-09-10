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
        
def get_number_viruses_x(ai_settings, virus_width):
    """Determines the number of viruses that fits in each line"""
    available_space_x = ai_settings.screen_width - 2 * virus_width
    number_viruses_x = int(available_space_x / (2 * virus_width))
    return number_viruses_x

def get_number_rows(ai_settings, ship_height, virus_height):
    """Determines the number of rows with viruses that fits in teh screen"""
    available_space_y = (
        ai_settings.screen_height - (3 * virus_height) - ship_height
        )
    number_rows = int(available_space_y / (2 * virus_height))
    return number_rows

def create_virus(ai_settings, screen, viruses, virus_number, row_number):
    # Creates an virus and positions it on the line of the
    virus = Virus(ai_settings, screen)
    virus_width = virus.rect.width
    virus.x = virus_width + 2 * virus_width * virus_number
    virus.rect.y = virus.rect.height + 2 * virus.rect.height * row_number
    virus.rect.x = virus.x
    viruses.add(virus)
            
def create_fleet(ai_settings, screen, ship, viruses):
    """Creates a complete fleet of viruses"""
    # Creates and calculates the number of virus in a line
    virus = Virus(ai_settings, screen)
    number_viruses_x = get_number_viruses_x(ai_settings, virus.rect.width)
    number_rows = get_number_rows(ai_settings,
                                  ship.rect.height,
                                  virus.rect.height)
    
    # Creates the virus fleet
    for row_number in range(number_rows):
        for virus_number in range(number_viruses_x):
            create_virus(ai_settings, screen, viruses, virus_number, row_number)
            
def update_viruses(viruses):
    """Updates all viruses positions"""
    viruses.update()