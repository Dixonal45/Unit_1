# unit1project_one.py
# by Allison Dixon
# Last modified September 16, 2019
#
# This program makes four different colored octagons

import turtle


# Creates an octagon
def make_an_octagon():
    for x in range(8):
        turtle.fd(50)
        turtle.rt(45)


# Makes turtle go to set location
def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# Makes a cyan filled octagon
go_to(-100, -100)
turtle.color("cyan")
turtle.begin_fill()
make_an_octagon()
turtle.end_fill()

# Makes a medium purple filled octagon in a new location
go_to(-100, 100)
turtle.color("medium purple")
turtle.begin_fill()
make_an_octagon()
turtle.end_fill()

# Makes a lavender filled octagon in a new location
go_to(100, 100)
turtle.color("lavender")
turtle.begin_fill()
make_an_octagon()
turtle.end_fill()

# Makes a dodger blue filled octagon in a new location
go_to(100, -100)
turtle.color("dodger blue")
turtle.begin_fill()
make_an_octagon()
turtle.end_fill()

# Program stays on screen until user clicks on screen
turtle.exitonclick()
