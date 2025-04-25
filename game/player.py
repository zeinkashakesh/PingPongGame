import pygame
from config import *
class Paddle:
    def __init__(self, x, y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT, is_ai=False, difficulty="hard"):
        self.rect = pygame.Rect(x, y, width, height)
        self.is_ai = is_ai
        self.difficulty = difficulty.lower()  # difficulty attribute: easy, medium, hard
        self.color = (0, 255, 100) if is_ai else (255, 60, 60) # AI = blue, player = red

    def move(self, move_up, move_down):
        # Handle player movement with boundaries
        if move_up and self.rect.top > 0:
            self.rect.y -= 5
        if move_down and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 5

    def update_ai(self, puck, ai_function):
        target_y = ai_function(self.rect, puck)

        if self.difficulty == "hard":
            # 🔥 Move directly to the target with zero tolerance
            self.rect.centery += (target_y - self.rect.centery) * 0.8  # fast smoothing

            # Optional: snap hard if it's close enough
            if abs(self.rect.centery - target_y) < 5:
                self.rect.centery = target_y

        else:
            # Other difficulty speeds
            if self.difficulty == "easy":
                speed = 2
            elif self.difficulty == "medium":
                speed = 10
            else:
                speed = 5

            if self.rect.centery < target_y:
                self.rect.centery += min(speed, target_y - self.rect.centery)
            elif self.rect.centery > target_y:
                self.rect.centery -= min(speed, self.rect.centery - target_y)

        # Clamp to arena bounds
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
