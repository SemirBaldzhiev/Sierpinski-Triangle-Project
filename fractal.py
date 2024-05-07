import turtle

def draw_sierpinski_triangle(turtle, order, size):
    if order == 0:
        turtle.fillcolor("red")
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()
    else:
        size /= 2
        draw_sierpinski_triangle(turtle, order - 1, size)
        turtle.forward(size)
        draw_sierpinski_triangle(turtle, order - 1, size)
        turtle.backward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        draw_sierpinski_triangle(turtle, order - 1, size)
        turtle.left(60)
        turtle.backward(size)
        turtle.right(60)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.setup(width=0.99, height=0.9)
    sierpinski_turtle = turtle.Turtle()
    sierpinski_turtle.penup()
    sierpinski_turtle.setpos(-window.window_width() / 2, -window.window_height() / 2)
    sierpinski_turtle.pendown()
    sierpinski_turtle.speed(100)

    order = int(input("Enter the level of the Sierpiński triangle: "))
    size = 100*order
    
    if size == 0: size = 100

    draw_sierpinski_triangle(sierpinski_turtle, order, size)

    window.exitonclick()

if __name__ == "__main__":
    main()