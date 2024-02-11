---
title: Tinas Pen

---


Turtles like Tina have a pen that draws when they move.  We can tell them to pick the pen up, so that they can move without drawing a line.  Then we can tell them to put the pen down, and they'll draw again.  We tell them this with the `penup()` and `pendown()` commands.

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.penup%28%29%0Atina.goto%280%2C100%29%0Atina.write%28%22I%20don%27t%20draw%20when%20my%20pen%20is%20up%21%22%29%0Atina.goto%280%2C50%29%0Atina.pendown%28%29%0Atina.write%28%22I%20do%20draw%20when%20my%20pen%20is%20down%21%22%29%0Atina.goto%28-50%2C50%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
