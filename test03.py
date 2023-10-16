from turtle import *
speed(0)
hideturtle()

def line(sx,sy,dx,dy):
    up()
    goto(sx,sy)
    down()
    goto(dx,dy)

sx = 0
sy = 200
dx = 10
dy = 0
while dx <= 200:
    line(sx,sy,dx,dy)
    sy = sy - 10
    dx = dx + 10

done()
