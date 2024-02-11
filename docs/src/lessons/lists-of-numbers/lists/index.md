---
title: Lists

---


Lists are very useful in programming.  In Python, lists look like this:

```python
["A", "List", "of", "Things"]
```

When things are in a list, we can tell Python to pull them out for us.  We just need to point to the right **index** number of the list.  Here's a diagram of the index numbers for the list above:

![Screen Shot 2014-09-28 at 5.01.51 PM.jpg](/api/files/5428a1b8d61e38df4eca1d46/Screen-Shot-2014-09-28-at-5-01-51-PM.jpeg "Screen Shot 2014-09-28 at 5.01.51 PM.jpg")

Let's ask Tina to help explain:

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.penup%28%29%0Ax%20%3D%20-80%3B%20y%20%3D%20175%3B%20tina.goto%28x%2C%20y%29%0A%0Aour_list%20%3D%20%5B%22A%22%2C%20%22List%22%2C%20%22of%22%2C%20%22Things%22%5D%0A%0Atina.write%28%22The%20code%20our_list%5B0%5D%20gives%20us%20the%20first%20thing%20in%20the%20list%3A%22%29%0Atina.goto%28x%20%2B%2010%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28our_list%5B0%5D%29%0Atina.goto%28x%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28%22The%20code%20our_list%5B1%5D%20gives%20us%20the%20second%20thing%20in%20the%20list%3A%22%29%0Atina.goto%28x%20%2B%2010%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28our_list%5B1%5D%29%0Atina.goto%28x%2C%20y%20-20%29%3B%20x%2C%20y%20%3D%20tina.pos%28%29%0Atina.write%28%22The%20code%20our_list%5B2%5D%20gives%20us%20the%20third%20thing%20in%20the%20list%3A%22%29%0Atina.goto%28x%20%2B%2010%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28our_list%5B2%5D%29%0Atina.goto%28x%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28%22The%20code%20our_list%5B3%5D%20gives%20us%20the%20third%20thing%20in%20the%20list%3A%22%29%0Atina.goto%28x%20%2B%2010%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28our_list%5B3%5D%29%0Atina.goto%28x%2C%20y%20-40%29%3By%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28%22And%20here%27s%20the%20whole%20list%20again%3A%22%29%0Atina.goto%28x%20%2B%2010%2C%20y%20-20%29%3B%20y%20%3D%20tina.pos%28%29%5B1%5D%0Atina.write%28str%28our_list%29%29%0Atina.goto%280%2C-160%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.
