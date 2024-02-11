import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
x = -80; y = 175; tina.goto(x, y)

our_list = ["A", "List", "of", "Things"]

tina.write("The code our_list[0] gives us the first thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[0])
tina.goto(x, y -20); y = tina.pos()[1]
tina.write("The code our_list[1] gives us the second thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[1])
tina.goto(x, y -20); x, y = tina.pos()
tina.write("The code our_list[2] gives us the third thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[2])
tina.goto(x, y -20); y = tina.pos()[1]
tina.write("The code our_list[3] gives us the third thing in the list:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(our_list[3])
tina.goto(x, y -40);y = tina.pos()[1]
tina.write("And here's the whole list again:")
tina.goto(x + 10, y -20); y = tina.pos()[1]
tina.write(str(our_list))
tina.goto(0,-160)
