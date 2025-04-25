from config import *

def dfs_pathfinding(start_y, target_y, step=10, visited=None, max_depth=50, depth=0):
    if visited is None:
        visited = set()

    if depth > max_depth or abs(start_y - target_y) <= step or start_y in visited:
        return target_y

    visited.add(start_y)

    if start_y < target_y:
        return dfs_pathfinding(start_y + step, target_y, step, visited, max_depth, depth + 1)
    else:
        return dfs_pathfinding(start_y - step, target_y, step, visited, max_depth, depth + 1)

def medium_ai(paddle_rect, puck):
    return dfs_pathfinding(paddle_rect.centery, puck.rect.centery)
