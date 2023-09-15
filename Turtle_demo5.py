import turtle
#Defining Graphics Window
Win1 = turtle.Screen()
#Using graphic pen on the screen
pen1 = turtle.Turtle()
pen1.color("blue")
#Using pen size
pen1.pensize(5)
#Moving forward
#n_side = 4    #Number of sides
for i in range(5):
    pen1.forward(100)
    pen1.right(145)
turtle.done()
#Sum of all angles for any figure is 360
