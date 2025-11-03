import turtle

def draw_square(t, side):
    for _ in range(4):
        t.forward(side)
        t.left(90)

def recursive(t, num_squares, side, rotation):
    if num_squares == 0:
        return
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_square(t, side)
    t.right(rotation)
    recursive(t, num_squares - 1, side + 3, rotation)

def main():
    num_squares = input("How many squares to draw? Default is 1: ").strip()
    if num_squares == "" or not num_squares.isdigit():
        num_squares = 1
    else:
        num_squares = int(num_squares)
        num_squares = max(1, min(num_squares, 100))

    valid_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white"]
    color = ""
    while color not in valid_colors:
        color = input("What color do you want the squares? Default is blue: ").strip()
        if color == "":
            color = "blue"
        if color not in valid_colors:
            print("Invalid color! Try again. Valid colors are:", valid_colors)

    side = 1
    rotation = 15

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)

    recursive(t, num_squares, side, rotation)

    turtle.done()

main()