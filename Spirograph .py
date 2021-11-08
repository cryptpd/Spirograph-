
import turtle as tt


tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

for i in range(6):

    # Choose your color combination
    for color in ('green', 'magenta', 'white',
                  'yellow', 'red', 'blue',
                  'cyan'):
        tt.color(color)

        tt.circle(100)

        tt.left(10)


    tt.hideturtle()
