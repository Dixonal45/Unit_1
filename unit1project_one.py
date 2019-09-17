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


# The following lines draw octagons in new locations and colors
go_to(-100, -100)
make_an_octagon("cyan")

go_to(-100, 100)
make_an_octagon("medium purple")

go_to(100, 100)
make_an_octagon("lavender")

go_to(100, -100)
make_an_octagon("dodger blue")

# The program stays on screen until the user clicks on screen
turtle.exitonclick()
