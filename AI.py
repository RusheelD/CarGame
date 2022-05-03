from Car import Car
from pyglet.window import *
import random

class AI(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.move_directions = [key.UP, key.DOWN]
        self.turn_directions = [key.LEFT, key.RIGHT]
        self.moving = False
        self.turning = False
        self.move_direction = None
        self.turn_direction = None
        self.enabled = False
    
    def toggle_move(self):
        if(not(self.enabled)):
            self.moving = False
            self.turning = False
            return
        odds = random.randint(1, 100)

        if(self.moving):
            if(odds <= 2):
                self.move_stop(self.move_direction)
                self.moving = False
            elif(not(self.turning) and odds <= 60):
                self.turn_direction = random.choice(self.turn_directions)
                self.move_start(self.turn_direction)
                self.turning = True
            elif(odds >= 90):
                self.move_stop(self.turn_direction)
                self.turning = False
        elif(odds <= 90):
            move_odds = random.randint(1, 100)
            if(move_odds <= 90):
                self.move_direction = self.move_directions[0]
            else:
                self.move_direction = self.move_directions[1]
            self.move_start(self.move_direction)
            self.moving = True   
        