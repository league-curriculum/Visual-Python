![The LEAGUE](https://www.jointheleague.org/wp-content/uploads/2022/01/logo1.png)

Today we're going to learn the basics of a programming language named Python.  Python is fun to learn but is also a **Real** programming language that powers websites and apps like Yelp.com and Twitter.

[The LEAGUE of Amazing Programmers ](https://jointheleague.org) is a non profit progamming school that teaches 5th through 12th grade students all over San Diego to program. We are really happy to have you here for this class, and we hope that you will love programming as much as we do. 

This Hour of code activity was originally created by Trinket.io, and this course is 
a modified version of [A Visual Introduction to Python](https://hourofpython.com/a-visual-introduction-to-python/), with some extra lessons and exercises.

## Run your first program!

No need to save the fun stuff until the end.  Here's a program in Python.  Press Run to see what it does:

```python.run:height=470
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)

tommy.penup()
tommy.goto(0,-50)
tommy.color('black')
tommy.write("Let's Learn Python!", align="center", font=(None, 16, "bold"))
tommy.goto(0,-80)
```

At the end of this activity we'll come back to this example and you'll see you'll understand quite a lot about how it works.  **In fact, you'll write or customize lots of your your own programs in just an hour!**

## Keep Going!

You'll see lots of new things during this tutorial.  Code may always look unfamiliar, and *no one knows everything* about code, not even the experts!  So the most important thing is to **keep going**, even if you're confused or run into errors!

Also, for each of the interactive examples you see, there is a **Reset** button in the left hand menu.  If you want to start over, it will reset your code back to the beginning.

Have fun!
