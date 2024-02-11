import turtle
tina=turtle.Turtle()
tina.shape('turle')
tina.penup()

try:
    how_high = int(input("How high should Tina go? (Use numbers between 200 and -200)"))
    tina.goto(0, how_high)
    height = tina.pos()[1]
    
    if height > 150 and height <= 200:
        tina.write("This is very high!")
    elif height > 100 and height <= 150:
        tina.write("This is high!")
    elif height > 0 and height <= 100:
        tina.write("This is high but not too high!")
    elif height > -100 and height <= 0:
        tina.write("This is low but not too low!")
    elif height > -150 and height <= -100:
        tina.write("This is low!")
    elif height >= -200 and height <= -150:
        tina.write("This is very low!")
    else:
        raise
except:
    tina.backward(100)
    tina.write("Hey, that's not a number between 200 and -200!")    
    tina.backward(20)

