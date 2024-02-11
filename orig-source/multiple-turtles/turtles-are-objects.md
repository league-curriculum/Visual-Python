Tina is a `turtle`.  But what's a `turtle`?  It's what's called an `object`.  This means that a programmer has written some code that we can use to do cool things.  In Tina's case, she knows how to go `forward`, `backward`, `left`, and `right` because the people who wrote the `turtle` object thought those would be neat things for turtles to do.

At the beginning of all of our examples, we `import turtle`.  This lets us use code that's already been written and gives Tina and any other turtles we make their abilities.

<iframe src="//player.vimeo.com/video/107875794?title=0&amp;byline=0&amp;portrait=0" width="710" height="249" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

You can give Tina a different name, and that newly named turtle will know how to do everything Tina does.  Give Tina any name you choose in this example:

```python.run
import turtle

tina = turtle.Turtle()
tina.shape('turtle')

tina.forward(100)
```



Hint: You'll have to change **all** of the names from Tina to the name you choose.  Otherwise, Python will be confused which one you're talking about.