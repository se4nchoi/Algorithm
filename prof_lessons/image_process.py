# turtle
from turtle import *
from math import sin, cos, pi


setup(800, 800)
speed(1500)
pencolor('green')
width(5)

up(); goto(200, 0); down()

for a in range(0,730, 720//5):
    ## FILLING IN THE COS X SINE CURVE INTERSECT
    # s = sin(a*pi/180)
    # c = cos(3*a*pi/180)   # converting to radian
    # # matching phase and period for turtle window display
    # # 진폭과 위상 맞추기
    # x = a * 600 / 360 - 300
    # ys = s * 200
    # yc = c * 200
        
    # up(); goto(x,ys); down(); goto(x,yc)
    
    x = 200 * cos(a*pi/180)
    y = 200 * sin(a*pi/180)
    goto(x,y)

hideturtle()
done()



# tkinter
#  

