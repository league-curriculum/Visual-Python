---
title: Lists Of Numbers

---



Until now, we've had to write out numbers every time we want Tina to move.  We can use a list of numbers and a loop to get her to move many times!

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Anumber_list%20%3D%20%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C8%2C9%2C10%5D%20%0A%0Atina.color%28%22green%22%29%20%0Afor%20number%20in%20number_list%3A%20%0A%20%20%20%20tina.forward%28number%2A10%29%20%0A%20%20%20%20tina.left%2860%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

The code `number_list = [1,2,3,4,5,6,7,8,9,10]` is where Tina gets her numbers from.  Can you change the numbers in the list to change how she moves?  Make sure that your list starts and ends with square brackets (`[]`), and has a comma (`,`) in between every number.
