import heapq
from config import *

def a_star_pathfinding(start_y, target_y, step=10):
    heap = [(0, start_y)]
    visited = set()

    while heap:
        cost, current_y = heapq.heappop(heap)
        if abs(current_y - target_y) <= step:
            return target_y
        if current_y in visited:
            continue
        visited.add(current_y)

        for direction in [-step, step]:
            next_y = current_y + direction
            if 0 <= next_y <= SCREEN_HEIGHT:
                priority = abs(next_y - target_y)
                heapq.heappush(heap, (priority, next_y))

    return start_y

def hard_ai(paddle_rect, puck):
    prediction_offset = 0.6 * puck.x_velocity  # further ahead
    target_y = puck.rect.centery + prediction_offset
    return a_star_pathfinding(paddle_rect.centery, target_y)

