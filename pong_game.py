import turtle
import os

wn= turtle.Screen()
wn.title("Pong by UTKARSH")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



#paddleA
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddleB
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Function
def paddle_a_up():
    y= paddle_a.ycor()
    y+= 20
    paddle_a.sety()

def paddle_a_down():
    y= paddle_a.ycor()
    y-= 20
    paddle_a.sety()

def paddle_b_up():
    y= paddle_b.ycor()
    y+= 20
    paddle_b.sety()

def paddle_b_down():
    y= paddle_b.ycor()
    y-= 20
    paddle_b.sety()


#keyboard binding


#Main game loop
while True:
    wn.update()