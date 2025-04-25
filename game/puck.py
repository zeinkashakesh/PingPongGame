
import pygame
from config import *


def flash_screen(screen):
    flash_color = (255, 255, 255)
    screen.fill(flash_color)
    pygame.display.flip()
    pygame.time.delay(100)
class Puck:
    def __init__(self, screen, goal_sound):
        self.screen = screen
        self.goal_sound = goal_sound
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PUCK_RADIUS * 2, PUCK_RADIUS * 2)
        self.x_velocity = 5
        self.y_velocity = 5
        self.radius = PUCK_RADIUS



    def update(self, player, ai, player_score, ai_score):
        if player.rect.colliderect(self.rect):
            self.x_velocity = -self.x_velocity
            self.rect.x = player.rect.right

        if ai.rect.colliderect(self.rect):
            self.x_velocity = -self.x_velocity
            self.rect.x = ai.rect.left - self.rect.width

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.y_velocity = -self.y_velocity

        if self.rect.left <= 0:
            if self.goal_sound:
                self.goal_sound.play()
            flash_screen(self.screen)
            ai_score += 1
            self.reset()
        elif self.rect.right >= SCREEN_WIDTH:
            if self.goal_sound:
                self.goal_sound.play()
            flash_screen(self.screen)
            player_score += 1
            self.reset()

        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

        return player_score, ai_score

    def handle_collision(self, paddle):
        self.x_velocity *= -1
        if self.rect.centery < paddle.rect.centery:
            self.y_velocity -= 2
        else:
            self.y_velocity += 2

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 255), self.rect.center, self.radius)

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.x_velocity *= -1
        self.y_velocity = 5



