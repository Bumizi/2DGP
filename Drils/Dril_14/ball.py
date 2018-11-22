import random
from pico2d import *

import game_world
import game_framework

toss_x, toss_y = 0, 0


class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y = random.randint(0, 1800-1), random.randint(0, 1100-1)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx = self.x - self.bg.window_left
        cy = self.y - self.bg.window_bottom
        self.image.draw(cx, cy)
        #self.image.draw(self.cx, self.cy)

        #draw_rectangle(*self.get_bb())

    def set_background(self, bg):
        self.bg = bg
        #self.x = self.bg.w / 2
        #self.y = self.bg.h / 2

    def update(self):
        #self.x -= toss_x
        #self.y -= toss_y
        #cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        #print('x :', Boy.x_velocity, 'y:', Boy.y_velocity, ' Frame Time:' + str(game_framework.frame_time))
        #self.y -= self.fall_speed * game_framework.frame_time
        pass

