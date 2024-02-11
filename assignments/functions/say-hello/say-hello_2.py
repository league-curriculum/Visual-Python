import turtle
tina = turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(-60,175)

def say(something):
    x, y = tina.pos()
    tina.write("You told me to say this:")
    tina.goto(x + 10, y -10)
    tina.write(something)
    tina.goto(x, y - 25)
    
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
say("Hi there!")
