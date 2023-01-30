from turtle import *
import math
#import turtle module for 2D graphics. extremely simple and for beginners kinda trash but whatever lol
#means you dont have to use turtle. for methods
#canvas stays open
#turtle gives you a cursor, when moved, it draws a line like forward(100) moves it 100 pixels forward
#left(90) turns relative to current position
#give user options and draw math equations?

 #makes it instant, change later, 1 is slowest


def tree(size, levels, angle):
    color("brown")
    if levels == 0:    #Basecase
        color("green")
        dot(size)
        color("black")
        return
    #right branch
    forward(size)
    right(angle)
    tree(size * 0.8, levels - 1, angle)
    #left, angle x2 brings you to middle, then opposite
    left(angle * 2)
    tree(size * 0.8, levels - 1, angle)
    right(angle) #recenters
    backward(size) #return to starting point

#left(90) #ensures graph starts going up
#tree(90, 8, 30)


def i(size):
    color("red")
    left(90)
    forward(size)
    left(90)
    forward(size/2)
    right(180)
    forward(size)
    left(180)
    forward(size/2)
    left(90)
    forward(size)
    right(90)
    forward(size/2)
    left(180)
    forward(size)

def l(size):
    color("red")
    left(90)
    forward(size)
    left(180)
    forward(size)
    left(90)
    forward(size/1.5)

def o(size):
    color("red")
    left(90)
    penup()
    forward(size)
    right(90)
    pendown()
    makecircle()


def makecircle():
    counter = 0
    while(counter < 360):
        right(1)
        forward(1)
        counter += 1


def v(size):
    color("red")
    left(110)
    forward(size)
    backward(size)
    right(40)
    forward(size)
    backward(size)
    right(70)

def e(size):
    color("red")
    left(90)
    forward(size)
    right(90)
    forward(size/1.2)
    backward(size/1.2)
    right(90)
    forward(size/2)
    left(90)
    forward(size/1.8)
    backward(size/1.8)
    right(90)
    forward(size/2)
    left(90)
    forward(size/1.2)


def y(size):
    color("red")
    size = size / 2
    left(90)
    forward(size)
    left(20)
    forward(size)
    backward(size)
    right(40)
    forward(size)
    backward(size)
    left(20)
    backward(size)
    right(90)


def u(size):
    color("red")
    i = 0
    left(90)
    penup()
    forward(size)
    left(90)
    forward(size/2)
    pendown()
    left(90)
    forward(size/2)
    makehalfcircle()
    forward(size/2)


def makehalfcircle():
    counter = 0
    while counter < 183:
        left(1)
        forward(1)
        counter += 1


def drawdots(length):
    i = 0
    while i < length:
        color("black")
        forward(20)
        dot(20)
        i += 1


delay(1)
left(3960)
delay(0)
speed(0)
penup()
left(180)
forward(550)
left(90)
forward(200)
right(90)
right(180)
pendown()
i(100)
penup()
forward(100)
pendown()
l(100)
penup()
forward(60)
left(90)
forward(10)
right(90)
pendown()
o(100)
penup()
forward(100)
right(90)
forward(105)
left(90)
pendown()
v(100)
penup()
forward(50)
right(90)
forward(5)
left(90)
pendown()
e(90)
penup()
forward(80)
pendown()
y(100)
penup()
forward(90)
pendown()
left(90)
forward(5)
right(90)
o(100)
penup()
forward(120)
right(90)
forward(100)
left(90)
right(90)
forward(9)
left(90)
u(100)
left(90)
penup()
forward(500)
right(90)
forward(180)
right(90)
left(90)
pendown()
tree(100, 6, 30)
penup()
right(180)
forward(115)
right(92)

mainloop()
