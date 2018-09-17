from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

Point_List = [[203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92],
              [692, 518], [682, 336], [712, 349], [203, 535]]


def move_right_face(dif_x, dif_y, i):
    x = Point_List[i][0]
    y = Point_List[i][1]
    frame = 0
    j = 0
    while j != 40:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += dif_x
        y += dif_y
        j += 1
        delay(0.05)
        get_events()


def move_left_face(dif_x, dif_y, i):
    x = Point_List[i][0]
    y = Point_List[i][1]
    frame = 0
    j = 0
    while j != 40:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += dif_x
        y += dif_y
        j += 1
        delay(0.05)
        get_events()


def move_point_to_point(i):
    dif_x = (Point_List[i+1][0]-Point_List[i][0]) / 40
    dif_y = (Point_List[i+1][1]-Point_List[i][1]) / 40
    if dif_x > 0:
        move_right_face(dif_x, dif_y, i)
    elif dif_x < 0:
        move_left_face(dif_x, dif_y, i)


i = 0

while True:
    move_point_to_point(i)
    if i < 9:
     i += 1
    elif i >= 9:
     i = 0
