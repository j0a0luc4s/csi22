import turtle
import time

def draw_spiral(t, n, sz, theta):
    for i in range(n):
       t.forward(i*sz)
       t.right(theta)

wn = turtle.Screen()
tess = turtle.Turtle()

wn.bgcolor("lightgreen")
tess.pencolor("blue")
tess.fillcolor("blue")
tess.pensize("2")

draw_spiral(tess, 100, 2, 90)
time.sleep(5)
wn.resetscreen()
draw_spiral(tess, 100, 2, 89)

wn.mainloop()
