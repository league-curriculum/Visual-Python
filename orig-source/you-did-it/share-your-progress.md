We've learned quite a lot in just a short time!  

We started with an example that looked a lot like the one below.  Think about how much you've learned!  

Code is more fun if your friends are doing it too!  Customize this code and share the link or email it:

```python.run
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.end_fill()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(10)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("I completed an Hour of Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)
tommy.write("Try it out at HourofPython.com", align="center", font=(None, 16, "bold"))
tommy.goto(0,-110)
```

Special thanks to the many people who've helped make this site possible and to **you** for making it through to the end!