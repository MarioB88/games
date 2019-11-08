import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("white")
screen_width=800
screen_height=600
wn.setup(width=800, height=600)
wn.tracer(0)

# Score

score_A = 0
score_B = 0

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
ball.dx = 0.4
ball.dy = -0.4

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, screen_height/2 - 40)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

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
        winsound.PlaySound("bounceBorder.wav", winsound.SND_ASYNC)
    
    if (ball.ycor() < (-(screen_height/2) + 10)):
        ball.sety(-(screen_height/2)+10)
        ball.dy *= -1
        winsound.PlaySound("bounceBorder.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -(screen_width/2)):
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("claps.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() > (screen_width/2)):
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("claps.wav", winsound.SND_ASYNC)

    # Ball hits the paddle

    if (ball.xcor() > second_pddl.xcor()-20 and ball.xcor() < second_pddl.xcor()-10) and (ball.ycor() < second_pddl.ycor()+40 and ball.ycor() > second_pddl.ycor() -40):
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bouncePaddle.wav", winsound.SND_ASYNC)
        

    if (ball.xcor() < first_pddl.xcor()+20 and ball.xcor() > first_pddl.xcor()+10) and (ball.ycor() < first_pddl.ycor()+40 and ball.ycor() > first_pddl.ycor() -40):
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bouncePaddle.wav", winsound.SND_ASYNC)

    # End of the game

    if score_A >= 10 or score_B >= 10:
        finishpen = turtle.Turtle()
        finishpen.hideturtle()
        finishpen.speed(0)
        finishpen.penup()
        finishpen.goto(0, 0)

        first_pddl.clear()
        first_pddl.hideturtle()
        second_pddl.clear()
        second_pddl.hideturtle()
        ball.clear()
        ball.hideturtle()
        pen.clear()

        i = 0
        for i in range (3):
            wn.bgcolor("black")
            finishpen.color("white")
            finishpen.clear()
            if score_A >= 10:
                finishpen.write("Player A wins!", align="center", font=("Arial", 32, "bold"))
            else:
                finishpen.write("Player B wins!", align="center", font=("Arial", 32, "bold"))
            time.sleep(1.5)
            wn.bgcolor("white")
            finishpen.color("black")
            finishpen.clear()
            if score_A >= 10:
                finishpen.write("Player A wins!", align="center", font=("Arial", 32, "bold"))
            else:
                finishpen.write("Player B wins!", align="center", font=("Arial", 32, "bold"))
            time.sleep(1.5)