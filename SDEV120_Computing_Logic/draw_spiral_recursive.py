import turtle

ZOOM_SCALE = 8.0
LINE_WIDTH = 7
SPEED = 5
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
cur_color = -1

# make screen object and
# set screen mode to world
sc = turtle.Screen()
sc.mode('world')
sc.setup(500, 500)

turtle.setworldcoordinates(-50, -450, 450, 50)


def change_color(t):
    global cur_color
    cur_color += 1
    if cur_color >= len(COLORS):
        cur_color = 0
    t.color(COLORS[cur_color])


def draw_spiral(t, line_length):
    change_color(t)
    if line_length > 0:
        t.forward(line_length * ZOOM_SCALE)
        t.right(90)
        draw_spiral(t, line_length - 5)


def main():
    t = turtle.Turtle()
    t.width(LINE_WIDTH)
    t.speed(SPEED)
    draw_spiral(t, 50)
    turtle.done()


main()
