import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("white")
screen_width=800
screen_height=600
wn.setup(width=800, height=600)
wn.tracer(0)

# First paddle

first_pddl = turtle.Turtle()
first_pddl.speed(0)
first_pddl.shape("square")
first_pddl.color("black")
first_pddl.shapesize(stretch_wid=5, stretch_len=1)
first_pddl.penup()
first_pddl.goto(-350, 0)


# Second paddle

second_pddl = turtle.Turtle()
second_pddl.speed(0)
second_pddl.shape("square")
second_pddl.color("black")
second_pddl.shapesize(stretch_wid=5, stretch_len=1)
second_pddl.penup()
second_pddl.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6
ball.dy = -0.6


# Function

def first_pddl_up():
    y = first_pddl.ycor()
    y += 20
    first_pddl.sety(y)
    
def first_pddl_down():
    y = first_pddl.ycor()
    y -= 20
    first_pddl.sety(y)

def second_pddl_up():
    y = second_pddl.ycor()
    y += 20
    second_pddl.sety(y)
    
def second_pddl_down():
    y = second_pddl.ycor()
    y -= 20
    second_pddl.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(first_pddl_up, "w")
wn.onkeypress(first_pddl_down, "s")

wn.onkeypress(second_pddl_up, "Up")
wn.onkeypress(second_pddl_down, "Down")

#Main game loop

while True:
    wn.update()

    # Mode the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball hits the border
    if (ball.ycor() > (screen_height/2 - 10)):
        ball.sety((screen_height/2)-10)
        ball.dy *= -1
    
    if (ball.ycor() < (-(screen_height/2) + 10)):
        ball.sety(-(screen_height/2)+10)
        ball.dy *= -1

    if (ball.xcor() < -(screen_width/2)):
        ball.goto(0, 0)
        ball.dx *= -1
    
    if (ball.xcor() > (screen_width/2)):
        ball.goto(0, 0)
        ball.dx *= -1

    # Ball hits the paddle