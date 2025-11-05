import turtle

#setup turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

#Recursion count variable
numRecursion = 0

#function to draw squares
def draw_square(t, side):
    for _ in range(4):
        t.forward(side)
        t.left(90)

#recursive function that adds 1 to side and -1 to number of times will draw per loop. goes back to center every time
def recursive(t, num_squares, side, rotation):

    #make it so this function can access the variable
    global numRecursion
    #end case stops here
    if num_squares == 0:
        return
    #add 1 per run
    numRecursion += 1

    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_square(t, side)
    t.right(rotation)
    recursive(t, num_squares - 1, side + 1, rotation)

#get user input
num_squares = input("How many squares to draw? Default is 1: ").strip()
if num_squares == "" or not num_squares.isdigit():
    num_squares = 1
else:
    num_squares = int(num_squares)
    if num_squares > 1000:
        num_squares = 1000
    elif num_squares < 1:
        num_squares = 1
#check to see if program gets right input also just for user clarification
print("You inputted " + str(num_squares))

#make list of valid colors
valid_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"]
color = ""
#while loop to check for right color
while color not in valid_colors:
    color = input("What color do you want the squares? Default is blue: ").strip()
    if color == "":
        color = "blue"
    if color not in valid_colors:
        print("Invalid color! Valid colors are:", valid_colors)

#settings
side = 1
rotation = 15

t.color(color)

#call recusive function
recursive(t, num_squares, side, rotation)

#print total recursion calls
print("Total recursive calls: " + str(numRecursion))
turtle.done()

