---
title: How High Up Is Tina

---


Tina can ask us things, and we can also tell her to ask herself things. In this example, we'll tell her to go to a high or low spot on the screen and she'll change what she says depending on how high or low she is.

<iframe width="100%" height="500" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%3Dturtle.Turtle%28%29%0Atina.shape%28%27turle%27%29%0Atina.penup%28%29%0A%0Atry%3A%0A%20%20%20%20how_high%20%3D%20int%28input%28%22How%20high%20should%20Tina%20go%3F%20%28Use%20numbers%20between%20200%20and%20-200%29%22%29%29%0A%20%20%20%20tina.goto%280%2C%20how_high%29%0A%20%20%20%20height%20%3D%20tina.pos%28%29%5B1%5D%0A%20%20%20%20%0A%20%20%20%20if%20height%20%3E%20150%20and%20height%20%3C%3D%20200%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22This%20is%20very%20high%21%22%29%0A%20%20%20%20elif%20height%20%3E%20100%20and%20height%20%3C%3D%20150%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22This%20is%20high%21%22%29%0A%20%20%20%20elif%20height%20%3E%200%20and%20height%20%3C%3D%20100%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22This%20is%20high%20but%20not%20too%20high%21%22%29%0A%20%20%20%20elif%20height%20%3E%20-100%20and%20height%20%3C%3D%200%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22This%20is%20low%20but%20not%20too%20low%21%22%29%0A%20%20%20%20elif%20height%20%3E%20-150%20and%20height%20%3C%3D%20-100%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22This%20is%20low%21%22%29%0A%20%20%20%20elif%20height%20%3E%3D%20-200%20and%20height%20%3C%3D%20-150%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22This%20is%20very%20low%21%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20raise%0Aexcept%3A%0A%20%20%20%20tina.backward%28100%29%0A%20%20%20%20tina.write%28%22Hey%2C%20that%27s%20not%20a%20number%20between%20200%20and%20-200%21%22%29%20%20%20%20%0A%20%20%20%20tina.backward%2820%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Here are a few ideas for customizing this program:
* Try changing what Tina says at the different height levels
* Try changing what the height levels are
* Extra Credit: Try changing what Tina *does* at each different height level.  Right now she just writes some words.  What else does she know how to do?  


## More Detail

Want to learn more about how `if`, `elif`, and `else` work?   Line 9, `tina.pos()[1]` asks tina how far up or down the grid she is. `elif` is short for "else if". Each of the tests of height is tried in order until one is true. If none of the tests are true, the program moves on to the lines indented below `else`.  In Python, `else` means, "if all else fails, do this". The `raise` inside the `else` block raises an error, which means switch to the `except` block. That's how the program can respond differently if you enter anything except a number in between 200 and -200.

Don't worry about understanding all of this in your first hour!  But tools like `if`, `elif`, `else`, `raise`, and `except` will give you and other programmers more control over the programs you write as you get more practice.
