import pyglet
from pyglet.window import *

class Car(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity= 0.0
        self.max_velocity = 1500.0
        self.rotate_speed = 200.0
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.enabled = False
    
    def update(self, dt):
        if self.velocity > self.max_velocity:
            self.velocity = self.max_velocity
        elif self.velocity < -1 * self.max_velocity:
            self.velocity = -1 * self.max_velocity

        angle_radians = -math.radians(self.rotation)
        self.x += math.cos(angle_radians) * self.velocity * dt
        self.y += math.sin(angle_radians) * self.velocity * dt
        
        if self.keys['up']:
            self.velocity = self.max_velocity
        if self.keys['down']:
            self.velocity = -1 * self.max_velocity
        if self.keys['left'] and self.velocity != 0:
            self.rotation -= self.rotate_speed * dt * (self.velocity / abs(self.velocity))
        if self.keys['right'] and self.velocity != 0:
            self.rotation += self.rotate_speed * dt * (self.velocity / abs(self.velocity))
        

    def on_key_press(self, symbol, modifiers):
        if(symbol == key.I):
            self.enabled = True
        elif(symbol == key.O):
            self.enabled = False
            for s in [key.UP, key.DOWN, key.LEFT, key.RIGHT]:
                self.move_stop(s)
        else:
            self.move_start(symbol)

    def on_key_release(self, symbol, modifiers):
        if(symbol == key.I):
            self.enabled = True
        elif(symbol == key.O):
            self.enabled = False
        else:
            self.move_stop(symbol)

    def move_start(self, symbol):
        if symbol == key.UP or symbol == key.W:
            self.keys['up'] = True
            self.drag = 0
        elif symbol == key.DOWN or symbol == key.S:
            self.keys['down'] = True
        elif symbol == key.LEFT or symbol == key.A:
            self.keys['left'] = True
        elif symbol == key.RIGHT or symbol == key.D:
            self.keys['right'] = True
        elif symbol == key.SPACE:
            self.velocity = 0

    def move_stop(self, symbol):
        if symbol == key.UP or symbol == key.W:
            self.keys['up'] = False
            self.velocity = 0
        elif symbol == key.DOWN or symbol == key.S:
            self.keys['down'] = False
            self.velocity = 0
        elif symbol == key.LEFT or symbol == key.A:
            self.keys['left'] = False
        elif symbol == key.RIGHT or symbol == key.D:
            self.keys['right'] = False

    def toggle_move(self):
        return
        
    