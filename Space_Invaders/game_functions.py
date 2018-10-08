import sys
import time
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from random import randint
from alien_bullet import Alien_Bullet
from scoreboard import Scoreboard


def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets):
    """Respond to ship being hit by alien"""
    if stats.ships_left > 0:
        stats.ships_left -= 1

        sb.prep_ships()

        n = 0
        while n <= 6:
            ship.destroy_ship()
            ship.blitme()
            pygame.display.flip()
            sleep(0.2)
            n += 1

        ship.reset_ship()
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        ai_settings.sound_counter_reset = 200

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, high_score_button, ss):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)
            check_high_score_button(stats, mouse_x, mouse_y, high_score_button, ss)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                      aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_high_score_button(stats, mouse_x, mouse_y, high_score_button, ss):
    button_clicked = high_score_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ss.prep_high_score_screen(stats)
        stats.high_score_screen_active = True


def update_high_score_screen(ss, screen, ai_settings, stats):
    screen.fill(ai_settings.start_color)
    ss.show_high_score_screen()
    pygame.display.flip()
    time.sleep(3)
    stats.high_score_screen_active = False


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        high_score_file = open('high_score.txt', 'w')
        high_score_file.write(str(stats.high_score))
        high_score_file.close()
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, alien_bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for alien_bullet in alien_bullets.sprites():
        alien_bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    sb.show_score()

    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    """Update position of bullets and get rid of old bullets"""
    bullets.update()
    alien_bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    for alien_bullet in alien_bullets.copy():
        if alien_bullet.rect.top >= screen.get_rect().bottom:
            alien_bullets.remove(alien_bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  ship, aliens, bullets)
    check_alien_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)


def check_alien_bullet_ship_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    collisions = pygame.sprite.spritecollideany(ship, alien_bullets)

    if collisions:
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  ship, aliens, bullets):
    """Respond to bullet-alien collisions"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            for x in aliens:
                stats.score += ai_settings.alien_points * (x.alien_type + 1)
                # * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (8 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number, alien_type):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen, alien_type)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    alien = Alien(ai_settings, screen, 0)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, number_rows - row_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        alien.change_sprite()
    if ai_settings.sound_counter_reset >= 0:
        ai_settings.sound_counter_reset -= 10
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, random_shot, alien_bullets):
    """Update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if random_shot:
        alien_list = aliens.sprites()
        new_bullet = Alien_Bullet(ai_settings, screen, alien_list[randint(0, len(aliens) - 1)])
        alien_bullets.add(new_bullet)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets, alien_bullets)


def check_high_score(stats, sb):
    """Check to see if there's a new high score"""
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_start_screen(screen, ai_settings, play_button, ss):
    """Initial start screen"""
    screen.fill(ai_settings.start_color)
    play_button.draw_button()
    ss.show_start_screen()
    pygame.display.flip()


def prep_start(ss):
    ss.prep_title()
    ss.prep_small_alien()
    ss.prep_medium_alien()
    ss.prep_big_alien()
    ss.prep_alien_scores()
    ss.prep_high_score_button()
