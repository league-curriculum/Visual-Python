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
