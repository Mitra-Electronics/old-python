import turtle
#Defining Graphics Window
Win1 = turtle.Screen()
#Using graphic pen on the screen
pen1 = turtle.Turtle()
n_sidein = turtle.numinput("Enter the number of sides","Enter the number of sides")
#Using pen colour
n_side = int(n_sidein)
pen1.color("blue")
#Using pen size
pen1.pensize(5)
#Moving forward
#n_side = 4    #Number of sides
length = 100   #length of each side
angle = 360.0/n_side #angle of each side
for i in range(n_side):
    pen1.forward(length)
    pen1.right(angle)
turtle.done()
#Sum of all angles for any figure is 360
