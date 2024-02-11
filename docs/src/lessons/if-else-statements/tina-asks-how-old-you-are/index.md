---
title: Tina Asks How Old You Are

---


Turtles can determine whether a number is above or below another number.  Let's write a program that asks how old you are:

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0Atina.penup%28%29%0A%0Atry%3A%0A%20%20%20%20age%20%3D%20int%28input%28%22How%20old%20are%20you%3F%20%28Use%20numbers%29%22%29%29%0A%20%20%20%20if%20age%20%3E%3D%2010%20and%20age%20%3C%3D%2015%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22You%27re%20between%2010%20and%2015%20years%20old%22%29%0A%20%20%20%20%20%20%20%20tina.backward%2820%29%0A%20%20%20%20elif%20age%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22You%27re%20less%20than%2010%20years%20old%22%29%0A%20%20%20%20%20%20%20%20tina.backward%2820%29%0A%20%20%20%20elif%20age%20%3E%2015%3A%0A%20%20%20%20%20%20%20%20tina.write%28%22You%27re%20over%2015%20years%20old%22%29%0A%20%20%20%20%20%20%20%20tina.backward%2820%29%0Aexcept%3A%0A%20%20%20%20tina.backward%28100%29%0A%20%20%20%20tina.write%28%22I%20don%27t%20think%20I%20understand%20that%20age.%20%20Are%20you%20using%20numbers%3F%22%29%0A%20%20%20%20tina.backward%2820%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

**Advanced:** In the example above you'll see there are `try:` and `except:`.  These lines try to run code that comes after `try:`, and if any errors happen, do what's in the `except:` section.  This is how Tina knows whether you put in a real number like `15`.  This is how real programmers change the behavior of programs based on any errors that might come up.

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.
