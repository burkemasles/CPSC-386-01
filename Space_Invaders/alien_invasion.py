import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from scoreboard import Scoreboard
from start_screen import Start_Screen
from random import randint
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Space Invaders")

    play_button = Button(screen, "Play", screen_rect.centerx, screen_rect.centery)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()
    alien_bullets = Group()

    ss = Start_Screen(ai_settings, screen)

    gf.prep_start(ss)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    random_tick = pygame.time.get_ticks() + randint(500, 1200)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets, ss.button, ss)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
            if pygame.time.get_ticks() >= random_tick:
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, True, alien_bullets)
                random_tick = pygame.time.get_ticks() + randint(500, 1200)
            else:
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, False, alien_bullets)
            gf.update_screen(ai_settings, screen, stats, sb,
                             ship, aliens, bullets, play_button, alien_bullets)
            if ai_settings.sound_counter <= 0:
                ai_settings.sound.play()
                ai_settings.sound_counter = ai_settings.sound_counter_reset
            else:
                ai_settings.sound_counter -= 1
        elif not stats.high_score_screen_active:
            gf.update_start_screen(screen, ai_settings, play_button, ss)
        else:
            gf.update_high_score_screen(ss, screen, ai_settings, stats)


run_game()
