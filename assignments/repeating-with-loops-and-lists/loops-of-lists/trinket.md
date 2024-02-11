So far we've been telling Tina to do things over and over.  Remember this example?

{{ trinket("loops-of-lists_1.py", width="100%", height="800", embed_type="python") | safe }}

There's a lot of repetition.  If we give Tina a list of colors and tell her to do the same thing with each color, we can make the same picture with much less code!

{{ trinket("loops-of-lists_2.py", width="100%", height="800", embed_type="python") | safe }}

We can now easily change how many times Tina draws as well.  Try adding a new color name to the list. Here's what it would look like to add `"yellow"` to the list:

```python
color_list = ["black", "blue", "purple", "green", "yellow"]
```

Don't forget the **quotes** (`""`) around your color word!

Hit a snag?  Don't worry! Tips: 
- Remember to put your color name in quotes (`""`)
- Remember to include a comma (`,`) in between each color name and the next one
- Remember to begin and end your list with square brackets (`[` and `]`)

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.