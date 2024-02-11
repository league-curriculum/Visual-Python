import turtle
tina = turtle.Turtle()
tina.shape('turtle')

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

for each_color in colors:
    angle = 360 / len(colors)
    tina.color(each_color)
    tina.circle(40)
    tina.right(angle)
    tina.forward(30)
