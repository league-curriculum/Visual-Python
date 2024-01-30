
Until now, we've had to write out numbers every time we want Tina to move.  We can use a list of numbers and a loop to get her to move many times!

```python.run
import turtle
tina = turtle.Turtle()
tina.shape('turtle')

number_list = [1,2,3,4,5,6,7,8,9,10] 

tina.color("green") 
for number in number_list: 
    tina.forward(number*10) 
    tina.left(60) 
```

The code `number_list = [1,2,3,4,5,6,7,8,9,10]` is where Tina gets her numbers from.  Can you change the numbers in the list to change how she moves?  Make sure that your list starts and ends with square brackets (`[]`), and has a comma (`,`) in between every number.