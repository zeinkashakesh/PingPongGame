import pygame
from config import *



#ARENA SHOW
def draw_arena(screen, player_score, ai_score, flash=False, winner=None):
    if flash:
        screen.fill((255, 255, 255))  
    else:
        screen.fill((10, 10, 30))  

    pygame.draw.line(screen, (0, 255, 255), (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 2)
    pygame.draw.circle(screen, (255, 0, 255), (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 40, 2)
    if winner:
        font= pygame.font.SysFont("comicsansms", 48)
        win_text= font.render(f"{winner} Wins!", True, (255, 255, 255))
        screen.blit(win_text, win_text.get_rect(center=(SCREEN_WIDTH // 2, 200)))


#
def draw_score(screen, player_score, ai_score):
    font= pygame.font.SysFont("Consolas", 64, bold=True)
    score_text= f"{player_score}    |    {ai_score}"

    glow_color= (255, 20, 147)     
    main_color= (0, 255, 255)      
    text_surface= font.render(score_text, True, main_color)
    glow_surface= font.render(score_text, True, glow_color)
    text_rect= text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    for offset in [(-3, -3), (3, -3), (-3, 3), (3, 3)]:
        glow_rect= text_rect.move(offset)
        screen.blit(glow_surface, glow_rect)

    screen.blit(text_surface, text_rect)

