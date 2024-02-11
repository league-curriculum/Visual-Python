---
title: Make 5 Cakes

---


One of the great things about functions is that they can repeat complicated instructions without us having to repeat ourselves in code!

Earlier we talked about how **functions are like recipes**. In this exercise, we've already taught Tina the recipe for making a picture of a cake and she's made three.  Tell her to make more cakes by **calling** the function with different `x` and `y` locations at the very bottom of the program.  

How many cakes should she make?

<iframe width="100%" height="500" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%3Dturtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Adef%20make_cake%28x%3D0%2C%20y%3D0%29%3A%0A%20%20%20%20tina.penup%28%29%0A%20%20%20%20tina.color%28%27pink%27%29%0A%20%20%20%20tina.goto%28x%2C%20y%29%0A%20%20%20%20tina.pendown%28%29%0A%20%20%20%20tina.begin_fill%28%29%0A%20%20%20%20tina.goto%28x%20%2B%2020%2C%20y%29%0A%20%20%20%20tina.goto%28x%20%2B%2020%2C%20y%20%2B%2020%29%0A%20%20%20%20tina.goto%28x%20-%2020%2C%20y%20%2B%2020%29%0A%20%20%20%20tina.goto%28x%20-%2020%2C%20y%29%0A%20%20%20%20tina.goto%28x%2C%20y%29%20%20%0A%20%20%20%20tina.end_fill%28%29%0A%20%20%20%20tina.goto%28x%2C%20y%20%2B%2020%29%0A%20%20%20%20tina.color%28%27yellow%27%29%0A%20%20%20%20tina.goto%28x%2C%20y%20%2B%2035%29%0A%20%20%20%20tina.goto%28x%2C%20y%20%2B%2030%29%0A%20%20%20%20tina.color%28%27black%27%29%0A%20%20%20%20tina.goto%28x%2C%20y%20%2B%2020%29%0A%20%20%20%20tina.penup%28%29%0A%20%20%20%20tina.goto%28x%2C%20y%20%2B%2010%29%0A%20%20%20%20%0Amake_cake%280%2C0%29%0Amake_cake%28-100%2C0%29%0Amake_cake%28100%2C0%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Hint: The first number in `make_cake()` is **how far left or right** Tina should go, while the second is **how high or low** she should go before starting to draw.



---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.
