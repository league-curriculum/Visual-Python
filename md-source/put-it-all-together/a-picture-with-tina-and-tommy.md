Let's take some time and make neat pictures with Tina and Tommy!  

Remember, since they're both `turtle` objects, we can move them `forward` and `backward`, turn them `left` and `right`, `goto` a specific point, change their `color`, and tell them to `write` words on the screen.  To tell Tina or Tommy what to do, add a command with a period after their name like this:

```python
tina.forward(100)

tommy.goto(50,50)
```

`goto` is particularly helpful in drawing.  

Here's a trinket with Tina and Tommy in it, waiting for your commands.  Add commands and run them to see what they do.  Keep going until you have the picture you want!  When you're done, use the Share links in the menu bar to share your link with your teacher or friends.

```python.run:height=500
import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')

tina.begin_fill()
tina.goto(200,0)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,0)
tina.goto(0,0)
tina.end_fill()

tommy.penup()
tommy.goto(-70,100)
tommy.write("Tina, let's Make a picture together!")
tommy.goto(0,50)
tommy.pendown()

tina.penup()
tina.color('white')
tina.goto(-40,-100)
tina.write("Alright, I'm ready!!")
tina.goto(0,-130)
tina.pendown()
```



If you run into errors, check to make sure your **parentheses** (`()`) and **quotes** (`'`) are in the right places. If you want to start over, you can **Reset** the example in the left hand menu.

