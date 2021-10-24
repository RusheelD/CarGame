import pyglet
from Car import *

window = pyglet.window.Window(1400, 800)

background = pyglet.image.SolidColorImagePattern((255,255,255,255)).create_image(window.width,window.height)

#car_image = pyglet.image.SolidColorImagePattern((255,0,0,255)).create_image(60,30)
car_number = 1
car_image = pyglet.image.load('car' + str(car_number) + '.png')
car_image.anchor_x = int(car_image.width / 2)
car_image.anchor_y = int(car_image.height / 2)
car = Car(car_image)
car.scale = 0.2
car.rotation -= 90
car.x = window.width / 2
car.y = window.height / 2

window.push_handlers(car)

@window.event
def on_draw():
    window.clear()
    background.blit(0,0)
    car.draw()

def update(dt):
    car.update(dt)
    if(car.x > window.width or car.x < 0):
        car.x = car.x % window.width
    if(car.y > window.height or car.y < 0):
        car.y = car.y % window.height

pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()