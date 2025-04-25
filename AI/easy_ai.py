import random
from config import *

def easy_ai(paddle_rect, puck):
 
    return puck.rect.centery + random.randint(-50, 50)
