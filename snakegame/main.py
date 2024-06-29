import turtle
import time
import random

speed=0.11

frame = turtle.Screen()
frame.title("Snake Game v1")
frame.bgcolor("lightblue")
frame.setup(width=1920,height=1080)
frame.tracer(0)

x=0
y=0
head = turtle.Turtle()
head.direction="stop"
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)

feed = turtle.Turtle()
feed.direction="stop"
feed.speed(0)
feed.shape("square")
feed.color("black")
feed.penup()
feed.goto(0,0)
feed.shapesize(2)

bottom = []
def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+30)
    if head.direction =="down":
        y=head.ycor()
        head.sety(y-30)
    if head.direction =="right":
        x=head.xcor()
        head.setx(x+30)
    if head.direction =="left":
        x=head.xcor()
        head.setx(x-30)

def goup():
    if head.direction!="down":
        head.direction="up"
def godown():
    if head.direction!="up":
        head.direction="down"
def goright():
    if head.direction!="left":
        head.direction="right"
def goleft():
    if head.direction!="right":
        head.direction="left"


frame.listen()
frame.onkey(goup,"Up")
frame.onkey(godown,"Down")
frame.onkey(goright,"Right")
frame.onkey(goleft,"Left")

z=0
c=0

while True:
    frame.update()
    move()
    time.sleep(speed)

    if head.xcor()>720 or head.xcor()<(-720) or head.ycor() >400 or head.ycor()<(-400):
        head.direction="stop"
        hata = turtle.Screen()
        hata.setup(500,200)
        hata.bgcolor("white")
        hata.title("Game Over")
        time.sleep(3)

        break
    if head.distance(feed) < 30:
        k = (-400)
        l = 400
        a = random.randint(k,l)
        b = random.randint(k,l)
        feed.goto(a,b)




        tail = turtle.Turtle()
        tail.color("black")
        tail.penup()
        tail.speed(0)
        tail.shape("square")
        tail.goto(x, y)
        tail.shapesize(2)

        bottom.append(tail)

    for i in range(len(bottom) -1, 0, -1):
         m = bottom[i-1].xcor()
         n = bottom[i-1].ycor()
         bottom[i].goto(m,n)

    if len(bottom) > 0:
        x = head.xcor()
        y = head.ycor()
        bottom[0].goto(x,y)
