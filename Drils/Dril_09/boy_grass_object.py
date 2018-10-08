from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Ball21x21:
    def __init__(self):
        self.x, self.y = random.randint(40, 700), 600
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > 60:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41x41:
    def __init__(self):
        self.x, self.y = random.randint(40, 700), 600
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(5, 20)

    def update(self):
        if self.y > 70:
            self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
random_create = random.randint(1, 19)
boy = Boy()
team = [Boy() for i in range(11)]
balls21 = Ball21x21()
balls41 = Ball41x41()
balls21t = [Ball21x21() for i in range(random_create)]
balls41t = [Ball41x41() for i in range(20 - random_create)]
grass = Grass()
running = True


# game main loop code
while running:
    handle_events()
    for boy in team:
        boy.update()
    for balls21 in balls21t:
        balls21.update()
    for balls41 in balls41t:
        balls41.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for balls21 in balls21t:
        balls21.draw()
    for balls41 in balls41t:
        balls41.draw()
    update_canvas()
    delay(0.05)


# finalization code
close_canvas()