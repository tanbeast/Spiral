import turtle
colors = ["red", "purple","blue","green","orange","yellow","white"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
    my_pen.pencolor(colors[x %7])
    my_pen.width(x/950+3)
    my_pen.forward(x/1)
    my_pen.left(30)
