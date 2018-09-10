from pico2d import *
from math import *
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
#state가 1이면 사각형, 0이면 원
state=1
#direction이 1이면 아래, 2는 우, 3은 위, 4는 좌
direction=1
x=400
y=90
r=270
grass.draw_now(400, 30)
character.draw_now(x, y)
while(True):
    if(state==1):
        if(direction==1):
            x=x+2
            if(x==780):
                direction=2
            elif(x==398):
                escape=y
                state=0
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x,y)
            delay(0.01)
        elif(direction==2):
            y=y+2
            if(y==560):
                direction=3
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x,y)
            delay(0.01)
        elif(direction==3):
            x=x-2
            if(x==18):
                direction=4
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x,y)
            delay(0.01)
        elif(direction==4):
            y=y-2
            if(y==90):
                direction=1
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x,y)
            delay(0.01)
    elif(state==0):
        angle=math.radians(r)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        x=x+4*sin(angle)
        y=y+4*cos(angle)
        r=r+1
        if(398<x):
            if(y<92):
                state=1
                x=400
                y=90
                r=270
        delay(0.01)


