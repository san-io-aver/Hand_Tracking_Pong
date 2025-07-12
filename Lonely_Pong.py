import turtle, tkinter
import time
from handTracking import HandTracker 

handX=0
width = 1000
height = 600
score=0

win = turtle.Screen()
win.title("SinglePOng")
win.bgcolor("black")
win.setup(width=width,height=height)
win.tracer(0)

#bat
bat = turtle.Turtle()
bat.speed(0)
bat.shape("square")
bat.color("white")
bat.shapesize(stretch_wid=1,stretch_len=5)
bat.penup()
bat.goto(0,-270)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

score_display = turtle.Turtle()
score_display.speed(0)
score_display.hideturtle()
score_display.color("white")
score_display.goto(0, 260)
score_display.write(f"Score: {score}",align="center",font=("Courier",18,"normal"))
#movement
#handX 0-1
def bat_move(hX):
    x = 1000*hX - 500 #(x-min1)/(max1-min1 = (hx-min2)/(max2-min2)
    bat.setx(x)
def update_score():
    score_display.clear()
    score_display.penup() 
    score_display.write(f"Score: {score}",align="center",font=("Courier",18,"normal"))
def gameOver():
    score_display.clear()
    score_display.penup()  
    score_display.goto(0, 260)
    score_display.write(f"GAME OVER (Score: {score})", align="center", font=("Courier", 25, "normal"))
    score_display.goto(0, 220)
    score_display.write("RESTART GAME? PRESS ENTER", align="center", font=("Courier", 18, "normal"))



def restart():
    global score 
    score=0
    update_score()
    ball.goto(400,400)
    ball.dy *= -1 


ht = HandTracker()   
win.listen()
win.onkeypress(restart, "Return") 

try:
    while True:
        win.update()
        if ht.getXcoordinate():
            handX = ht.getXcoordinate()
        bat_move(handX)
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        
        if ball.xcor() > 490:
            ball.setx(490)
            ball.dx *= -1
        if ball.xcor() < -490:
            ball.setx(-490)
            ball.dx *= -1
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1                      
        if ball.ycor() < -290:
            ball.sety(-290)
            gameOver()

        if ball.ycor() < -250 and ball.ycor() > -270 and ball.xcor() < bat.xcor()+50 and ball.xcor() > bat.xcor()-50:   
            ball.sety(-250)
            offset = ball.xcor() - bat.xcor()
            print(offset)
            ball.dx = offset * 0.08  # control angle sensitivity
            ball.dy *= -1
            score+=1
            update_score()
            
        time.sleep(1/120)
except (turtle.Terminator, tkinter.TclError):
    print("closed.")
finally:
    ht.exit()        
        
        
        
