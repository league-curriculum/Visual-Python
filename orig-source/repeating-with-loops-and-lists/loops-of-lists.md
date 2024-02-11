So far we've been telling Tina to do things over and over.  Remember this example?

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.left(90)
tina.forward(20)
tina.write("What color am I now?")

tina.forward(20)
tina.color("blue")
tina.write("What color am I now?")

tina.forward(20)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(20)
tina.color("green")
tina.write("What color am I now?")
```

There's a lot of repetition.  If we give Tina a list of colors and tell her to do the same thing with each color, we can make the same picture with much less code!

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

color_list = ["black", "blue", "purple", "green"]

tina.left(90)

for color in color_list:
    tina.forward(20)
    tina.color(color)
    tina.write("What color am I now?")
```

We can now easily change how many times Tina draws as well.  Try adding a new color name to the list. Here's what it would look like to add `"yellow"` to the list:

```python
color_list = ["black", "blue", "purple", "green", "yellow"]
```

Don't forget the **quotes** (`""`) around your color word!

Hit a snag?  Don't worry! Tips: 
- Remember to put your color name in quotes (`""`)
- Remember to include a comma (`,`) in between each color name and the next one
- Remember to begin and end your list with square brackets (`[` and `]`)