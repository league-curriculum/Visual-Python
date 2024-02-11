---
title: Saying Hello

---


Tina's already said hello but you can tell her your name and she'll say hello to you.

<iframe src="//player.vimeo.com/video/107445354?title=0&amp;byline=0&amp;portrait=0" width="600" height="338" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

First, find the line where Tina says `"Why, hello there!"`.  Next, change it so that she's saying hello to you.  My name is Elliott, so I'd change what she says to `"Why, hello Elliott!"`

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.penup%28%29%0Atina.forward%2820%29%0Atina.write%28%22Why%2C%20hello%20there%21%22%29%0Atina.backward%2820%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The program you wrote above is great for people that have the same name as you, but what if someone has a different name?  We can write a program that asks for your name with the `input` function, so that Tina can get it right for anyone's name.  Run this program and enter your name:

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Ayour_name%20%3D%20input%28%22What%27s%20your%20name%3F%22%29%0A%0Atina.penup%28%29%0Atina.forward%2820%29%0Atina.write%28%22Why%2C%20hello%2C%20%22%20%2B%20your_name%20%2B%20%22%21%22%29%0Atina.backward%2820%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The `input` function is what makes the program ask you for your name.  Whatever you type in is then stored in a `variable`.  Tina uses this variable to remember and then say your name!

We can teach Tina to say anything we want using `input`.  Can you add `input` to this program so that anyone who runs it can tell Tina what to say?

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Asay_what%20%3D%20%22What%20should%20I%20say%3F%22%0A%0Atina.penup%28%29%0Atina.forward%2820%29%0Atina.write%28say_what%29%0Atina.backward%2820%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Hint: the `say_what` variable is what Tina says in this program. How can we use `input` like we did above that the program will ask whoever runs the program what the variable should be?
