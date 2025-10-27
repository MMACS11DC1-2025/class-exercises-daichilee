import turtle

turtle = turtle.Turtle()

def drawTree(level, branchLength):
  if level > 0:
    turtle.forward(branchLength)
    turtle.left(40)
    drawTree(level-1, branchLength/1.61)
    
    turtle.right(80)
    drawTree(level-1, branchLength/1.61)
    
    turtle.left(40)
    turtle.back(branchLength)
  else:
    turtle.color("green")
    turtle.stamp()
    turtle.color("brown")
turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.shape("triangle")
levels = input("How many levels do you want me to draw? ")
drawTree(int(levels), 120)