import turtle

def squares(alex, n):
    alex.penup()
    alex.forward(10)
    alex.left(90)
    alex.forward(10)
    alex.right(90)

    for i in range(n):
        for j in range(4):
            alex.pendown()
            alex.forward(20*(n-i))
            alex.left(90)
        alex.penup()
        alex.forward(10)
        alex.left(90)
        alex.forward(10)
        alex.right(90)
    alex.right(90)
    alex.forward(10*n)
    alex.right(90)
    alex.forward(10*n)
    alex.left(90)
    alex.forward(10)
    alex.right(90)
    alex.forward(10)
    alex.right(180)

wn = turtle.Screen()
alex = turtle.Turtle()

wn.bgcolor("lightgreen")
alex.pencolor("pink")
alex.fillcolor("pink")
alex.pensize("3")

squares(alex, 5)


wn.mainloop()
