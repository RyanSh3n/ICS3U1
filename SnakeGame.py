import turtle
import time
import random

delay = 0.1

#Score
score =0
highScore=0

#Setting up the screen
window = turtle.Screen()
window.title("Snake Game by Lexiang Pan and Ryan Shen")
window.bgcolor("green")
window.setup(width=600, height = 600)
window.tracer(0)

#Head of the snake:
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food of snake
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0,100)
apple.direction = "stop"

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions
def going_up():
    if head.direction != "down":
        head.direction = "up"
def going_down():
    if head.direction != "up":
        head.direction = "down"
def going_left():
    if head.direction != "right":
        head.direction = "left"
def going_right():
    if head.direction != "left":
        head.direction = "right"

#Functions
def snakeMoving():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Function

def restartGame(segments, delay):
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    #hide segments
    for s in segments:
        s.goto(1000,1000)

    #Clear segments list
    segments = []

    #reset score
    score=0

    #reset delay
    delay =0.1

    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

#Keyboard Binding
window.listen()
window.onkeypress(going_up, "w")
window.onkeypress(going_down, "s")
window.onkeypress(going_left, "a")
window.onkeypress(going_right, "d")

while True:
    window.update()

    #check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        restartGame(segments, delay)

    #check for collision with food
    if head.distance(apple) < 20:
        #move food to a new coordinate
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        apple.goto(x, y)

        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten delay
        delay -=0.001

        #increase score
        score +=10
    
        if score >highScore:
            highScore = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))

    #moving the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #moving segments to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    snakeMoving()

    #check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            restartGame(segments, delay)
    time.sleep(delay)

window.mainloop()
