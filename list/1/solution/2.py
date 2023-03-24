import turtle

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz);
        t.left(360/n);

wn = turtle.Screen()
tess = turtle.Turtle()

wn.bgcolor("lightgreen")
tess.pencolor("pink")
tess.fillcolor("pink")
tess.pensize("3")

draw_poly(tess, 8, 50)

wn.mainloop()
