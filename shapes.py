import turtle
turtle.speed(0)
turtle.pencolor("green")
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)

turtle.penup()
turtle.forward(200)
turtle.pencolor("purple")
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.forward(200)
turtle.pencolor("red")
turtle.pendown()

for x in range(5):
    turtle.forward(50)
    turtle.left(72)

turtle.penup()
turtle.forward(140)
turtle.pencolor("blue")
turtle.pendown()

turtle.circle(20)

turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.pencolor("orange")
turtle.pendown()

for x in range(5):
    turtle.forward(80)
    turtle.right(144)

turtle.penup()
turtle.forward(200)
turtle.pencolor("pink")
turtle.pendown()

for x in range (4):
    turtle.forward(60)
    turtle.right(90)
turtle.right(30)
for x in range (4):
    turtle.forward(60)
    turtle.right(90)
turtle.right(30)
for x in range (4):
    turtle.fd(60)
    turtle.right(90)
turtle.right(30)
for x in range (4):
    turtle.fd(60)
    turtle.right(90)
turtle.right(30)
for x in range(4):
    turtle.fd(60)
    turtle.right(90)

turtle.penup()
turtle.goto(-100,100)
turtle.rt(60)
turtle.pencolor("turquoise")
turtle.pendown()

for x in range(4):
    turtle.fd(50)
    turtle.lt(120)
turtle.rt(90)
for x in range(3):
    turtle.fd(50)
    turtle.lt(90)

turtle.penup()
turtle.goto(300,300)
turtle.pencolor("black")
turtle.rt(300)
turtle.pendown()

turtle.color("red")
turtle.begin_fill()
for x in range(4):
    turtle.fd(50)
    turtle.lt(120)
turtle.end_fill()
turtle.rt(90)
turtle.color("purple")
turtle.begin_fill()
for x in range(3):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()

turtle.penup()
turtle.goto(220,300)
turtle.seth(240)
turtle.pendown()

turtle.color("red")
turtle.begin_fill()
for x in range(4):
    turtle.fd(50)
    turtle.lt(120)
turtle.end_fill()
turtle.rt(90)
turtle.color("purple")
turtle.begin_fill()
for x in range(3):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()

turtle.penup()
turtle.goto(140,300)
turtle.seth(240)
turtle.pendown()

turtle.color("red")
turtle.begin_fill()
for x in range(4):
    turtle.fd(50)
    turtle.lt(120)
turtle.end_fill()
turtle.rt(90)
turtle.color("purple")
turtle.begin_fill()
for x in range(3):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()

turtle.penup()
turtle.goto(60,300)
turtle.seth(240)
turtle.pendown()

turtle.color("red")
turtle.begin_fill()
for x in range(4):
    turtle.fd(50)
    turtle.lt(120)
turtle.end_fill()
turtle.rt(90)
turtle.color("purple")
turtle.begin_fill()
for x in range(3):
    turtle.fd(50)
    turtle.lt(90)
turtle.end_fill()

turtle.penup()
turtle.goto(250,-200)
turtle.rt(60)
turtle.pendown()

def make_a_house(color, color2):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(3):
        turtle.fd(50)
        turtle.lt(120)
    turtle.end_fill()
    turtle.lt(60)
    turtle.color(color2)
    turtle.begin_fill()
    for y in range(3):
        turtle.fd(50)
        turtle.lt(90)
    turtle.end_fill()


def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


make_a_house("cyan", "medium purple")
go_to(180, -200)
turtle.lt(30)
make_a_house("indigo", "powder blue")
go_to(110, -200)
turtle.lt(30)
make_a_house("hot pink", "yellow")
go_to(35, -200)
turtle.lt(30)
make_a_house("green", "blue")


turtle.exitonclick()
