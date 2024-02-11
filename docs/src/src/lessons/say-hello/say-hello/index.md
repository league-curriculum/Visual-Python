---
title: Say Hello

---


Functions are recipes, but we can also give them special inputs called `parameters` that can make them slightly different each time.  Turns out, we've already done this before!
The `x` and `y` coordinates we entered are `parameters`.  To make a function that accepts a parameter, we include its name inside the parentheses when we define it:

<iframe width="100%" height="200" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=def%20my_function%28parameter%29%3A%0A%20%20%20%20print%28parameter%29%0A%0Amy_function%28%22Hello%21%22%29%0Amy_function%28%22Bonjour%21%22%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
 In the example above we **call** `my_function` twice, once with a parameter we defined as "Hello!", and another time with the parameter "Bonjour!".  The function does the same thing, print the parameter, but we get to tell it what to print.
 
In the previous example, where Tina made cakes, we told here **where** to make cakes by including an `x` and `y` coordinate.  Here's how we'd tell her to make a cake at the x,y point 0,100:

```python
make_cake(0,100)
```


Great- this means that we can write a function that tells Tina how to print different things.

Can you modify this example so that the function `say()` is **called** with different `parameter` inputs?

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.penup%28%29%0Atina.goto%28-60%2C175%29%0A%0Adef%20say%28something%29%3A%0A%20%20%20%20x%2C%20y%20%3D%20tina.pos%28%29%0A%20%20%20%20tina.write%28%22You%20told%20me%20to%20say%20this%3A%22%29%0A%20%20%20%20tina.goto%28x%20%2B%2010%2C%20y%20-10%29%0A%20%20%20%20tina.write%28something%29%0A%20%20%20%20tina.goto%28x%2C%20y%20-%2025%29%0A%20%20%20%20%0Asay%28%22Hi%20there%21%22%29%0Asay%28%22Hi%20there%21%22%29%0Asay%28%22Hi%20there%21%22%29%0Asay%28%22Hi%20there%21%22%29%0Asay%28%22Hi%20there%21%22%29%0Asay%28%22Hi%20there%21%22%29%0Asay%28%22Hi%20there%21%22%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Hints:

* Tina will need anything she says to be in **quotes** (`"`) so she can read it.
* You can make Tina say even more things!  Just add another line with `say("Your message here")`
