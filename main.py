from turtle import*
ball=Turtle()
window =Screen()
bgcolor("grey")
window.setup(1000,600)

p1 = Turtle()
p1.penup()
p1.shapesize(7,2)
p1.color("green")
p1.shape("square")
p1.setx(490)

ball.color("black")




def u1():
    p1.sety(p1.ycor()+30)
def u2():
    p2.sety(p2.ycor()+30)
def d1():
    p1.sety(p1.ycor() - 30)
def d2():
    p2.sety(p2.ycor() - 30)
ball.shape("circle")
ball.penup()

p2 = Turtle()
p2.penup()
p2.shape("square")
p2.color("red")
p2.shapesize(10,2)
p2.setx(-490)

y_velo=5.5
x_velo=10
int(ball.ycor())
int(ball.xcor())

window.listen()
window.onkey(u1, "Up")
window.onkey(u2, "w")
window.onkey(d1, "Down")
window.onkey(d2, "s")
window.update()
while True:

    a=(ball.xcor())
    ball.setx(ball.xcor() + x_velo)
    ball.sety(ball.ycor() + y_velo)
    if(ball.ycor()<-565/2 or ball.ycor()>565/2):
        y_velo=-y_velo
    if((a)>500):
        print("player 1 wins")
        break
    if((a)<-500):
        print("player 2 wins")
        break
    print(p1.distance(ball))
    if(p2.distance(ball)<60 or p1.distance(ball)<60):
        x_velo=-x_velo

done()


