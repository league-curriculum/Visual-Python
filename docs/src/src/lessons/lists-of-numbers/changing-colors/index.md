---
title: Changing Colors

---



We can loop over a list of colors and tell Tina to turn that color.

<iframe src="//player.vimeo.com/video/107875423?title=0&amp;byline=0&amp;portrait=0" width="600" height="337" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> 

Run this program, and see where the colors come from.  What happens if you add or remove colors from the list?

<iframe width="100%" height="800" src="https://trinket.io/tools/1.0/jekyll/embed/python#code=import%20turtle%0Atina%20%3D%20turtle.Turtle%28%29%0Atina.shape%28%27turtle%27%29%0A%0Acolors%20%3D%20%5B%22red%22%2C%20%22orange%22%2C%20%22yellow%22%2C%20%22green%22%2C%20%22blue%22%2C%20%22purple%22%2C%20%22black%22%5D%0A%0Afor%20each_color%20in%20colors%3A%0A%20%20%20%20angle%20%3D%20360%20/%20len%28colors%29%0A%20%20%20%20tina.color%28each_color%29%0A%20%20%20%20tina.circle%2840%29%0A%20%20%20%20tina.right%28angle%29%0A%20%20%20%20tina.forward%2830%29" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Want to make this program your own?  Change what tina does inside the `for` loop.  What else could she do for each color?
