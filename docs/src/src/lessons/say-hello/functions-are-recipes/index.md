---
title: Functions Are Recipes

---


**Functions** are ways for us to have a program remember code we already wrote and do it again.  They're like recipes.

We can use functions to teach Tina how to do new things.  We make a function by typing `def`, then the function name, a pair of **parentheses** (`()`), then a colon (`:`).  Here's the beginning of a function named `first_function`:

```python
def first_function():
```

After a funtion is defined, we can put code inside of it by **indenting** it.  Indenting means having four spaces on the front:

```python
def first_function():
    print "This line is indented 4 spaces!"
```

Once a function is defined, we can **call** it by typing its name and a pair of **parentheses** (`()`).  Here's how we'll **call** our `first_function()`:

```python
first_function()
```
When we do this, everything inside the function will happen.

In this example, there's already a function called `triangle()` defined for you, and it is **called** one time.  **Call** it one or more times and see what happens!

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%3Dturtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0Atina.color%28%27purple%27%29%0A%0Adef%20triangle%28%29%3A%0A%20%20%20%20tina.left%2860%29%0A%20%20%20%20tina.forward%2830%29%0A%20%20%20%20tina.left%28120%29%0A%20%20%20%20tina.forward%2830%29%0A%20%20%20%20tina.left%28120%29%0A%20%20%20%20tina.forward%2830%29%0A%0Atriangle%28%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Ideas for modifying this program:
* Change what the `triangle()` says and Tina will do your new instructions.
* Try writing your own function and **calling** it as well!
