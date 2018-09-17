from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

Point_List = [[203, 535], [132, 243], [535, 470], [477, 203], [715, 136], [316, 225], [510, 92],
              [692, 518], [682, 336], [712, 349]]

i = 0
x = 0
y = 0
direction = 0
frame = 0
dif_x = 0
dif_y = 0

def move_right_face():
    x = 0
    frame = 0
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()
    pass
def move_left_face():
    x = 0
    frame = 0
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x -= 5
    delay(0.05)
    get_events()
    pass

def move_point_to_point():
    x, y = Point_List[i]
    dif_x=(Point_List[i][1]-Point_List[i][1])
    dif_y=(Point_List[i+1][1]-Point_List[i+1][1])
    distance = math.sqrt((dif_x**2)+(dif_y**2)) / 40
    pass

while True:
     clear_canvas_now()
     grass.draw_now(400, 30)
     character.draw_now(Point_List[i][0], Point_List[i][1])
     move_point_to_point()
     if dif_x > 0:
         move_right_face()
     elif dif_x < 0:
         move_left_face()
    
close_canvas()
