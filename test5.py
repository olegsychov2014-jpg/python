import time
import turtle as t
def change_position(x,y):
    t.speed(100)
    t.penup()
    t.goto(x=x, y=y)
    t.pendown()
def three():
    t.left(90)
    t.color("red4")
    t.forward(40)
    t.right(90)
    t.begin_fill()
    t.color("green")
    t.circle(30)
    t.end_fill()
def peramida(colir,vidstan):
    t.speed(100)
    t.begin_fill()
    t.forward(vidstan)
    t.left(120)
    t.forward(vidstan)
    t.left(120)
    t.forward(vidstan)
    t.left(120)
    t.color(colir)
    t.end_fill()
def ptax(color):
    t.right(40)
    t.color(color)
    t.forward(50)
    t.left(80)
    t.forward(50)
    t.right(35)

three()
# t.left(180)
change_position(x=-200,y=30)
three()
change_position(x=-250,y=-20)
three()
change_position(x=-200,y=-35)
peramida("gray",vidstan=120)
change_position(x=200,y=-10)
peramida("red",vidstan=340)
change_position(x=-450,y=50)
peramida("blue",vidstan=500)
change_position(x=350,y=-100)
ptax("red")
change_position(x=-30,y=25)
ptax("blue")
change_position(x=-50,y=25)
ptax("yellow")
t.done()


#     t.circle(20)
# change_position(x=-10,y=-50)
# t.right(90)
# t.forward(30)
# t.done()





