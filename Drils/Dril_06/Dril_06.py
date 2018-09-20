from pico2d import *

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
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
i = 0
cx = 100
cy = 90
dir = 0
mx, my = 0, 0
character.clip_draw(frame * 100, 300 * 1, 100, 100, x, 90)
hide_cursor()

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    dif_x = (mx - cx) / 40
    dif_y = (my - cy) / 40

    if dif_x > 0:
        dir = 1
    elif dif_x < 0:
        dir = -1

    cx += dif_x
    cy += dif_y

    if dir > 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
    elif dir < 0:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, cx, cy)
    elif dir == 0:
        character.clip_draw(frame * 100, 300 * 1, 100, 100, cx, cy)

    cursor.clip_draw(0, 0, 100, 100, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()




