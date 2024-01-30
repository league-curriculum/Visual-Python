Functions are recipes, but we can also give them special inputs called `parameters` that can make them slightly different each time.  Turns out, we've already done this before!

In the previous example, where Tina made cakes, we told here **where** to make cakes by including an `x` and `y` coordinate.  Here's how we'd tell her to make a cake at the x,y point 0,100:

```python
make_cake(0,100)
```

The `x` and `y` coordinates we entered are `parameters`.  To make a function that accepts a parameter, we include its name inside the parentheses when we define it:

```python.run:height=200
def my_function(parameter):
    print(parameter)

my_function("Hello!")
my_function("Bonjour!")
```
 In the example above we **call** `my_function` twice, once with a parameter we defined as "Hello!", and another time with the parameter "Bonjour!".  The function does the same thing, print the parameter, but we get to tell it what to print.
 
Great- this means that we can write a function that tells Tina how to print different things.

Can you modify this example so that the function `say()` is **called** with different `parameter` inputs?

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(-60,175)

def say(something):
    x, y = tina.pos()
    tina.write("You told me to say this:")
    tina.goto(x + 10, y -10)
    tina.write(something)
    tina.goto(x, y - 25)
    
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
```

Hints:

* Tina will need anything she says to be in **quotes** (`"`) so she can read it.
* You can make Tina say even more things!  Just add another line with `say("Your message here")`