
We can loop over a list of colors and tell Tina to turn that color.

<iframe src="//player.vimeo.com/video/107875423?title=0&amp;byline=0&amp;portrait=0" width="600" height="337" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> 

Run this program, and see where the colors come from.  What happens if you add or remove colors from the list?

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

for each_color in colors:
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.circle(40)
    tina.right(angle)
    tina.forward(30)
```

Want to make this program your own?  Change what tina does inside the `for` loop.  What else could she do for each color?