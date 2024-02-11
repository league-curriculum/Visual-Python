import turtle

tina = turtle.Turtle()
tommy = turtle.Turtle()

tina.color('blue')
tommy.color('green')

tina.shape('turtle')
tommy.shape('turtle')

tina.begin_fill()
tina.goto(200,0)
tina.goto(200,-200)
tina.goto(-200,-200)
tina.goto(-200,0)
tina.goto(0,0)
tina.end_fill()

tommy.penup()
tommy.goto(-70,100)
tommy.write("Tina, let's Make a picture together!")
tommy.goto(0,50)
tommy.pendown()

tina.penup()
tina.color('white')
tina.goto(-40,-100)
tina.write("Alright, I'm ready!!")
tina.goto(0,-130)
tina.pendown()
