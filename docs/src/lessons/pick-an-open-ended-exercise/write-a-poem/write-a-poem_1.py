import turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.penup()

def line(words, horiz_pos = -50):
    x,y = tina.pos()
    tina.goto(max(horiz_pos, -190), y)
    tina.write(words)
    x,y = tina.pos()
    tina.goto(x, y - 25)
    
def by(author):
    x,y = tina.pos()
    tina.goto(x + 70, max( -190, y -30))
    tina.write(author)
    x,y = tina.pos()
    tina.goto(0, y)
    
tina.goto(-50, 190)
line("Snow in my shoe")
line("Abandoned")
line("Sparrow's nest")
by("Jack Kerouac")
