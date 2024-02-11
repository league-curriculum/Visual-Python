Functions are recipes, but we can also give them special inputs called `parameters` that can make them slightly different each time.  Turns out, we've already done this before!
The `x` and `y` coordinates we entered are `parameters`.  To make a function that accepts a parameter, we include its name inside the parentheses when we define it:

{{ trinket("say-hello_1.py", width="100%", height="200", embed_type="python") | safe }}
 In the example above we **call** `my_function` twice, once with a parameter we defined as "Hello!", and another time with the parameter "Bonjour!".  The function does the same thing, print the parameter, but we get to tell it what to print.
 
In the previous example, where Tina made cakes, we told here **where** to make cakes by including an `x` and `y` coordinate.  Here's how we'd tell her to make a cake at the x,y point 0,100:

```python
make_cake(0,100)
```


Great- this means that we can write a function that tells Tina how to print different things.

Can you modify this example so that the function `say()` is **called** with different `parameter` inputs?

{{ trinket("say-hello_2.py", width="100%", height="800", embed_type="python") | safe }}

Hints:

* Tina will need anything she says to be in **quotes** (`"`) so she can read it.
* You can make Tina say even more things!  Just add another line with `say("Your message here")`

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.