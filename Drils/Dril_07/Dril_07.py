from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global cx, cy
    global mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x - 50, KPU_HEIGHT - 1 - event.y + 50
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_character(p1, p2):
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    for i in range(0, 100+1, 2):
        frame = 0
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        if p2[0] > p1[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        elif p2[0] < p1[0]:
            character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        update_canvas()
        delay(0.02)

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
i = 0

size = 20
points = [(random.randint(-500, 500), random.randint(-350, 350)) for i in range(size)]
n = 1
while running:
    move_character(points[n-1], points[n])
    n = (n + 1) % size
    handle_events()
close_canvas()




