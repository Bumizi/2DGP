import game_framework
from pico2d import *
import main_state


name = "PauseState"
image = None
blink_time = 0.0
blink = None


def enter():
    global image
    global blink
    blink = False
    image = load_image('pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    global is_pause
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()
                pass

    pass


def draw():
    global blink
    clear_canvas()
    if blink:
        image.draw(400, 300)
    main_state.grass.draw()
    main_state.boy.draw()
    update_canvas()
    pass


def update():
    global blink_time
    global blink
    if blink_time > 1.0:
        blink_time = 0
        if blink:
            blink = False
        else:
            blink = True
    delay(0.01)
    blink_time += 0.01
    pass


def pause():
    pass


def resume():
    pass






