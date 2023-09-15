import turtle
#Defining Graphics Window
Win1 = turtle.Screen()
#Using graphic pen on the screen
pen1 = turtle.Turtle()
pen1.color("red")
#Using pen size
pen1.pensize(10)
#Moving forward
#n_side = 4    #Number of sides
'''for i in range(100):
    pen1.forward(1)
    pen1.right(1)'''
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()
#turtle.done()
#Sum of all angles for any figure is 360
