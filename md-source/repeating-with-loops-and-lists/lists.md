Lists are very useful in programming.  In Python, lists look like this:

```python
["A", "List", "of", "Things"]
```

When things are in a list, we can tell Python to pull them out for us.  We just need to point to the right **index** number of the list.  Here's a diagram of the index numbers for the list above:

![Screen Shot 2014-09-28 at 5.01.51 PM.jpg](/api/files/5428a1b8d61e38df4eca1d46/Screen-Shot-2014-09-28-at-5-01-51-PM.jpeg "Screen Shot 2014-09-28 at 5.01.51 PM.jpg")

Let's ask Tina to help explain:

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
x = -80; y = 175; tina.goto(x, y)

our_list = ["A", "List", "of", "Things"]

tina.write("The code our_list[0] gives us the first thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[0])
tina.goto(x, y -20); y = tina.pos()[1]
tina.write("The code our_list[1] gives us the second thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[1])
tina.goto(x, y -20); x, y = tina.pos()
tina.write("The code our_list[2] gives us the third thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[2])
tina.goto(x, y -20); y = tina.pos()[1]
tina.write("The code our_list[3] gives us the third thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[3])
tina.goto(x, y -40);y = tina.pos()[1]
tina.write("And here's the whole list again:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(str(our_list))
tina.goto(0,-160)
```
