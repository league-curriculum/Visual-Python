Not only can we rename Turtles: we can have more than one!  Let's give Tina a friend named Tommy:

```python.run
import turtle

tina = turtle.Turtle()
tina.shape('turtle')
tina.color('black')

tina.left(90)
tina.forward(100)
tina.write("I'm Tina!")
tina.forward(20)
tina.right(90)

tommy = turtle.Turtle()
tommy.shape('turtle')
tommy.color('black')

tommy.right(90)
tommy.forward(100)
tommy.write("I'm Tommy!")
tommy.forward(20)
tommy.left(90)
```

Tina and Tommy are both drawing in `black`.  Can you modify the code `tina.color('black')` and `tommy.color('black')` so that they're different colors?  Need a color idea?  Try an unusal one like `'goldenrod'` or `'magenta'`.  Don't forget the **quotes** (`'`)!