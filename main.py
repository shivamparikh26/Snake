import turtle
import random
import time
box = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("light blue")
box.speed(1000)
box.penup()
box.goto(-200,200)
box.pendown()
for i in range(4):
  box.forward(400)
  box.right(90)
box.ht()
t = turtle.Turtle()
t.speed(1000)
t.shape("square")
t.penup()
t.goto(0,100)

direction = "stop"
def up():
  global direction
  if direction!="down":
    direction = "up"
def down():
  global direction
  if direction!="up":
    direction = "down"
def left():
  global direction 
  if direction!="right":
    direction = "left"
def right():
  global direction 
  if direction!="left":
    direction = "right"
screen.onkey(up,"up")
screen.onkey(down,"down")
screen.onkey(left,"left")
screen.onkey(right,"right")
screen.listen()
def move():
  if direction == "up":
    t.sety(t.ycor()+20)
  if direction == "down":
    t.sety(t.ycor()-20)
  if direction == "right":
    t.setx(t.xcor()+20)
  if direction == "left":
    t.setx(t.xcor()-20)
score = 0
highscore = 0
s = turtle.Turtle()
s.speed(1000)
s.color("white")
s.penup()
s.goto(0,175)
s.write("score: "+str(score)+" High Score: " +str(highscore),align ="center", font=("Courier", 18, "normal"))

s.ht()

red = turtle.Turtle()
red.speed(1000)
red.shape("circle")
red.color("red")
red.penup()
red.goto(0,0)

tail = []
while True:
  screen.update()
  time.sleep(1)
  if t.distance(red)<15:
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    red.goto(x,y)
    t2 = turtle.Turtle()
    t2.speed(1000)
    t2.shape("square")
    t2.color("gray")
    t2.penup()
    tail.append(t2)
    score+=10
    if score>highscore:
      highscore = score
  for i in range(len(tail)-1,0,-1):
    x = tail[i-1].xcor()
    y = tail[i-1].ycor()
    tail[i].goto(x,y)
  if len(tail)>0:
    x = t.xcor()
    y = t.ycor()
    tail[0].goto(x,y)
  move()
  hit = False
  for i in tail:
    if i.distance(t)<20:
      hit = True
      break
  if t.xcor()>200 or t.xcor()<-200 or t.ycor()>200 or t.ycor()<-200 or hit:
    time.sleep(0.5)
    t.goto(0,0)
    direction = "stop"
    for i in tail:
      i.goto(1000,1000)
    tail = []
    score = 0
  s.clear()
  s.write("score: "+str(score)+" High Score: " +str(highscore),align ="center", font=("Courier", 18, "normal"))
