---
title: Loops Of Lists

---


So far we've been telling Tina to do things over and over.  Remember this example?

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Atina.left%2890%29%0Atina.forward%2820%29%0Atina.write%28%22What%20color%20am%20I%20now%3F%22%29%0A%0Atina.forward%2820%29%0Atina.color%28%22blue%22%29%0Atina.write%28%22What%20color%20am%20I%20now%3F%22%29%0A%0Atina.forward%2820%29%0Atina.color%28%22purple%22%29%0Atina.write%28%22What%20color%20am%20I%20now%3F%22%29%0A%0Atina.forward%2820%29%0Atina.color%28%22green%22%29%0Atina.write%28%22What%20color%20am%20I%20now%3F%22%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

There's a lot of repetition.  If we give Tina a list of colors and tell her to do the same thing with each color, we can make the same picture with much less code!

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Acolor_list%20%3D%20%5B%22black%22%2C%20%22blue%22%2C%20%22purple%22%2C%20%22green%22%5D%0A%0Atina.left%2890%29%0A%0Afor%20color%20in%20color_list%3A%0A%20%20%20%20tina.forward%2820%29%0A%20%20%20%20tina.color%28color%29%0A%20%20%20%20tina.write%28%22What%20color%20am%20I%20now%3F%22%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

We can now easily change how many times Tina draws as well.  Try adding a new color name to the list. Here's what it would look like to add `"yellow"` to the list:

```python
color_list = ["black", "blue", "purple", "green", "yellow"]
```

Don't forget the **quotes** (`""`) around your color word!

Hit a snag?  Don't worry! Tips: 
- Remember to put your color name in quotes (`""`)
- Remember to include a comma (`,`) in between each color name and the next one
- Remember to begin and end your list with square brackets (`[` and `]`)
