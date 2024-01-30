Turtles can determine whether a number is above or below another number.  Let's write a program that asks how old you are:

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

try:
    age = int(input("How old are you? (Use numbers)"))
    if age >= 10 and age <= 15:
        tina.write("You're between 10 and 15 years old")
        tina.backward(20)
    elif age < 10:
        tina.write("You're less than 10 years old")
        tina.backward(20)
    elif age > 15:
        tina.write("You're over 15 years old")
        tina.backward(20)
except:
    tina.backward(100)
    tina.write("I don't think I understand that age.  Are you using numbers?")
    tina.backward(20)
```

**Advanced:** In the example above you'll see there are `try:` and `except:`.  These lines try to run code that comes after `try:`, and if any errors happen, do what's in the `except:` section.  This is how Tina knows whether you put in a real number like `15`.  This is how real programmers change the behavior of programs based on any errors that might come up.