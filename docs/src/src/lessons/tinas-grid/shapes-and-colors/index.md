---
title: Shapes And Colors

---


Now it is your turn to try your own turtle program, by using hints from your previous programs. First, let's review your last turtle program: 

```python.run:height=400  
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
```

For the program you are going to write, you need to know one more thing: how to write a loop. A loop does something over and over. The loop in the program below is made by the line ``for i in range(4)``. This line will cause the indented code below if multiple times. First, guess how many times the turtle will print "Where Am I"
and then run the program to see if you are right.

```python.run:height=400 
import turtle
tina = turtle.Turtle()

tina.right(90)

for i in range(3):
    tina.forward(30)
    tina.write("Where Am I")
```

Now we can get to writing your own program. Use what you know about Tina the Turtle from previous programs, and what you've just learned about loops to write the program below. Read the comments for hints about what you should do. 

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0A%0A%0Awindow%20%3D%20turtle.Screen%28%29%0Awindow.bgcolor%28%27white%27%29%0A%0A%23%20This%20code%20makes%20a%20new%20Turtle.%20Pick%20a%20new%20name%20for%20the%20turtle%0Amy_turtle%20%3D%20turtle.Turtle%28%29%0A%0A%23%20Make%20your%20turtle%27s%20shape%20%27turtle%27%2C%20.shape%28%27turtle%27%29%0A%0A%23%20Set%20your%20turtle%27s%20speed%20using%20.speed%282%29%0A%0A%23%20Set%20your%20turtle%27s%20color%20using%20.color%28%27green%27%29%20and%20.pencolor%28%27blue%27%29%0A%0A%23%20Move%20your%20turtle%20forward%20using%20.forward%28100%29%0A%23%20TEST%20%20%20%20Did%20your%20turtle%20move%20forward%3F%0A%0A%23%20Move%20your%20turtle%20left%20or%20right%20using%20.left%2890%29%20or%20.right%2890%29%0A%0A%23%20Now%20put%20the%20forward%20and%20left/right%20code%20into%20a%20for%20loop%20to%20repeat%204%20times.%0A%23%20TEST%20%20%20%20Did%20your%20turtle%20draw%20a%20square%3F%0A%0A%23%20Move%20your%20turtle%20to%20a%20new%20place%20on%20the%20screen%20using%20.goto%28x%2C%20y%29%0A%23%20x%3D0%20and%20y%3D0%20is%20the%20center%20of%20the%20screen%0A%0A%23%20Have%20your%20turtle%20draw%20a%20circle%20using%20.circle%28radius%2C%20steps%3D30%29%0A%23%20TEST%20%20%20%20Did%20your%20turtle%20draw%20a%20circle%3F%0A%0A%23%20Add%20color%20to%20your%20shape%20by%20adding%20.begin_fill%28%29%20before%20drawing%20the%20circle%0A%23%20and%20.end_fill%28%29%20below%0A%0A%23%20Draw%203%20more%20shapes%20with%20different%20fill%20colors%21%0A%0A%23%20%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%20DO%20NOT%20EDIT%20THE%20CODE%20BELOW%20%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%3D%0Aturtle.done%28%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Don't worry if you don't understand all of the code.  You don't have to to get started, and more and more of it will become familiar to you as you keep going.

Use the arrow or click Next to go to the next example!
