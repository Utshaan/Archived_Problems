import turtle
sc = turtle.Screen()
sc.title("Pong Game")
sc.setup(width=1000, height=600)
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("grey")
sc.bgcolor("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("cyan")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("yellow")
hit_ball.penup()
hit_ball.goto(0,0)
hit_ball.dx = 5
hit_ball.dy = -5
left_player = 0
right_player = 0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("pink")
sketch.penup()
sketch.hideturtle()
sketch.goto(0,260)
sketch.write("left_player : 0       right_player : 0", align="center", font=("hooge 05_55", 24, "normal"))
def paddleaup():
    y = left_pad.ycor()
    y +=20
    left_pad.sety(y)
def paddleadown():
    y = left_pad.ycor()
    y -=20
    left_pad.sety(y)
def paddlebup():
    y = right_pad.ycor()
    y+=20
    right_pad.sety(y)
def paddlebdown():
    y = right_pad.ycor()
    y -=20
    right_pad.sety(y)
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "i")
sc.onkeypress(paddlebdown, "k")
while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
    if hit_ball.xcor() > 500:
        hit_ball.goto(0,0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("left_player : {}          right_player : {}".format(left_player, right_player), align="center", font=("hooge 05_55", 24, "normal"))
    if hit_ball.xcor() < -500:
        hit_ball.goto(0,0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("left_player : {}          right_player : {}".format(left_player, right_player), align="center", font=("hooge 05_55", 24, "normal"))
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and hit_ball.ycor() > right_pad.ycor()-40):
        hit_ball.setx(360)
        hit_ball.dx *= -1
    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor()+40 and hit_ball.ycor() > left_pad.ycor()-40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
