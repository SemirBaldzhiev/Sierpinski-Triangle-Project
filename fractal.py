import turtle

DEGREE = 60
SIDES = 3
DRAW_SPEED = 100
SIZE_COEFFICIENT = 100

def draw_sierpinski_triangle(turtle, level, size):
    if level == 0:
        turtle.fillcolor("red")
        turtle.begin_fill()
        for _ in range(SIDES):
            turtle.forward(size)
            turtle.left(DEGREE*2)
        turtle.end_fill()
    else:
        size /= 2
        draw_sierpinski_triangle(turtle, level - 1, size)
        turtle.forward(size)
        draw_sierpinski_triangle(turtle, level - 1, size)
        turtle.backward(size)
        turtle.left(DEGREE)
        turtle.forward(size)
        turtle.right(DEGREE)
        draw_sierpinski_triangle(turtle, level - 1, size)
        turtle.left(DEGREE)
        turtle.backward(size)
        turtle.right(DEGREE)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=0.99, height=0.9)
    sierpinski_turtle = turtle.Turtle()
    sierpinski_turtle.penup()
    sierpinski_turtle.setpos(-window.window_width() / 2, -window.window_height() / 2)
    sierpinski_turtle.pendown()
    sierpinski_turtle.speed(DRAW_SPEED)

    level = int(input("Enter the level of the Sierpiński triangle [0-6]: "))
    while (level < 0 or level > 6):
        print("Invalid level. Please enter a level between 0 and 6.")
        level = int(input("Enter the level of the Sierpiński triangle [0-6]: "))
        
    size = SIZE_COEFFICIENT * level
    
    if size == 0: size = SIZE_COEFFICIENT

    draw_sierpinski_triangle(sierpinski_turtle, level, size)

    window.exitonclick()

if __name__ == "__main__":
    main()