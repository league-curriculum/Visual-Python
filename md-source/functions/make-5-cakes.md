One of the great things about functions is that they can repeat complicated instructions without us having to repeat ourselves in code!

Earlier we talked about how **functions are like recipes**. In this exercise, we've already taught Tina the recipe for making a picture of a cake and she's made three.  Tell her to make more cakes by **calling** the function with different `x` and `y` locations at the very bottom of the program.  

How many cakes should she make?

```python.run:height='500'
import turtle
tina=turtle.Turtle()
tina.shape('turtle')

def make_cake(x=0, y=0):
    tina.penup()
    tina.color('pink')
    tina.goto(x, y)
    tina.pendown()
    tina.begin_fill()
    tina.goto(x + 20, y)
    tina.goto(x + 20, y + 20)
    tina.goto(x - 20, y + 20)
    tina.goto(x - 20, y)
    tina.goto(x, y)  
    tina.end_fill()
    tina.goto(x, y + 20)
    tina.color('yellow')
    tina.goto(x, y + 35)
    tina.goto(x, y + 30)
    tina.color('black')
    tina.goto(x, y + 20)
    tina.penup()
    tina.goto(x, y + 10)
    
make_cake(0,0)
make_cake(-100,0)
make_cake(100,0)
```

Hint: The first number in `make_cake()` is **how far left or right** Tina should go, while the second is **how high or low** she should go before starting to draw.

