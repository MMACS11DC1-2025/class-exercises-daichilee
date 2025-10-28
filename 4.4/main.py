import turtle


def drawsquare(pen, size):
    """Draw a single square with side `size` using turtle `pen`."""
    for _ in range(4):
        pen.forward(size)
        pen.left(90)


def prompt_int(prompt, default=9, min_val=1, max_val=100):
    s = None
    try:
        screen = turtle.Screen()
        s = screen.textinput("Input", "{} [{}]:".format(prompt, default))
    except Exception:
        try:
            s = input("{} [{}]: ".format(prompt, default))
        except (EOFError, KeyboardInterrupt):
            return default

    if s is None:
        return default
    s = s.strip()
    if s == "":
        return default
    try:
        v = int(s)
    except ValueError:
        return default
    if min_val is not None and v < min_val:
        return min_val
    if max_val is not None and v > max_val:
        return max_val
    return v


def main():
    count = prompt_int("How many squares to draw?", 9, min_val=1, max_val=100)
    size = 100
    angle = 40

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    for _ in range(count):
        pen.penup()
        pen.goto(0, 0)   
        pen.pendown()
        drawsquare(pen, size)
        pen.right(angle)

    turtle.done()


if __name__ == "__main__":
    main()