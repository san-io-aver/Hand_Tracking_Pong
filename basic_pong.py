import turtle

win = turtle.Screen()
win.title("SinglePOng")
win.bgcolor("black")
win.setup(width=1000,height=600)
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
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#movement
def bat_right():
    x = bat.xcor()
    x += 60
    bat.setx(x)

def bat_left():
    x = bat.xcor()
    x -= 60
    bat.setx(x)
    
win.listen()
win.onkeypress(bat_right,"Right")    
win.onkeypress(bat_left,"Left") 
   
while True:
    win.update()
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
        ball.goto(400,400)
        ball.dy *= -1     
    if ball.ycor() < -250 and ball.ycor() > -270 and ball.xcor() < bat.xcor()+40 and ball.xcor() > bat.xcor()-40:   
        ball.sety(-250)
        ball.dy *= -1
        
        
        
        
