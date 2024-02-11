Tina can ask us things, and we can also tell her to ask herself things. In this example, we'll tell her to go to a high or low spot on the screen and she'll change what she says depending on how high or low she is.

{{ trinket("how-high-up-is-tina_1.py", width="100%", height="500", embed_type="python") | safe }}

Here are a few ideas for customizing this program:
* Try changing what Tina says at the different height levels
* Try changing what the height levels are
* Extra Credit: Try changing what Tina *does* at each different height level.  Right now she just writes some words.  What else does she know how to do?  


## More Detail

Want to learn more about how `if`, `elif`, and `else` work?   Line 9, `tina.pos()[1]` asks tina how far up or down the grid she is. `elif` is short for "else if". Each of the tests of height is tried in order until one is true. If none of the tests are true, the program moves on to the lines indented below `else`.  In Python, `else` means, "if all else fails, do this". The `raise` inside the `else` block raises an error, which means switch to the `except` block. That's how the program can respond differently if you enter anything except a number in between 200 and -200.

Don't worry about understanding all of this in your first hour!  But tools like `if`, `elif`, `else`, `raise`, and `except` will give you and other programmers more control over the programs you write as you get more practice.

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.