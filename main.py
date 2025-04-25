import pygame
from config import *
from game.player import Paddle
from game.puck import Puck
from game.arena import draw_arena, draw_score
from game.difficulty import select_difficulty
from AI.easy_ai import easy_ai
from AI.medium_ai import medium_ai
from AI.hard_ai import hard_ai


pygame.init()
pygame.mixer.init()

# Sounds
pygame.mixer.music.load("assets/Sound effects/background_music1.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

goal_sound = pygame.mixer.Sound("assets/Sound effects/goal.wav")

# Difficulty mapping
ai_fn = {
    "easy": easy_ai,
    "medium": medium_ai,
    "hard": hard_ai
}

# Main game loop
def game_loop(difficulty):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ai_function = ai_fn[difficulty]
    player = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ai = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, is_ai=True)
    ai.difficulty = difficulty
    puck = Puck(screen, goal_sound)

    player_score = 0
    ai_score = 0
    goal_flash_timer = 0
    winner = None
    running = True

    while running:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

       
        if puck.rect.x < 0:
            ai_score += 1
            puck.reset()
            goal_flash_timer = 20
            goal_sound.play()
        elif puck.rect.x > SCREEN_WIDTH:
            player_score += 1
            puck.reset()
            goal_flash_timer = 20
            goal_sound.play()

        
        goal_flash = goal_flash_timer > 0
        if goal_flash:
            goal_flash_timer -= 1

        
        if player_score >= 5:
            winner = "Player"
            running = False
        elif ai_score >= 5:
            winner = "AI"
            running = False

       
        draw_arena(screen, player_score, ai_score, goal_flash, winner if not running else None)
        draw_score(screen, player_score, ai_score)

        if running:
            keys = pygame.key.get_pressed()
            player.move(keys[pygame.K_w], keys[pygame.K_s])
            ai.update_ai(puck, ai_function)
            player_score, ai_score = puck.update(player, ai, player_score, ai_score)

            player.draw(screen)
            ai.draw(screen)
            puck.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()

    show_winner_menu(screen, winner, difficulty)


def show_winner_menu(screen, winner, difficulty):
    font = pygame.font.Font("assets/Orbitron-ExtraBold.ttf", 48)
    winner_text = font.render(f"{winner} Wins!", True, (0, 255, 255))
    screen.fill((10, 10, 30))
    screen.blit(winner_text, winner_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)))

    # Buttons
    button_font = pygame.font.Font("assets/Orbitron-ExtraBold.ttf", 36)

    replay_text = button_font.render("Replay", True, (0, 0, 0))
    replay_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 60)

    quit_text = button_font.render("Quit", True, (0, 0, 0))
    quit_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 80, 200, 60)

    pygame.draw.rect(screen, (0, 255, 100), replay_rect, border_radius=10)
    screen.blit(replay_text, replay_text.get_rect(center=replay_rect.center))

    pygame.draw.rect(screen, (255, 60, 60), quit_rect, border_radius=10)
    screen.blit(quit_text, quit_text.get_rect(center=quit_rect.center))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if replay_rect.collidepoint(event.pos):
                    game_loop(difficulty)
                    waiting = False
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()


#MAIN FUNCTION
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    difficulty = select_difficulty(screen)
    game_loop(difficulty)

if __name__ == "__main__":
    main()
