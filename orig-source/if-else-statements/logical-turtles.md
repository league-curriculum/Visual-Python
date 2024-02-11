Turtles are very logical.  They can change what they do based on what we tell them.

Run this program and answer the question.  Tina will tell you whether you're right!

```python.run
import turtle

tina = turtle.Turtle()

Guess = int(input("What is 2 X 7?"))

if Guess == 2*7:
    tina.write(str(Guess) + ' is correct!')
    tina.penup()
    tina.backward(10)
else:
    tina.write('You said ' + str(Guess) + '. I got ' + str(2*7))
    tina.penup()
    tina.backward(10)
```

What else can you make Tina ask?  Try changing the numbers of the math problem.