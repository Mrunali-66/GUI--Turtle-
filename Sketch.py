from turtle import Turtle,Screen

draw=Turtle()
screen=Screen()

def move_forward():
    draw.forward(10)

def move_backward():
    draw.backward(10)


def move_left():
    new_heading=draw.heading()+10
    draw.setheading(new_heading)

def move_right():
    new_heading=draw.heading()+10
    draw.setheading(new_heading)

def move_right():
    new_heading=draw.heading()-10
    draw.setheading(new_heading)

def clear():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()

screen.listen()
screen.onkey(move_forward,"1")
screen.onkey(move_backward,"2")
screen.onkey(clear,"c")
screen.onkey(move_left,"3")
screen.onkey(move_right,"4")

screen.exitonclick()