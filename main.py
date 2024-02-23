import turtle

def paddle_a_up():
    y=pad_a.ycor()
    y+=30
    pad_a.sety(y)

def paddle_b_up():
    y=pad_b.ycor()
    y+=30
    pad_b.sety(y)
def paddle_a_down():
    y=pad_a.ycor()
    y-=30
    pad_a.sety(y)

def paddle_b_down():
    y=pad_b.ycor()
    y-=30
    pad_b.sety(y)


wn=turtle.Screen();
wn.title("The pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A

pad_a=turtle.Turtle()
pad_a.color("white")
pad_a.shape("square")
pad_a.speed(0)
pad_a.penup()
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.goto(-350, 0)


#paddle B


pad_b=turtle.Turtle()
pad_b.color("white")
pad_b.shape("square")
pad_b.speed(0)
pad_b.penup()
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.goto(350,0)

#Ball

ball=turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.speed(5)
ball.penup()

#scoring
pen=turtle.Turtle()
pen.color("white")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  player B: 0", align="center", font=("Courier", 24, "normal"))


# while True:

wn.update()

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

ball.dy=-0.2
ball.dx=0.2

score_a=0
score_b=0

while True:
    wn.update()
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy= -0.1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy= 0.1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() >340 and ball.xcor() <350 and (ball.ycor() < pad_b.ycor()+40  and ball.ycor() > pad_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < pad_a.ycor()+40  and ball.ycor() > pad_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1



turtle.mainloop()