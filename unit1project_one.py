# unit1project_one.py
# by Allison Dixon
# Last modified September 17, 2019
#
# This program makes four different colored octagons

import turtle


# This function creates an octagon in color of choice
def make_an_octagon(color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.fd(50)
        turtle.rt(45)
    turtle.end_fill()


# This function makes turtle go to location of choice
def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# Makes a cyan filled octagon
go_to(-100, -100)
make_an_octagon("cyan")

# Makes a medium purple filled octagon in a new location
go_to(-100, 100)
make_an_octagon("medium purple")

# Makes a lavender filled octagon in a new location
go_to(100, 100)
make_an_octagon("lavender")

# Makes a dodger blue filled octagon in a new location
go_to(100, -100)
make_an_octagon("dodger blue")

# Program stays on screen until user clicks on screen
turtle.exitonclick()
