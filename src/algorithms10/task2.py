import turtle
import math

ANGLE = 45
LENGTH_REDUCTION_FACTOR = math.sqrt(2) / 2

def draw_tree(branch_length: float, level: int):

    if level == 0:
        return

    turtle.forward(branch_length)

    position = turtle.pos()
    angle = turtle.heading()

    turtle.left(ANGLE)
    draw_tree(branch_length * LENGTH_REDUCTION_FACTOR, level - 1)

    turtle.setpos(position)
    turtle.setheading(angle)

    turtle.right(ANGLE)
    draw_tree(branch_length * LENGTH_REDUCTION_FACTOR, level - 1)

    turtle.setpos(position)
    turtle.setheading(angle)


def main():
    level = int(input("Enter recursion level: "))
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()
    draw_tree(100, level)
    turtle.done()


if __name__ == "__main__":
    main()