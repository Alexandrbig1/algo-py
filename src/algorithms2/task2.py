import turtle

def create_koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        create_koch_snowflake(t, length, level - 1)
        t.left(60)
        create_koch_snowflake(t, length, level - 1)
        t.right(120)
        create_koch_snowflake(t, length, level - 1)
        t.left(60)
        create_koch_snowflake(t, length, level - 1)

def draw_snowflake(size, level):
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size // 2, size // 3)
    t.pendown()

    for _ in range(3):
        create_koch_snowflake(t, size, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()

draw_snowflake(200, 2)