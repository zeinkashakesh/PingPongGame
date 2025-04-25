import pygame
from config import *


#DIFFICULTY SELECTION SCREEN
# This function displays a screen where the user can select the AI difficulty level.
def select_difficulty(screen):
    font = pygame.font.Font(None, 40)
    title_font = pygame.font.Font(None, 60)
    title = title_font.render("SELECT AI DIFFICULTY", True, (0, 255, 255))

    puck_radius = 60
    center_x =SCREEN_WIDTH //2
    center_y =SCREEN_HEIGHT //2
    gap =170

    buttons= [
        {"label":"EASY","color":(0,255,255),"pos":(center_x - gap,center_y),"value":"easy"},
        {"label":"MEDIUM","color":(255, 0, 255),"pos":(center_x, center_y),"value":"medium"},
        {"label":"HARD","color":(0, 255,0),"pos": (center_x + gap,center_y),"value": "hard"}
    ]
    #mute button
    mute_button_pos = (SCREEN_WIDTH - 60, 30)
    is_music_playing = True

    #mute 
    mute_icon= pygame.image.load("assets/mute.png").convert_alpha()
    unmute_icon= pygame.image.load("assets/volume-up.png").convert_alpha()
    mute_icon= pygame.transform.scale(mute_icon, (40, 40))
    unmute_icon= pygame.transform.scale(unmute_icon, (40, 40))

    clock= pygame.time.Clock()

    while True:
        screen.fill((10, 10, 30))  
        screen.blit(title,(center_x-title.get_width()// 2, 40))

        mouse_pos= pygame.mouse.get_pos()

        for btn in buttons:
            x,y= btn["pos"]
            color=btn["color"]
            dx=mouse_pos[0] - x
            dy=mouse_pos[1] - y
            dist_sq=dx * dx + dy * dy
            is_hovered= dist_sq <=(puck_radius + 20)**2

            if is_hovered:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), puck_radius + 10, 3)

            pygame.draw.circle(screen,(0, 0, 0),(x + 4, y + 4), puck_radius + 2)  # Shadow
            pygame.draw.circle(screen, color, (x, y), puck_radius)

            label_surface=font.render(btn["label"], True, (0, 0, 0))
            screen.blit(label_surface,(x-label_surface.get_width() // 2, y-label_surface.get_height() // 2))

        # Mute icon in top right
        icon= mute_icon if is_music_playing else unmute_icon
        screen.blit(icon, mute_button_pos)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Click on difficulty
                for btn in buttons:
                    x, y= btn["pos"]
                    dx= mouse_pos[0] - x
                    dy= mouse_pos[1] - y
                    if dx * dx + dy * dy <= puck_radius ** 2:
                        return btn["value"]

                # Click on mute
                mute_dx= mouse_pos[0] - mute_button_pos[0]
                mute_dy= mouse_pos[1] - mute_button_pos[1]
                if 0 <= mute_dx <= 40 and 0 <= mute_dy <= 40:
                    if is_music_playing:
                        pygame.mixer.music.pause()
                        is_music_playing = False
                    else:
                        pygame.mixer.music.unpause()
                        is_music_playing = True

        clock.tick(60)
