import turtle
tina = turtle.Turtle()
tina.shape('turtle')

color_list = ["black", "blue", "purple", "green"]

tina.left(90)

for color in color_list:
    tina.forward(20)
    tina.color(color)
    tina.write("What color am I now?")
