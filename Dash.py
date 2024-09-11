import turtle
import turtle as t


tim = t.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")

for _ in range(125):
    tim.forward(100)
    tim.color("pink")
    tim.penup()
    tim.forward(100)
    tim.pendown()
    tim.right(90)
    tim.speed("fastest")

    tim.forward(20)
    tim.color("sky blue")
    tim.penup()
    tim.forward(20)
    tim.pendown()
    tim.right(90)
    tim.speed("fastest")


    tim.forward(120)
    tim.color("light green")
    tim.penup()
    tim.forward(120)
    tim.pendown()
    tim.right(200)
    tim.forward(30)
    tim.speed("fastest")

    tim.forward(120)
    tim.color("white")
    tim.penup()
    tim.forward(120)
    tim.pendown()
    tim.right(160)
    tim.forward(150)
    tim.speed("fastest")

    tim.forward(120)
    tim.color("white")
    tim.penup()
    tim.forward(120)
    tim.pendown()
    tim.right(280)
    tim.forward(90)
    tim.speed("fastest")



screen.exitonclick()







