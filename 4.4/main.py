import turtle

#setup turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

#function to draw squares
def draw_square(t, side):
    for _ in range(4):
        t.forward(side)
        t.left(90)

#recursive function that adds 1 to side and -1 to number of times will draw per loop to get down to base case. Goes back to center every time
def recursive(t, num_squares, side, rotation):
    #end case stops here
    if num_squares == 0:
        return 0
    t.penup()
    t.goto(0, 0)
    t.pendown()
    #calls draw_square to draw square per recursion then modifies each one by size and rotation
    draw_square(t, side)
    t.right(rotation)
    #adds one to count for total recursion calls
    return 1+ recursive(t, num_squares - 1, side + 1, rotation)

#make dictionary
settings = {
    'default_color': 'blue',
    'side': 1,
    'rotation': 15,
    'valid_colors': ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"]
}

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
color = ""
#while loop to check for right color
while color not in settings['valid_colors']:
    color = input("What color do you want the squares? Default is " + settings['default_color'] + ": ").strip()
    if color == "":
        color = settings['default_color']
    if color not in settings['valid_colors']:
        print("Invalid color! Valid colors are:", settings['valid_colors'])

#set turtle to inputed color
t.color(color)

#print total recursion calls by return + 1 value and calls function in one line
numRecursion = recursive(t, num_squares, settings['side'], settings['rotation'])
print("Total recursive calls: " + str(numRecursion))
turtle.done()